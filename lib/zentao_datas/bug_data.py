# -*- coding: utf-8 -*-
# @Author chenliangliang
# @Time: 2023/4/27 16:23
# @File: bug_data.py
# @说明: 用来构建Bug请求的data值
import json
import os

from commond.config import setting, Yaml, config_csv
from lib.zentao_mysql.base_conect import zentao_sql


class RequestBugData:
    def __init__(self):
        # 获取config的配置
        config_yaml_path = os.path.join(setting.path.yamls_path, 'convert_config.yaml')
        self.convert_config = Yaml(config_yaml_path).data

        config_yaml_path = os.path.join(setting.path.yamls_path, 'init_config.yaml')
        self.init_config = Yaml(config_yaml_path).data

        # 获取对应动作的接口需要的data
        bug_field_path = os.path.join(setting.path.yamls_path, 'bug_field.yaml')
        self.bug_field = Yaml(bug_field_path).data

    #     self.default_edit_data = bug_field_yaml['editd']
    #     # self.default_closed_data = bug_field_yaml['closed']
    #     # self.default_activated_data = bug_field_yaml['activated']
    #     # self.default_resolved_data = bug_field_yaml['resolved']
    #     self.default_opened_data = bug_field_yaml['opened']
    #     # self.default_bugconfirmed_data = bug_field_yaml['bugconfirmed']
    #     # self.default_assigned_data = bug_field_yaml['assigned']

    def get_data(self, bug_id, action, data_dict):
        """
        传入通过view-case-id接口获取到的值
        :param data_dict: 待修改的值(下载的Bug_json信息)
        :param action: 动作信息
        :type bug_id: 研发/生产的Bugid
        :return: 返回初始化完的Bug信息
        """
        get_bug_by_id_sql = f'select * from zt_bug where id = {bug_id}'
        bug_df = zentao_sql.product_table_df(sql=get_bug_by_id_sql)
        timestamp_cols = bug_df.select_dtypes(include=['datetime64']).columns
        bug_df[timestamp_cols] = bug_df[timestamp_cols].applymap(lambda x: str(x))
        bug_dict = {}
        try:
            bug_dict = bug_df.to_dict('records')[0]
        except IndexError as e:
            assert KeyError(f'{bug_id},Bug_id不存在')

        # 第一次根据获取的原Bug信息初始化data
        default_data = self.convert_data(bug_dict, action)
        # 第二次根据下载的data信息更新初始化的data信息
        return_data = self.convert_data(data_dict, action, default_data)

        return return_data

    def convert_data(self, data, action, action_bug_field=None):
        """
        通用方法，将下载的data根据action转换为需要的json/dict
        :param action_bug_field: 待修改的数据
        :param action: 对应的接口
        :param data: 下载的data
        :return:
        """
        config = self.convert_config
        if not action_bug_field:  # 代表是初始化行为参数
            config = self.init_config
            if action in self.bug_field:
                action_bug_field = self.bug_field[action]
            else:
                action_bug_field = {}

        if action in config:
            action_config = config[action]
        else:
            action_config = {}

        # Update field.yaml according to conditions
        for key, value in data.items():
            if key in action_config:
                entry = action_config[key]
                if 'conditions' in entry:
                    conditions = entry['conditions']
                    for condition in conditions:
                        fields = condition['fields']
                        with_condition = eval(condition['condition'], {"data": data})
                        with_fields = isinstance(fields, list)
                        if with_condition and with_fields:
                            for field in fields:
                                if field in action_bug_field:
                                    action_bug_field[field] = condition['value']
                else:
                    fields = entry['fields']
                    for field in fields:
                        if field in action_bug_field:
                            if 'value' in entry:
                                action_bug_field[field] = entry['value']
                            else:
                                action_bug_field[field] = value
            else:
                if key not in action_bug_field:
                    continue
                action_bug_field[key] = value
        return action_bug_field


if __name__ == '__main__':
    bug_data_object = RequestBugData()
    # view_data = {'id': '26830', 'project': '0', 'product': '0', 'execution': '0', 'branch': '0', 'lib': '21',
    #              'module': '0', 'path': '0', 'story': '0', 'storyVersion': '1',
    #              'title': '交通信号灯validity属性为所关联道路所有车道2',
    #              'precondition': '交通信号灯objid在EFD数据表efd_obj_road_connection中所关联道路的laneseq数值存在255情况+2',
    #              'keywords': 'ZF', 'pri': '2', 'type': 'feature', 'auto': 'no', 'frame': '', 'stage': 'feature',
    #              'howRun': '', 'script': '', 'scriptedBy': '', 'scriptedDate': '', 'scriptStatus': '',
    #              'scriptLocation': '', 'status': 'normal', 'color': '', 'frequency': '1', 'order': '0',
    #              'openedBy': 'admin', 'openedDate': '2022-10-14 09:24:41', 'reviewedBy': '', 'reviewedDate': '',
    #              'lastEditedBy': 'admin', 'lastEditedDate': '2023-04-19 17:06:41', 'version': '12', 'linkCase': '',
    #              'fromBug': '0', 'fromCaseID': '0', 'fromCaseVersion': '1', 'deleted': '0', 'lastRunner': '',
    #              'lastRunDate': '', 'lastRunResult': '', 'execute': '', 'CaseSource': 'SW_Req', 'automatic': 'Yes',
    #              'scriptroute': '', 'CaseSequence': '4444', 'subStatus': '', 'toBugs': [], 'files': [],
    #              'currentVersion': '12', 'steps': {
    #         '361665': {'id': '361665', 'parent': '0', 'case': '26830', 'version': '12', 'type': 'step',
    #                    'desc': '使用OpenDRIVEEditor软件打开OD数据，在工具视图界面中显示信号灯分布+1',
    #                    'expect': '数据工具打开显示正常'},
    #         '361666': {'id': '361666', 'parent': '0', 'case': '26830', 'version': '12', 'type': 'step',
    #                    'desc': '以文本文档方式打开OD数据，查看交通信号灯<validity>属性',
    #                    'expect': '信号灯 <validity>属性为所关联道路所有车道'}}, 'needconfirm': False, 'caseFails': '0'}
    # case_data_object.init_edit_data(1)
    # print(case_data_object.get_new_edit_data({'yuanyinfenxi': '11233213123123213213'}))
    # ttrttttt = json.dumps(
    #     {'title': 'Temp：xxxx 错误 -1042', 'steps': '', 'comment': None, 'yuanyinfenxi': '11233213123123213213',
    #      'probability': '20%percent', 'source': 'customerFB', 'factoryIDrefer': '', 'customerIDrefer': '',
    #      'planresolve': 'resolution', 'Vresult': '', 'Discoverylink': '', 'product': 7, 'module': 0, 'plan': 0,
    #      'type': '', 'severity': 1, 'pri': 1, 'status': 'closed', 'subStatus': '6', 'assignedTo': 'closed',
    #      'deadline': '0000-00-00', 'feedbackBy': '', 'notifyEmail': '', 'os[]': 'others,Windows', 'browser[]': None,
    #      'identify': 0, 'keywords': '', 'contactListMenu': None, 'project': 8, 'execution': 0, 'story': 0, 'task': 0,
    #      'openedBuild': 'trunk,65,66', 'resolvedBy': 'admin', 'resolvedDate': '2022-05-13 08:21:36',
    #      'resolvedBuild': '29', 'resolution': 'fixed', 'duplicateBug': 0, 'closedBy': 'admin',
    #      'closedDate': '2022-06-01 09:03:23', 'testtask': 0, 'case': 0})
    # print(s)
    # print(case_data_object.default_edit_data)
    # print(case_data_object.get_new_edit_data({}))
    print(bug_data_object.get_data(bug_id=15652, action='edited', data_dict={'yuanyinfenxi': '231321'}))
