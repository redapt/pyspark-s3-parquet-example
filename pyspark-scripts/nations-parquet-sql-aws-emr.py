%pyspark

"""
File name: nations-parquet-sql.py
Author: Jonathan Dawson
Date Created: 6/8/2016
Date Modified: 6/8/2016
Python Version: 2.7
PySpark Version: 1.6.1

Example of loading .parquet formatted files into a in-memory SQLContext table and running SQL queries against it.

This script is configured to run on the AWS EMR Spark service inside a Zeppelin notebook and pull a parquet file from
AWS s3.
"""

import sys

LINE_LENGTH = 200


def print_horizontal():
    """
    Simple method to print horizontal line
    :return: None
    """
    for i in range(LINE_LENGTH):
        sys.stdout.write('-')
    print("")


try:
    from pyspark import SparkContext
    from pyspark import SQLContext

    print ("Successfully imported Spark Modules -- `SparkContext, SQLContext`")
    print_horizontal()
except ImportError as e:
    print ("Can not import Spark Modules", e)
    sys.exit(1)

sqlContext = SQLContext(sparkContext=sc)

# Loads parquet file located in AWS S3 into RDD Data Frame
parquetFile = sqlContext.read.parquet("s3://jon-parquet-format/nation.plain.parquet")

# Stores the DataFrame into an "in-memory temporary table"
parquetFile.registerTempTable("parquetFile")

# Run standard SQL queries against temporary table
nations_all_sql = sqlContext.sql("SELECT * FROM parquetFile")

# Print the result set
nations_all = nations_all_sql.map(lambda p: "Country: {0:15} Ipsum Comment: {1}".format(p.name, p.comment_col))

print("All Nations and Comments -- `SELECT * FROM parquetFile`")
print_horizontal()
for nation in nations_all.collect():
    print(nation)

# Use standard SQL to filter
nations_filtered_sql = sqlContext.sql("SELECT name FROM parquetFile WHERE name LIKE '%UNITED%'")

# Print the result set
nations_filtered = nations_filtered_sql.map(lambda p: "Country: {0:20}".format(p.name))

print_horizontal()
print("Nations Filtered -- `SELECT name FROM parquetFile WHERE name LIKE '%UNITED%'`")
print_horizontal()
for nation in nations_filtered.collect():
    print(nation)
