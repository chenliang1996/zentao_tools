# -*- coding: utf-8 -*-
# @Author chenliangliang
# @Time: 2023/5/5 13:23
# @File: upload.py
# 1. 解析指定路径下是否存在待上传包
# 2. 解压缩上传包
# 3. 解析下载的Bug.json 遍历每个Bug信息。判断action
# 4. opened
#      按照项目，产品对应关系修改其中的值
# 5. 指派人：
#         判断指派人是否为指定人
#         不是:则走编辑接口
#         是: 则走指派人接口
# 6. 根据配置文件获取修改后的接口需要的data
#     6.1 注意：下载时，需要额外再备注字段头部新增  xxxx {action} {datetime}
# 7. 图片，附件的特殊处理！！
# 8. 调用对应的接口完成动作
# 9. 上传过程中，任何报错，记录改Bug_id 写入error.json中。
import datetime
import os.path

from commond.common import unzip_file
from commond.config import setting
from commond.logger import logger


class bug_upload:
    """
    禅道上传类，实现bug信息上传
    """

    def __init__(self):
        """
        初始化
        """
        self.upload_path = setting.yaml['upload']['path']
        today_file = os.path.join(self.upload_path, f'{str(datetime.date.today())}.zip')
        if not os.path.isfile(today_file):
            logger.error(f'{today_file} 没有找到')
            raise FileNotFoundError(f'{today_file} 没有找到')
        if not unzip_file(today_file, today_file.replace('.zip', '')):
            logger.error(f'{today_file} 解压失败')
            raise IOError(f'{today_file} 解压失败')



if __name__ == '__main__':
    upload = bug_upload()
