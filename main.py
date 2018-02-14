#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

from libs.header import Header
from libs.request import Request
import json

if __name__ == "__main__":
    header = Header()
    header.set_content_json()
    header.set_accept_json()
    body = {"name": "python", "name":11}
    req = Request('POST', '127.0.0.1', '8080', '/user', header.headers, body)
    resp = req.send()
    print(resp.status_code)
    print(json.loads(resp.content))