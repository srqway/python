#!/usr/bin/python
# -*- coding: utf-8 -*-

import jieba

text = "李小福是创新办主任也是云计算方面的专家"

print("<<set dictionary:>>")
jieba.set_dictionary("../dict.txt.big");
set_dictionary_0 = jieba.cut(text)
for ele in set_dictionary_0:
    print(ele)
    

