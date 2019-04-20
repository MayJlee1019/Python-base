#!/usr/bin/env python   
# -*- coding:utf-8 -*- 
#@Time    :  8:09
#@Author  : Yun
#@File    : requests_test.py

import  requests
import  re
url = 'http://www.baidu.com'

response = requests.get(url)

print(response.content)

response.encoding = 'utf-8'
print(response.te6xt)