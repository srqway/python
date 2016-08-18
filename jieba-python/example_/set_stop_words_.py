#!/usr/bin/python
# -*- coding: utf-8 -*-

import jieba.analyse

text = "李小福是创新办主任也是云计算方面的专家"

print("<<set stop words:>>")
jieba.analyse.set_stop_words("../set_stop_words.txt");
set_idf_path_0 = jieba.analyse.extract_tags(text, topK=10)
for ele in set_idf_path_0:
    print(ele)
    

