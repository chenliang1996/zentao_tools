# -*- coding: utf-8 -*-
# @Author chenliangliang
# @Time: 2022/12/6 18:59
import zipfile
from datetime import timedelta, date
import os

from commond.logger import logger


def create_folder(folder_name):
    """
    用来创建folder_name的文件夹 不存在则创建 可创建多层嵌套文件夹
    :param folder_name: 为绝对路径
    :return:
    """
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def get_date():
    """
    获取上周四到当天的时间范围
    """
    today = date.today()
    last_thursday = today - timedelta(days=(today.weekday() - 3) % 7)
    return last_thursday, today


def check_key_in_dict(data_value, data_dict):
    """
    确认data_value中的key是否存在与data_dict，若不存在。返回False,存在，返回update后的data_dict
    :param data_value: 需要更新的值
    :param data_dict: 字典全集
    :return:
    """
    for key in data_value.keys():
        if key not in data_dict:
            return False
    data_dict.update(data_value)
    return data_dict


def unzip_file(zip_src, dst_dir):
    """
    解压ZIP文件
    :param zip_src: zip文件路径
    :param dst_dir: 解压到的目标文件夹
    :return:
    """
    r = zipfile.is_zipfile(zip_src)
    if r:
        fz = zipfile.ZipFile(zip_src)
        for file in fz.namelist():
            fz.extract(file, dst_dir)
    else:
        logger.debug("zip文件路径错误！")
        return False


if __name__ == '__main__':
    print(get_date())
