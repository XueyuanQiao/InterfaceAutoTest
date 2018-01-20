#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Qiaoxueyuan
@time: 2017/10/16 13:52
'''

import unittest
import ddt
import requests
import json
from interface_test.get_data.get_ivrdata import ExcelUtil

excel = ExcelUtil("C:\\Users\\Qiao\\PycharmProjects\\interface_test\\data\\data.xlsx", "ivrdata")


@ddt.ddt
class IVRTest(unittest.TestCase):
    def setUp(self):
        self.static_url = "http://example/static_web_api_demo"
        self.dynamic_url = "http://example/dynamic_web_api_demo"

    @ddt.data(*excel.next())
    def test_ivr(self, data):
        # Dynamic
        dy_a = data["a"]
        dy_b = data["b"]
        call_id = data["call_id"]
        dy_body = {
            "data":
                {
                    "a": dy_a,
                    "b": dy_b,
                    "udesk_call_id": call_id
                },
        }
        respond = json.loads(requests.post(self.dynamic_url, json=dy_body).text)
        print("Dynamic:   ", respond)
        self.assertEqual(len(respond), 1, "【dynamic】接受json结构不匹配，接收结果为%s" % str(respond))
        self.assertEqual(len(respond["data"]), 3, "【dynamic】接受json结构不匹配，接收结果为%s" % str(respond))
        self.assertEqual(respond["data"]["received_a"], dy_a, "【dynamic】接受received_a值不匹配，接收结果为%s" % str(respond))
        self.assertEqual(respond["data"]["received_b"], dy_b, "【dynamic】接受received_b值不匹配，接收结果为%s" % str(respond))
        self.assertEqual(respond["data"]["call_id"], call_id, "【dynamic】接受call_id值不匹配，接收结果为%s" % str(respond))

        # Static
        st_a = data["a"]
        st_b = data["b"]
        st_body = {
            "a": st_a,
            "b": st_b
        }
        respond = json.loads(requests.post(self.static_url, st_body).text)
        print("Static:   ", respond)
        self.assertEqual(len(respond), 1, "【static】接受json结构不匹配，接收结果为%s" % str(respond))
        self.assertEqual(len(respond["data"]), 2, "【static】接受json结构不匹配，接收结果为%s" % str(respond))
        self.assertEqual(respond["data"]["code"], 1, "【static】接受code值不匹配，接收结果为%s" % str(respond))
        self.assertEqual(respond["data"]["is_created"], False, "【static】接受is_created值不匹配，接收结果为%s" % str(respond))

    def tearDown(self):
        print("\t")


if __name__ == "__main__":
    suite = unittest.TestSuite(unittest.TestLoader().loadTestsFromTestCase(IVRTest))
    unittest.TextTestRunner(verbosity=1).run(suite)
