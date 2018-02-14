#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


class Header(object):
    def __init__(self):
        self.headers = dict()

    def set_accept_json(self):
        self.headers.update({"Accept": "Application/json"})

    def set_content_json(self):
        self.headers.update({"Content-Type": "Application/json"})

    def show(self):
        for k, v in self.headers.items():
            print(k, v)

if __name__ == "__main__":
    header = Header()
    header.set_accept_json()
    header.set_content_json()
    header.show()
