#!/usr/bin/python
# -*- coding: utf-8 -*-

import jieba

text = "李小福是创新办主任也是云计算方面的专家"

print("<<before load_userdict:>>")
before_load_userdict_0 = jieba.cut(text)
for ele in before_load_userdict_0:
    print(ele)

print("<<after load_userdict:>>")
jieba.load_userdict("../load_userdict.txt")
after_load_userdict_0 = jieba.cut(text)
for ele in after_load_userdict_0:
    print(ele)
    
