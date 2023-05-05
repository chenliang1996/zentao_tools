# -*- coding: utf-8 -*-
# @Author chenliangliang
# @Time: 2021/11/29 14:17
import requests
import urllib


class RestClient:

    def __init__(self):
        """
        第一次实例化request模块事，先进行session的实例化以及请求方式的实例
        """
        # logger.getLogger("requests").setLevel(logger.ERROR)  # 用于去除requests的log
        self.MySessions = None
        self._sessions()

    def _sessions(self):
        self.MySessions = requests.session()
        self.METHODS = {
            "GET": self.MySessions.get,
            "POST": self.MySessions.post,
            "PUT": self.MySessions.put,
            "DELETE": self.MySessions.delete,
            "HEAD": self.MySessions.head,
            "PATCH": self.MySessions.patch,
        }

    def request(self, url, method, new=False, data=None, json=None, **kwargs):
        """
        封装request请求，使所有请求都通过session进行，当有新的session页面时，只需要传入new=True即可刷新session。
        刷新后的session会自动替换之前的session信息。
        :param url: 请求地址
        :param method: 请求方式。必须大写
        :param new: 是否刷新session
        :param data: data数据。默认为空
        :param json: json数据。默认为空
        :param kwargs: 缺省参数包含
                    params,headers,cookies,files,auth,timeout,
                    allow_redirects,proxies,hooks,stream,verify,cert
                    穿过伊桑的参数会报错。typeerror
        :return: response对象
        """
        self._sessions() if new else None
        method = method.upper()
        if method in ("GET", "DELETE", "HEAD"):
            return self.METHODS.get(method)(url, **kwargs)
        elif method == "POST":
            return self.METHODS.get(method)(url, data, json, **kwargs)
        else:
            return self.METHODS.get(method)(url, data, **kwargs)


