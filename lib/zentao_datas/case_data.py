# -*- coding: utf-8 -*-
# @Author chenliangliang
# @Time: 2023/4/20 11:04
# @File: case_data.py
# @说明: 用来构建用例请求的data值

class RequestCaseData:
    def __init__(self):
        self.default_data = {
            "title": "",
            "precondition": "",
            "steps[1]": "",
            "stepType[1]": "step",
            "expects[1]": "",
            "CaseSource": "",
            "automatic": "",
            "script": "",
            "CaseSequence": "",
            "comment": "",
            "lib": "",
            "module": "",
            "type": "",
            "stage[]": "",
            "pri": "",
            "status": "",
            "keywords": "",
            "scriptroute": ""
        }

    def init_default_data(self, view_data):
        """
        传入通过view-case-id接口获取到的值
        :return:
        """
        for key, value in view_data.items():
            if key in self.default_data:
                self.default_data[key] = value
            elif key == 'steps':
                # steps = view_data['steps']
                steps_list = list(view_data['steps'].values())
                for i in range(len(steps_list)):
                    self.default_data[f'steps[{i + 1}]'] = steps_list[i]['desc']
                    self.default_data[f'stepType[{i + 1}]'] = 'step'
                    self.default_data[f'expects[{i + 1}]'] = steps_list[i]['expect']
            elif key == 'stage':
                self.default_data['stage[]'] = value

    def get_new_edit_data(self, edit_data: dict):
        """
        传入需要修改的值，生成可以直接用来传参的data
        :param edit_data: {'title':'1123'}
        :return:
        """
        for key in edit_data.keys():
            if key not in self.default_data.keys():
                raise ValueError(f"Key '{key}' is not in the default data!")
        self.default_data.update(edit_data)
        return self.default_data


if __name__ == '__main__':
    case_data_object = RequestCaseData()
    view_data = {'id': '26830', 'project': '0', 'product': '0', 'execution': '0', 'branch': '0', 'lib': '21',
                 'module': '0', 'path': '0', 'story': '0', 'storyVersion': '1',
                 'title': '交通信号灯validity属性为所关联道路所有车道2',
                 'precondition': '交通信号灯objid在EFD数据表efd_obj_road_connection中所关联道路的laneseq数值存在255情况+2',
                 'keywords': 'ZF', 'pri': '2', 'type': 'feature', 'auto': 'no', 'frame': '', 'stage': 'feature',
                 'howRun': '', 'script': '', 'scriptedBy': '', 'scriptedDate': '', 'scriptStatus': '',
                 'scriptLocation': '', 'status': 'normal', 'color': '', 'frequency': '1', 'order': '0',
                 'openedBy': 'admin', 'openedDate': '2022-10-14 09:24:41', 'reviewedBy': '', 'reviewedDate': '',
                 'lastEditedBy': 'admin', 'lastEditedDate': '2023-04-19 17:06:41', 'version': '12', 'linkCase': '',
                 'fromBug': '0', 'fromCaseID': '0', 'fromCaseVersion': '1', 'deleted': '0', 'lastRunner': '',
                 'lastRunDate': '', 'lastRunResult': '', 'execute': '', 'CaseSource': 'SW_Req', 'automatic': 'Yes',
                 'scriptroute': '', 'CaseSequence': '4444', 'subStatus': '', 'toBugs': [], 'files': [],
                 'currentVersion': '12', 'steps': {
            '361665': {'id': '361665', 'parent': '0', 'case': '26830', 'version': '12', 'type': 'step',
                       'desc': '使用OpenDRIVEEditor软件打开OD数据，在工具视图界面中显示信号灯分布+1',
                       'expect': '数据工具打开显示正常'},
            '361666': {'id': '361666', 'parent': '0', 'case': '26830', 'version': '12', 'type': 'step',
                       'desc': '以文本文档方式打开OD数据，查看交通信号灯<validity>属性',
                       'expect': '信号灯 <validity>属性为所关联道路所有车道'}}, 'needconfirm': False, 'caseFails': '0'}
    case_data_object.init_default_data(view_data)
    print(case_data_object.get_new_edit_data({}))
