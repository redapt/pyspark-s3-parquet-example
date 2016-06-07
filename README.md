# pyspark-s3-parquet-example
This repo demonstrates how to load a sample Parquet formatted file from an AWS S3 Bucket.  A python job will then be submitted to a local Apache Spark instance which will run a SQLContext to create a temporary table using a DataFrame.  SQL queries will then be possible against the temporary table.
