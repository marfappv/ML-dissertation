!pip install findspark

import os
os.environ["JAVA_HOME"] = "/Library/Java/JavaVirtualMachines/temurin-11.jdk/Contents/Home"
os.environ["SPARK_HOME"] = "/Users/Marfa-Popova/data_eng_ind/spark-3.2.1-bin-hadoop3.2"

import findspark
findspark.init("/Users/Marfa-Popova/data_eng_ind/spark-3.2.1-bin-hadoop3.2")
import pyspark
from pyspark.sql import SQLContext

sc = pyspark.SparkContext.getOrCreate()
sqlContext = SQLContext(sc)

assets_showroom = sqlContext.read.parquet("s3a://data-eng-ind/parquet-files/showroom.parquet", header=True)
assets_API = sqlContext.read.parquet("s3a://data-eng-ind/parquet-files/assets_API.parquet", header=True)
assets_ws = sqlContext.read.parquet("s3a://data-eng-ind/parquet-files/opensea_ws.parquet", header=True)
collections = sqlContext.read.parquet("s3a://data-eng-ind/parquet-files/collections_API.parquet", header=True)
finances = sqlContext.read.parquet("s3a://data-eng-ind/parquet-files/finances_API.parquet", header=True)
socials = sqlContext.read.parquet("s3a://data-eng-ind/parquet-files/socials_API.parquet", header=True)
urls = sqlContext.read.parquet("s3a://data-eng-ind/parquet-files/urls_API.parquet", header=True)

postgres_uri = "jdbc:postgresql://opensea.c5pkb2dzarva.us-west-2.rds.amazonaws.com:5432/opensea"
user = "marfapopova21"
password = "qwerty123"

assets_showroom.write \
    .mode("append") \
    .format("jdbc") \
    .option("dbtable", "nfts.assets") \
    .option("url", postgres_uri) \
    .option("user", user) \
    .option("password", password) \
    .option("driver", "org.postgresql.Driver") \
    .save()

assets_API.write \
    .mode("append") \
    .format("jdbc") \
    .option("url", postgres_uri) \
    .option("user", user) \
    .option("dbtable", "nfts.assets") \
    .option("password", password) \
    .option("driver", "org.postgresql.Driver") \
    .save()

assets_ws.write \
    .mode("append") \
    .format("jdbc") \
    .option("dbtable", "nfts.assets") \
    .option("url", postgres_uri) \
    .option("password", password) \
    .option("user", user) \
    .option("driver", "org.postgresql.Driver") \
    .save()

collections.write \
    .format("jdbc") \
    .mode("append") \
    .option("url", postgres_uri) \
    .option("dbtable", "nfts.collections") \
    .option("user", user) \
    .option("password", password) \
    .option("driver", "org.postgresql.Driver") \
    .save()

finances.write \
    .format("jdbc") \
    .option("dbtable", "nfts.finances") \
    .mode("append") \
    .option("password", password) \
    .option("url", postgres_uri) \
    .option("user", user) \
    .option("driver", "org.postgresql.Driver") \
    .save()

socials.write \
    .format("jdbc") \
    .mode("append") \
    .option("url", postgres_uri) \
    .option("user", user) \
    .option("dbtable", "nfts.socials") \
    .option("driver", "org.postgresql.Driver") \
    .option("password", password) \
    .save()

urls.write \
    .format("jdbc") \
    .mode("append") \
    .option("dbtable", "nfts.urls") \
    .option("url", postgres_uri) \
    .option("user", user) \
    .option("password", password) \
    .option("driver", "org.postgresql.Driver") \
    .save()


# Create a database and connect to it
conn = sqlite3.connect('WGA.db')

# Connecting to a database created in MS SQL Server Management Studio
import pyodbc

server = '.\sqlexpress' 
database = 'wga' 
username = 'sa'  
password  = 'marfa'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
cursor = cnxn.cursor()

# Test query
sql_statement = "select 1"
response = cursor.execute(sql_statement).fetchone()
print(response[0])
