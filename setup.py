from setuptools import setup

setup(name='pyspark-s3-parquet-example',
      version='0.1',
      description='This app demonstrates how to load a sample Parquet formatted file from an AWS S3 Bucket. '
                  'A python job will then be submitted to a local Apache Spark instance which will run a SQLContext '
                  'to create a temporary table using a DataFrame. SQL queries will '
                  'then be possible against the temporary table.',
      url='https://github.com/redapt/pyspark-s3-parquet-example',
      author='Jonathan Dawson',
      author_email='jdawson@redapt.com',
      license='MIT',
      packages=['pyspark-s3-parquet-example'],
      zip_safe=False)
