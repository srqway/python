#!/usr/bin/python
# -*- coding: utf-8 -*-

import jieba

text = u"永和服装饰品有限公司"

print("<<tokenize:>>")
tokenize_0 = jieba.tokenize(text)
for ele in tokenize_0:
    print("%s %d %d" % (ele[0], ele[1], ele[2]))
    
print("<<tokenize(mode=search):>>")
tokenize_1 = jieba.tokenize(text, mode="search")
for ele in tokenize_1:
    print("%s %d %d" % (ele[0], ele[1], ele[2]))
    