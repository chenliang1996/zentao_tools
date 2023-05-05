# -*- coding: utf-8 -*-
# @Author chenliangliang
# @Time: 2023/4/15 11:20
# @File: ztbase.py
import json
import time
from hashlib import md5

from commond.config import setting
from lib.api_base.rest_client import RestClient


class ZenTao:
    """
    禅道的基础对象，用于执行登录，获取全部产品、项目、迭代/执行等
    """
    login_url = r'/api.php?m=user&f=apilogin&account={}&code={}&time={}&token={}&zentaosid={}'
    get_token = r'/api.php/v1/tokens'
    get_sessionid = r'/api-getsessionid.json'

    def __init__(self, account, password='', freePasswd=False):
        """
        初始化
        """
        self.rc = RestClient()
        self.sid = self.get_sid()
        self.login(account, password=password, freePasswd=freePasswd)
        self.us_name = account

    def get_sid(self):
        url = setting.yaml['zentao']['url'] + self.get_sessionid
        response = self.rc.request(method='GET', url=url)
        if response.status_code == 200:
            data_dict = response.json()
            data = data_dict['data']
            data = json.loads(data.encode('utf-8').decode('unicode_escape'))
            sid = data['sessionID']
            # print(sid)
            return sid
        else:
            assert TimeoutError('连接超时')

    def login(self, account, password='', freePasswd=False):
        """
        登录
        :param account:
        :param password:
        :param freePasswd: 免密登录  False代表不启用
        :return:
        """

        if freePasswd:
            code = setting.yaml['zentao']['code']
            key = setting.yaml['zentao']['key']
            timeamp = str(int(time.time()))
            encoded_string = (code + key + timeamp).encode()
            token = md5(encoded_string).hexdigest()
            login_url = setting.yaml['zentao']['url'] + self.login_url.format('admin', code, timeamp, token, self.sid)
            response = self.rc.request(url=login_url, method='GET')
            # response = self.rc.request(url=fr"{setting.yaml['zentao']['url']}/project-bug-101.json", method='GET')
            if response.status_code != 200:
                assert TimeoutError('连接超时')
            elif response.status_code == 401:
                assert KeyError('缺少参数或应用未设置密钥')
            elif response.status_code == 403:
                assert KeyError('被限制访问')
            elif response.status_code == 404:
                assert KeyError('应用不存在')
            elif response.status_code == 405:
                assert KeyError('token已失效')
            elif response.status_code == 406:
                assert KeyError('用户不存在')
            elif response.status_code == 407:
                assert KeyError('错误的时间戳')
            # print(response.status_code)
            # print(response.text)
        else:
            data = json.dumps({'account': account, 'password': password})

            login_url = setting.yaml['zentao']['url'] + self.get_token
            response = self.rc.request(url=login_url, method='POST',
                                       data=data)
            if response.status_code != 200:
                assert TimeoutError('连接超时')


if __name__ == '__main__':
    zantao = ZenTao('admin', password='Kbd@2022', freePasswd=False)
    # zantao.get_sid()
