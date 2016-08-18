#!/usr/bin/python
# -*- coding: utf-8 -*-

import jieba.analyse

text = "李小福是创新办主任也是云计算方面的专家"

print("<<extract tags:>>")
extract_tags_0 = jieba.analyse.extract_tags(text, topK=10)
for ele in extract_tags_0:
    print(ele)
    
print("<<extract tags with weight:>>")
extract_tags_with_weight_0 = jieba.analyse.extract_tags(text, topK=10, withWeight=True)
for ele in extract_tags_with_weight_0:
    print(ele)
