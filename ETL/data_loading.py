import os
os.environ['JAVA_HOME'] = '/Library/Java/JavaVirtualMachines/temurin-11.jdk/Contents/Home'
#os.environ['SPARK_HOME'] = '/Users/Marfa-Popova/data_eng_ind/spark-3.2.1-bin-hadoop3.2'
os.environ['SPARK_HOME'] = '/Users/MarfaPopova/S2R Analytics/Development & Support Team - Power BI for Synergy - Advanced Analytics\DataFlowExtract/venv/spark-3.2.1-bin-hadoop3.2'

import findspark
findspark.init('/Users/MarfaPopova/S2R Analytics/Development & Support Team - Power BI for Synergy - Advanced Analytics\DataFlowExtract/venv/spark-3.2.1-bin-hadoop3.2')
import pyspark
from pyspark.sql import SQLContext

sc = pyspark.SparkContext.getOrCreate()
sqlContext = SQLContext(sc)

projects = sqlContext.read.parquet('/Users/MarfaPopova/S2R Analytics/Development & Support Team - Power BI for Synergy - Advanced Analytics/DataFlowExtract/ETL/parquet-files/projects.parquet', header=True)
clients = sqlContext.read.parquet('/Users/MarfaPopova/S2R Analytics/Development & Support Team - Power BI for Synergy - Advanced Analytics/DataFlowExtract/ETL/parquet-files/clients.parquet', header=True)
stages = sqlContext.read.parquet('/Users/MarfaPopova/S2R Analytics/Development & Support Team - Power BI for Synergy - Advanced Analytics/DataFlowExtract/ETL/parquet-files/stages.parquet', header=True)
transactions = sqlContext.read.parquet('/Users/MarfaPopova/S2R Analytics/Development & Support Team - Power BI for Synergy - Advanced Analytics/DataFlowExtract/ETL/parquet-files/transactions.parquet', header=True)
staff = sqlContext.read.parquet('/Users/MarfaPopova/S2R Analytics/Development & Support Team - Power BI for Synergy - Advanced Analytics/DataFlowExtract/ETL/parquet-files/staff.parquet', header=True)

#postgres_uri = 'jdbc:postgresql://opensea.c5pkb2dzarva.us-west-2.rds.amazonaws.com:5432/opensea'
#user = 'marfapopova21'
#password = 'qwerty123'


# Connect to the existing database 'wga'
#import sqlite3
#conn = sqlite3.connect('wga.db')

# Connecting to a database created in MS SQL Server Management Studio
import pyodbc

server = '.\sqlexpress' 
database = 'wga' 
username = 'sa'  
password  = 'marfa'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
cursor = cnxn.cursor()

# Test query
sql_statement = 'select 1'
response = cursor.execute(sql_statement).fetchone()
print(response[0])

# Test how many tables there are in the database
sql_statement = 'select 1'
response = cursor.execute(sql_statement).fetchone()
print(response[0])

# Write data tables ino the database
staff.write \
    .format('jdbc') \
    .option('dbtable', 'wga.staff') \
    .mode('append') \
    .option('password', password) \
    .option('url', cnxn) \
    .option('user', username) \
    .save()

projects.write \
    .mode('append') \
    .format('jdbc') \
    .option('dbtable', 'wga.projects') \
    .option('url', cnxn) \
    .option('user', username) \
    .option('password', password) \
    .save()
    
stages.write \
    .mode('append') \
    .format('jdbc') \
    .option('dbtable', 'wga.stages') \
    .option('url', cnxn) \
    .option('password', password) \
    .option('user', username) \
    .save()

clients.write \
    .mode('append') \
    .format('jdbc') \
    .option('url', cnxn) \
    .option('user', username) \
    .option('dbtable', 'wga.clinets') \
    .option('password', password) \
    .save()

transactions.write \
    .format('jdbc') \
    .mode('append') \
    .option('url', cnxn) \
    .option('dbtable', 'wga.transactions') \
    .option('user', username) \
    .option('password', password) \
    .save()