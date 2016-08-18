#!/usr/bin/python
# -*- coding: utf-8 -*-

import jieba

text = "如果放到post中将出错"

print("<<before suggest_freq:>>")
before_suggest_freq_0 = jieba.cut(text, HMM=False)
for ele in before_suggest_freq_0:
    print(ele)

print("<<after suggest_freq:>>")
jieba.suggest_freq(('中', '将'), True)
after_suggest_freq_0 = jieba.cut(text, HMM=False)
for ele in after_suggest_freq_0:
    print(ele)
