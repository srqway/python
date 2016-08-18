#!/usr/bin/python
# -*- coding: utf-8 -*-

import jieba.posseg

text = "李小福是创新办主任也是云计算方面的专家"

print("<<cut:>>")
cut_0 = jieba.posseg.cut(text)
for ele in cut_0:
    print(ele)
    
print("<<cut without HMM:>>")
cut_without_hmm_0 = jieba.posseg.cut(text, HMM=False)
for ele in cut_without_hmm_0:
    print(ele)
    

