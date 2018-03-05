#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


import unittest
from libs.const import *
from libs.header import Header
from libs.request import Request
from libs.database import delete_user


class TestUserCreate(unittest.TestCase):

    def setUp(self):
        delete_user(ADMIN_USER)

    def testUserCreate(self):
        header = Header()
        header.set_content_json()
        header.set_accept_json()
        body = {"name": ADMIN_USER, "age": ADMIN_AGE}
        req = Request(POST, api_server_host, api_server_port, '/user', header.headers, body)
        resp = req.send()
        self.assertEqual(resp.status_code, 200)

    def tearDown(self):
        delete_user(ADMIN_USER)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestUserCreate('testUserCreate'))
    runner = unittest.TextTestRunner()
    runner.run(suite)