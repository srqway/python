#!/usr/bin/python
# -*- coding: utf-8 -*-

import jieba.analyse

text = "李小福是创新办主任也是云计算方面的专家"

print("<<textrank:>>")
textrank_0 = jieba.analyse.textrank(text)
for ele in textrank_0:
    print(ele)
    
print("<<textrank with weight:>>")
textrank_with_weight_0 = jieba.analyse.textrank(text, withWeight=True)
for ele in textrank_with_weight_0:
    print(ele)
