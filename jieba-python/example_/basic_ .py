#!/usr/bin/python
# -*- coding: utf-8 -*-

import jieba

print("<<default mode(return generator):>>")
default_mode_0 = jieba.cut("我来到北京清华大学", cut_all=False)
for ele in default_mode_0:
    print(ele)

print("<<full mode(return generator):>>")
full_mode_0 = jieba.cut("我来到北京清华大学", cut_all=True)      
for ele in full_mode_0:
    print(ele)

print("<<search engine mode(return generator):>>")
search_engine_mode_0 = jieba.cut_for_search("我来到北京清华大学")
for ele in search_engine_mode_0:
    print(ele)

print("<<default mode(return list):>>")
default_mode_1 = jieba.lcut("我来到北京清华大学", cut_all=False)
for ele in default_mode_1:
    print(ele)

print("<<full mode(return list):>>")
full_mode_1 = jieba.lcut("我来到北京清华大学", cut_all=True)      
for ele in full_mode_1:
    print(ele)

print("<<search engine mode(return list):>>")
search_engine_mode_1 = jieba.lcut_for_search("我来到北京清华大学")
for ele in search_engine_mode_1:
    print(ele)

