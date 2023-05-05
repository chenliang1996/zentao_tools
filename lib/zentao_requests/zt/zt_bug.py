# -*- coding: utf-8 -*-
# @Author chenliangliang
# @Time: 2023/4/27 13:56
# @File: zt_bug.py
import json
import os

from requests import HTTPError

from commond.config import setting, Yaml
from commond.logger import logger
from lib.zentao_requests.zt.ztbase import ZenTao
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)


class Requests_Bug(ZenTao):
    """
    Bug的线管的请求接口
    """
    editd_bug_url = r'/bug-edit-{}.json?zentaosid={}'
    closed_bug_url = r'/bug-edit-{}.json?zentaosid={}'
    activated_bug_url = r'/bug-edit-{}.json?zentaosid={}'
    resolved_bug_url = r'/bug-edit-{}.json?zentaosid={}'
    opened_bug_url = r'/bug-create-{}.json?zentaosid={}'
    bugconfirmed_bug_url = r'/bug-confirmBug-{}.json?zentaosid={}'
    assigned_bug_url = r'/bug-assignTo-{}.json?zentaosid={}'

    def bug_request(self, action, data_json, bug_id):
        """
        请求分发方法，根据不同的行为实施不同的请求。
        :param action:
        :param bug_id:
        :param data_json:
        :return:
        """
        url = ''
        if action == 'edited':
            url = setting.yaml['zentao']['url'] + self.editd_bug_url.format(bug_id, self.sid)
            # self.edit_bug(data_json, bug_id)
        elif action == 'closed':
            self.close_bug(data_json)
        elif action == 'activated':
            self.activate_bug(data_json)
        elif action == 'resolved':
            self.resolve_bug(data_json)
        elif action == 'opened':
            self.create_bug(data_json)
        elif action == 'bugconfirmed':
            self.confirme_bug(data_json)
        elif action == 'assigned':
            self.assigned_bug(data_json)
        # else:
        #     pass
        if not url:
            logger.error(
                f'action参数错误，错误的action:{action},正确的如下：editd,closed,activated,resolved,opened,bugconfirmed,assigned')
            raise ValueError('action参数错误')
        response = self.rc.request(url, method='POST', data=data_json)
        data_dict = response.json()
        data = data_dict['data']
        data = json.loads(data.encode('utf-8').decode('unicode_escape'))
        logger.info(response.status_code, data.get('locate', ''))
        if response.status_code != 200:
            logger.warning(f'状态码：{response.status_code}', response.text)
            raise HTTPError('连接错误')
        elif data.get('result', '') == 'fail':
            logger.error(f'{action}失败，{data.get("message")},传入的data{data_json}')
            raise KeyError('传入的字段或值有误')
    #
    # def get_view_bug(self, bug_id):
    #     """
    #     通过数据库请求获取bug.json 用于bug信息
    #     :param bug_id: 带获取的Bug_id
    #     :return: 返回获取到的Bug信息
    #     """
    #
    #     pass
    #
    # def edit_bug(self, data_json, bug_id):
    #     """
    #     编辑Bug的接口
    #     :param data_json:
    #     :param bug_id:
    #     :return:
    #     """
    #     url = setting.yaml['zentao']['url'] + self.edit_bug_url.format(bug_id, self.sid)
    #     response = self.rc.request(url, method='POST', data=data_json)
    #     data_dict = response.json()
    #     data = data_dict['data']
    #     data = json.loads(data.encode('utf-8').decode('unicode_escape'))
    #     logger.info(response.status_code, data.get('locate', ''))
    #     if response.status_code != 200:
    #         logger.warning(f'状态码：{response.status_code}', response.text)
    #         raise HTTPError('连接错误')
    #     elif data.get('result', '') == 'fail':
    #         logger.error(f'编辑失败，{data.get("message")},传入的data{data_json}')
    #         raise KeyError('传入的字段或值有误')
    #
    # def confirme_bug(self, data_json):
    #     """
    #     编辑Bug的接口
    #     :param data_json:
    #     :return:
    #     """
    #     default_edit_data = ''
    #     self.rc.request()
    #
    # def create_bug(self, data_json):
    #     """
    #     创建Bug的json
    #     :param data_json:
    #     :return:
    #     """
    #     default_create_data = ''
    #     self.rc.request()
    #
    # def activate_bug(self, data_json):
    #     """
    #     创建Bug的json
    #     :param data_json:
    #     :return:
    #     """
    #     default_create_data = ''
    #     self.rc.request()
    #
    # def close_bug(self, data_json):
    #     """
    #     创建Bug的json
    #     :param data_json:
    #     :return:
    #     """
    #     default_create_data = ''
    #     self.rc.request()
    #
    # def assigned_bug(self, data_json):
    #     """
    #     创建Bug的json
    #     :param data_json:
    #     :return:
    #     """
    #     default_create_data = ''
    #     self.rc.request()
    #
    # def resolve_bug(self, data_json):
    #     """
    #     创建Bug的json
    #     :param data_json:
    #     :return:
    #     """
    #     default_create_data = ''
    #     self.rc.request()


if __name__ == '__main__':
    rst_bug = Requests_Bug('admin', password='Kbd@2022', freePasswd=False)
    rst_bug.bug_request('edited',
                        {'title': '3213213',
                         'steps': '<p>[步骤]</p>\n<br />\n<p>[结果]</p>\n<br />\n<p>[期望]</p>\n<br />',
                         'comment': None, 'yuanyinfenxi': '231321', 'probability': '100%percent', 'source': 'qualityFB',
                         'factoryIDrefer': '', 'customerIDrefer': '', 'planresolve': '',
                         'Vresult': '注：多版本验证时，回归几个版本则填写几次验证结果 <br /><br />【回归软件版本】：<br />【回归数据版本】：<br />【预置条件】：<br />【回归结果】：<br />【回归次数】：<br />【附件】：',
                         'Discoverylink': 'ReviewDesign', 'product': 7, 'module': 411, 'plan': 0, 'type': 'TestError',
                         'severity': 3, 'pri': 3, 'status': 'active', 'subStatus': 'activate', 'assignedTo': 'admin',
                         'deadline': '0000-00-00', 'feedbackBy': '【202304251041】何凯', 'notifyEmail': '', 'os[]': None,
                         'browser[]': None, 'identify': 0, 'keywords': '', 'contactListMenu': None, 'project': 8,
                         'execution': 0, 'story': 0, 'task': 0, 'openedBuild': 'trunk', 'resolvedBy': '',
                         'resolvedDate': '', 'resolvedBuild': '', 'resolution': '', 'duplicateBug': 0, 'closedBy': '',
                         'closedDate': '', 'testtask': 0, 'case': 0}, 15652)
