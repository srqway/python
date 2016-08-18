#!/usr/bin/python
# -*- coding: utf-8 -*-

import jieba

text = "李小福是创新办主任也是云计算方面的专家"

print("<<before add_word:>>")
before_add_word_0 = jieba.cut(text)
for ele in before_add_word_0:
    print(ele)

print("<<after add_word:>>")
jieba.add_word('创新办')
jieba.add_word('也是')
jieba.add_word('云计算')
after_add_word_0 = jieba.cut(text)
for ele in after_add_word_0:
    print(ele)
    
