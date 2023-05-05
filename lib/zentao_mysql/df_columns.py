# -*- coding: utf-8 -*-
# @Author chenliangliang
# @Time: 2022/12/22 15:26
BUG_COLUMNS = {'id': 'Bug编号',
               'project': '所属项目',
               'product': '所属产品',
               'injection': '注入阶段',
               'identify': '环节',
               'branch': '分支/平台',
               'module': '所属模块',
               'execution': '所属执行',
               'plan': '所属计划',
               'story': '相关需求',
               'storyVersion': '研发需求版本',
               'task': '相关任务',
               'toTask': '转任务',
               'toStory': '转研发需求',
               'title': 'Bug标题',
               'keywords': '关键词',
               'severity': '严重程度',
               'pri': '优先级',
               'type': 'Bug类型',
               'os': '操作系统',
               'browser': '浏览器',
               'hardware': '硬件',
               'found': '发现者',
               'steps': '重现步骤',
               'status': 'Bug状态',
               'color': '标题颜色',
               'confirmed': '是否确认',
               'activatedCount': '激活次数',
               'activatedDate': '激活日期',
               'feedbackBy': '反馈者',
               'notifyEmail': '通知邮箱',
               'mailto': '抄送给',
               'openedBy': '由谁创建',
               'openedDate': '创建日期',
               'openedBuild': '影响版本',
               'assignedTo': '指派给',
               'assignedDate': '指派日期',
               'deadline': '截止日期',
               'resolvedBy': '解决者',
               'resolution': '解决方案',
               'resolvedBuild': '解决版本',
               'resolvedDate': '解决日期',
               'closedBy': '由谁关闭',
               'closedDate': '关闭日期',
               'duplicateBug': '重复Bug',
               'linkBug': '相关Bug',
               'case': '相关用例',
               'caseVersion': '用例版本',
               'feedback': '反馈',
               'result': '结果',
               'repo': '所属版本库',
               'mr': '合并请求',
               'entry': '代码路径',
               'lines': '代码行',
               'v1': '版本1',
               'v2': '版本2',
               'repoType': '版本库类型',
               'issueKey': 'Sonarqube问题键值',
               'testtask': '测试单',
               'lastEditedBy': '最后修改者',
               'lastEditedDate': '修改日期',
               'deleted': '已删除',
               'source': '问题来源',
               'factoryIDrefer': '关联生产ID',
               'customerIDrefer': '关联客户ID',
               'yuanyinfenxi': '问题原因分析及对策',
               'probability': '问题发生概率',
               'planresolve': '计划解决版本',
               'subStatus': '子状态',
               'introducer': '提出人',
               'Vresult': '验证结果',
               'Discoverylink': '发现环节'
               }
TASK_COLUMNS = {'id': '编号',
                'project': '所属项目',
                'product': '所属产品',
                'parent': '父任务',
                'execution': '所属执行',
                'module': '所属模块',
                'design': '相关设计',
                'story': '相关研发需求',
                'storyVersion': '研发需求版本',
                'designVersion': '设计版本',
                'fromBug': '来源Bug',
                'feedback': '反馈',
                'name': '任务名称',
                'type': '任务类型',
                'mode': '任务模式',
                'pri': '优先级',
                'estimate': '最初预计',
                'consumed': '总计消耗',
                'left': '预计剩余',
                'deadline': '截止日期',
                'status': '任务状态',
                'subStatus': '子状态',
                'color': '标题颜色',
                'mailto': '抄送给',
                'desc': '任务描述',
                'version': '版本',
                'openedBy': '由谁创建',
                'openedDate': '创建日期',
                'assignedTo': '指派给',
                'assignedDate': '指派日期',
                'estStarted': '预计开始',
                'realStarted': '实际开始',
                'finishedBy': '完成者',
                'finishedDate': '实际完成',
                'finishedList': '完成者列表',
                'canceledBy': '由谁取消',
                'canceledDate': '取消时间',
                'closedBy': '由谁关闭',
                'closedDate': '关闭时间',
                'planDuration': '计划持续天数',
                'realDuration': '实际持续天数',
                'closedReason': '关闭原因',
                'lastEditedBy': '最后修改',
                'lastEditedDate': '最后修改日期',
                'activatedDate': '激活日期',
                'repo': '所属版本库',
                'mr': '合并请求',
                'entry': '代码路径',
                'deleted': '已删除',
                'vision': '所属界面',
                }

BYDESING = {
    None: '',
    'bydesign': '设计如此',
    'duplicate': '重复Bug',
    'external': '外部原因',
    'fixed': '已解决',
    'notrepro': '无法重现',
    'willnotfix': '不予解决',
    'tostory': '转为研发需求',
}

SOURCE = {"internalFB": "内部反馈",
          "UT": "单元测试",
          "factoryFB": "生产反馈",
          "customerFB": "外部客户反馈",
          "IT": "集成测试",
          "SYST": "系统测试",
          "RandomT": "随机测试",
          "vehicleT": "实车测试", }

BUG_STATUS = {'active': '激活',
              'resolved': '已处理',
              'closed': '已关闭',
              }

TASK_STATUS = {
    None: '',
    'wait': '未开始',
    'doing': '进行中',
    'done': '已完成',
    'pause': '已暂停',
    'cancel': '已取消',
    'closed': '已关闭',
}

BUG_PRI = {0: 'P0',
           1: 'P1',
           2: 'P2',
           3: 'P3',
           4: 'P4',
           }

BUG_SEVERITY = {0: '0',
                1: 'A',
                2: 'B',
                3: 'C',
                4: 'D',
                5: 'S'
                }

USER_COLUMNS = {'字段': '描述',
                'id': '用户编号',
                'company': '所属公司',
                'type': '用户类型',
                'dept': '部门',
                'account': '用户名',
                'password': '密码',
                'role': '职位',
                'realname': '姓名',
                'pinyin': '',
                'nickname': '昵称',
                'commiter': '源代码帐号',
                'avatar': '用户头像',
                'birthday': '生日',
                'gender': '性别',
                'email': '邮箱',
                'skype': 'Skype',
                'qq': 'QQ',
                'mobile': '手机',
                'phone': '电话',
                'weixin': '微信',
                'dingding': '钉钉',
                'slack': 'Slack',
                'whatsapp': 'WhatsApp',
                'address': '通讯地址',
                'zipcode': '邮编',
                'nature': '性格特征',
                'analysis': '影响分析',
                'strategy': '应对策略',
                'join': '入职日期',
                'visits': '访问次数',
                'visions': '界面类型',
                'ip': '最后IP',
                'last': '最后登录',
                'fails': '失败次数',
                'locked': '锁住日期',
                'feedback': '',
                'ranzhi': 'ZDOO帐号',
                'ldap': '',
                'score': '积分',
                'scoreLevel': '积分等级',
                'resetToken': '',
                'deleted': '(已删除)',
                'clientStatus': '登录状态',
                'clientLang': '客户端语言',
                }

STORY_STATUS = {
    None: "",
    'draft': '草稿',
    'reviewing': '评审中',
    'active': '激活',
    'closed': '已关闭',
    'changing': '变更中',
}

STORY_PRI = {0: 'P0',
             '0': 'P0',
             '1': 'P1',
             '2': 'P2',
             '3': 'P3',
             '4': 'P4',
             }

STORY_STAGE = {
    None: "",
    'wait': '未开始',
    'planned': '已计划',
    'projected': '已立项',
    'developing': '研发中',
    'developed': '研发完毕',
    'testing': '测试中',
    'tested': '测试完毕',
    'verified': '已验收',
    'released': '已发布',
    'closed': '已关闭',
}

BUG_TYPE = {
    'NULL': '',
    'ReqError': '需求问题',
    'DesignError': '设计问题',
    'codeerror': '编码问题',
    'IntegrationError': '集成问题',
    'config': '配置问题',
    'standard': '标准问题',
    'MakeError': '制作问题',
    'TestError': '测试问题',
    'OutsideError': '外部问题',
    'UI': 'UI 界面问题',
    'Match': '现势性问题',
    'others': '其他问题',
}

BUG_Discoverylink = {
    'CustomerUse': '用户使用',
    'AcceptanceTest': '验收测试',
    'ReviewDesign': '评审&设计',
    'IntegrationTesting': '集成测试',
    'SystemTesting': '系统测试',
    'RandomTest': '随机测试',
    'UnitTest': '单元测试',
}