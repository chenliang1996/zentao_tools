# -*- coding: utf-8 -*-
# @Author yaochenghcheng
# @Time 2021年12月13日14:03:25
# @Description: 包含了一些简单的配置项，主要是框架的设置
#               调用方法 导入setting实例就可以使用


import logging
import os
import sys
from dataclasses import dataclass

import pandas
import yaml


@dataclass
class Log:
    # 默认log输出等级
    level: int = logging.DEBUG
    # log文件最大保存文件大小
    # 50M
    max_log_length: int = 5 * 10 * 1024 * 1024
    # 达到最大保存大小 自动备份数量
    backup_count: int = 5


# 返回yaml解析结果的类
class Yaml:
    # 解析yaml数据

    path = None
    data = None

    def __init__(self, path=None):
        Yaml.path = path
        self.data = self.__read_yaml()

    def __read_yaml(self):
        # yaml 格式读取 utf8 和 “ISO-8859-1”两种编码方式
        with open(self.path, "r", encoding="utf-8") as f:
            try:
                cfg = f.read()
            except:
                with open(self.path, "r", encoding="ISO-8859-1") as f:
                    cfg = f.read()
        return yaml.load(cfg, Loader=yaml.FullLoader)


# 解析所有路径相关的路径类
class Path:
    # 配置项config 路径
    config_path = os.path.abspath(os.path.dirname(__file__))
    # 项目根路径
    if hasattr(sys, 'frozen'):
        root_path = os.path.abspath(os.path.split(sys.executable)[0])
    else:
        root_path = os.path.abspath(config_path + os.sep + "..")

    # log根路径
    log_root_path = os.path.abspath(root_path + os.sep + "log")
    # 配置文件config路径
    config_file_path = os.path.abspath(root_path)
    # 测试用例根路径
    template_path = os.path.join(root_path, 'Template')

    result_path = os.path.join(root_path, 'Result')
    if not os.path.exists(result_path):
        os.makedirs(result_path)

    yamls_path = os.path.join(root_path, 'yamls')

    csvs_path = os.path.join(root_path, 'config_csv')


class config_csv:
    path = None
    data = None

    def __init__(self, path=None):
        config_csv.path = path
        self.data = self.__read_csv()

    def __read_csv(self):
        return pandas.read_csv(self.path)


# 所有设置的总类
class Setting:
    """
        使用方法： 导入 setting实例 setting.log  setting.yaml
                    返回为参数字典
    """

    @property
    def log(self):
        return Log

    @property
    def yaml(self):
        path = os.path.abspath(Path.config_file_path)
        return Yaml(path + "/setting.yaml").data

    @property
    def path(self):
        return Path


setting = Setting()
if __name__ == "__main__":
    print(os.path.dirname(__file__))
