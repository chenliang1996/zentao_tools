# -*- coding: utf-8 -*-
# @Author chenliangliang
# @Time: 2022/12/7 9:20
# @update： 2022年12月7日
#           by: chenliangliang
#           function：修改log路径，修改log格式，修改log名字,修改终端输出颜色


import logging
import logging.handlers
import os
import sys
import time
# 读取setting里面的log路径名
import colorlog

from commond.common import create_folder
from commond.config import setting

log_colors_config = {
    'DEBUG': 'white',  # cyan white
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red',
}

class Logger:

    def __init__(self):
        LOG_PATH = setting.path.log_root_path
        # 如果文件不存在，则创建文件夹
        create_folder(LOG_PATH)
        self.logname = os.path.join(LOG_PATH, "{}.log".format(time.strftime("%H_%M")))
        self.logger = logging.getLogger("log")
        self.logger.setLevel(setting.yaml['Parameter']['log_cli_level'])

        # self.formater = logging.Formatter(
        #     '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]:<%(module)s %(funcName)s > %(message)s')
        # self.formater = logging.Formatter(
        #     '[%(asctime)s]%(message)s')
        console_formatter = colorlog.ColoredFormatter(
            # fmt='%(log_color)s[%(asctime)s.%(msecs)03d] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s',
            datefmt='%Y-%m-%d  %H:%M:%S',
            log_colors=log_colors_config
        )
        self.file_hander = logging.handlers.RotatingFileHandler(self.logname, mode="w",
                                                                maxBytes=setting.log.max_log_length,
                                                                backupCount=setting.log.backup_count, encoding="UTF-8")

        self.console = logging.StreamHandler(sys.stdout)

        self.console.setLevel(setting.yaml['Parameter']['log_cli_level'])
        self.file_hander.setLevel(setting.yaml['Parameter']['log_cli_level'])
        self.file_hander.setFormatter(console_formatter)
        self.console.setFormatter(console_formatter)
        self.logger.addHandler(self.console)
        self.logger.addHandler(self.file_hander)

    def getstr(self, meg):
        filename = sys._getframe(2).f_code.co_filename.split(os.sep)[-1]
        # func_name = sys._getframe(2).f_code.co_name
        level = sys._getframe(1).f_code.co_name
        func_line = sys._getframe(2).f_lineno
        message = ",".join([str(i) for i in meg])
        asctime = time.strftime("%Y-%m-%d %H:%M:%S")
        # return "["+ filename +" "+ func_name+" "+ str(func_line) +"]"+ "["+ level +"]: "+message
        return "[" + asctime + " " + filename + " " + str(func_line) + "]" + "[" + level + "]: " + message
        # return message

    def info(self, *args):
        self.logger.info(self.getstr(args))

    def error(self, *args):
        self.logger.error(self.getstr(args))

    def debug(self, *args):
        self.logger.debug(self.getstr(args))

    def warning(self, *args):
        self.logger.warning(self.getstr(args))


logger = Logger()


def func_log(fn):
    from functools import wraps
    import inspect
    @wraps(fn)
    def wrapper(*args, **kwargs):
        logger.info("开始执行方法 : %s" % fn.__name__)

        logger.info("方法参数如下 : " + str(args) + str(kwargs))

        logger.info("执行信息 : " + str(inspect.stack()[1]))

        out = fn(*args, **kwargs)

        logger.info("方法执行结束 : %s" % fn.__name__)
        return out

    return wrapper


if __name__ == '__main__':
    logger.info("---测试开始---", 1232, [222])
    logger.debug("---测试结束---", "wewe", "eecwef")
