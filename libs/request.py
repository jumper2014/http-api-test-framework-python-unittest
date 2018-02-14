#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import requests


class Request(object):
    """
    仅支持json格式的body
    """
    def __init__(self, method, host, port, uri, headers, body):
        self.method = method
        self.url = "http://{0}:{1}{2}".format(host, port, uri)
        self.headers = headers
        self.body = body

    def send(self):
        # 让requests去处理json
        resp = requests.request(method=self.method, url=self.url, headers=self.headers, json=self.body)
        return resp


