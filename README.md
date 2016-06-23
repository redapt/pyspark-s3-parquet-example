# pyspark-s3-parquet-example
This repository demonstrates some of the mechanics necessary to load a sample [Parquet](https://parquet.apache.org/) formatted file from an AWS S3 Bucket.
A python job will then be submitted to a local [Apache Spark](http://spark.apache.org/) instance which will run a SQLContext to create a temporary table and load the Parquet file contents into a DataFrame.
SQL queries will then be possible against the in-memory temporary table.  SparkSQL has a lot to explore and this repo will serve as cool place to check things out.

The sample Parquet file was pulled from the [following repository](https://github.com/jcrobak/parquet-python/).  Thanks a bunch!

## Running the Examples

### AWS EMR using A Zeppelin Notebook

The [following script](./pyspark-scripts/nations-parquet-sql-aws-emr.py) can be copied and pasted inside a Zeppelin notebook running in AWS EMR.

#### Prerequisites

1. AWS Account created
2. AWS ACCESS key and SECRET ACCESS KEY stored in ~/.aws/credentials file
3. EMR Cluster Configured with Spark 1.6.1 and [Apache Zeppelin](http://docs.aws.amazon.com/ElasticMapReduce/latest/ReleaseGuide/emr-sandbox.html#emr-zeppelin)
4. Copy the [parquet file](./test-data/nation.plain.parquet) to a s3 bucket in your AWS account.

#### Steps

1. Configure the [Spark Interpreter](http://docs.aws.amazon.com/ElasticMapReduce/latest/ReleaseGuide/emr-sandbox.html#emr-zeppelin) in Zeppelin.
2. Copy the [script](./pyspark-scripts/nations-parquet-sql-aws-emr.py) into a new Zeppelin Notebook.
3. Run the script with the "arrow button".
4. Profit and play around with PySpark in the safety of the Zeppelin notebook.

#### Sample Output

The [following output](./sample-output/jon-sample-output.png) is from one of my sample runs ...

### Run against local instance of Spark

The [following-script](./pyspark-scripts/nations-parquet-sql-local.py) as been configured to run against a local instance of spark.  The location of the Parquet file is also being 
served locally rather than from s3.  Other than that the script is doing the same as the AWS script and the output will be the same.

#### Prerequisites

1. [Apache Spark 1.6.1](http://spark.apache.org/downloads.html) installed locally.
2. [Python 2.7.11](https://www.python.org/downloads/release/python-2711/)

#### Steps

1. From root cd into pyspark-scripts
2. Run the following
   python nations-parquet-sql-local.py
3. Once again profit and play around.
