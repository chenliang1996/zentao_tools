# -*- coding: utf-8 -*-
# @Author chenliangliang
# @Time: 2023/4/18 10:07
# @File: zt_caselib.py
import json
import re
import warnings

from commond.common import check_key_in_dict
from urllib3.exceptions import HTTPError
from commond.config import setting
from commond.logger import logger
from lib.zentao_datas.case_data import RequestCaseData
from lib.zentao_requests.zt.ztbase import ZenTao

warnings.filterwarnings("ignore", category=DeprecationWarning)


class Case_lib(ZenTao):
    """
    用例库接口类
    """
    case_lib_url = r'/caselib-browse-{}.json'
    case_url = r'/testcase-view-{}.json'
    edit_case_url = r'/testcase-edit-{}.json'
    put_testcase_url = r'biz/api.php/v1/testcases/{}'

    def get_cases(self, lib_id):
        """
        获取对应用例库ID的全部信息
        :param lib_id: 用例库ID
        :return:
        """
        url = setting.yaml['zentao']['url'] + self.case_lib_url.format(lib_id)
        response = self.rc.request(url, 'GET')
        if response.status_code != 200:
            logger.warning(f'状态码：{response.status_code}', response.text)
            raise HTTPError('连接错误')
        data_dict = response.json()
        data = data_dict['data']
        data = json.loads(data.encode('utf-8').decode('unicode_escape'))
        return data

    def put_testcase_by_id(self, data_dict, case_id):
        """
        修改测试用例
        默认'Scriptpath'需要修改的字段
        data = {
            "scriptpath": "1111",
        }
        :return: True/False
        """

        url = setting.yaml['zentao']['url'] + self.put_testcase_url.format(case_id)
        if isinstance(data_dict, dict):
            data = json.dumps(data_dict)
        else:
            data = data_dict
        response = self.rc.request(url, method='PUT', data=data)
        # response = self.rc.request(url, method='GET')
        logger.debug(response.status_code, response.text)
        if response.status_code != 200:
            logger.warning(f'状态码：{response.status_code}', response.text)
            raise HTTPError('连接错误')

    def edit_testcase_by_id(self, data_dict, case_id):
        """
        修改测试用例
        默认'Scriptpath'需要修改的字段
        data = {
            "scriptpath": "1111",
        }
        :return: True/False
        """

        url = setting.yaml['zentao']['url'] + self.edit_case_url.format(case_id)
        case_data = self.get_case_data_by_id(case_id)
        # 修改获取到的
        case_data_object = RequestCaseData()
        case_data_object.init_default_data(case_data)
        case_data = case_data_object.get_new_edit_data(data_dict)
        uid = self.get_uid(url.replace('.json', '.html'))
        case_data['uid'] = uid
        response = self.rc.request(url, method='POST', data=case_data)
        logger.debug(response.status_code, response.text)
        if response.status_code != 200:
            logger.warning(f'状态码：{response.status_code}', response.text)
            raise HTTPError('连接错误')

    def get_case_data_by_id(self, case_id):
        """
        通过case_id获取case的值
        :param case_id:
        :return:
        """
        url = setting.yaml['zentao']['url'] + self.case_url.format(case_id)
        response = self.rc.request(url, 'GET')
        if response.status_code != 200:
            logger.warning(f'状态码：{response.status_code}', response.text)
            raise HTTPError('连接错误')
        data_dict = response.json()
        data = data_dict['data']
        case_data = json.loads(data.encode('utf-8').decode('unicode_escape'), strict=False)['case']
        return case_data

    def get_uid(self, url):
        """POST传参uid字段获取"""
        # headers = {"Referer": r'http://172.16.101.67/index-index.html?tid=2b6nydlk'}
        self.rc.MySessions.headers.update({'Referer': r'http://172.16.101.67/index-index.html?tid=2b6nydlk'})
        response = self.rc.request(url, "GET").text
        uid = re.findall("var kuid = '(.*?)';", response, )[0]
        return uid
        # print(uid)


if __name__ == '__main__':
    cl = Case_lib('admin', password='Kbd@2022', freePasswd=False)
    # cl.get_cases(142)
    data1 = {"title": "交通信号灯validity属性为所关联道路所有车道222"}
    cl.edit_testcase_by_id(data1, 26830)
    # cl.get_uid('http://172.16.101.67/testcase-edit-26830.html')
