#!/usr/bin/python
# -*- coding: utf-8 -*-

import jieba

text = "李小福是创新办主任也是云计算方面的专家"

print("<<enable_parallel:>>")
jieba.enable_parallel()
enable_parallel_0 = jieba.cut(text)
for ele in enable_parallel_0:
    print(ele)
    