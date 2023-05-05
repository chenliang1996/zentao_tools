# -*- coding: utf-8 -*-
# @Author chenliangliang
# @Time: 2023/5/5 14:03
# @File: download.py
# 1. 获取，解析汇总表
# 2. 查询数据库中，zt_action表
#     查询条件：
#         1. objectType = bug
#         2. objectID，product在目标项目下
#         3. actor!= admin
# 3.