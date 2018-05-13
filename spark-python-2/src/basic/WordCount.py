# -*- coding: utf-8 -*-

from pyspark import SparkConf
from pyspark import SparkContext

if __name__ == "__main__":
    sparkConf = SparkConf().setAppName("WordCount")
    sc = SparkContext(conf=sparkConf)
    localFile = sc.textFile("file:///opt/spark-2.3.0-bin-hadoop2.7/LICENSE")
    strRDD = localFile.flatMap(lambda line : line.split(" ")).map(lambda word : (word, 1)).reduceByKey(lambda x,y : x + y)
    print(strRDD.collect())
    