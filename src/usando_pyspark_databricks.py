# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, min, max, avg
import time

# Inicializar sessão Spark
spark = SparkSession.builder.appName('ProcessamentoSimples').getOrCreate()

dbfs_path = '/Volumes/workspace/default/etl_pipelines/meducies_1bilhao.txt'

# Inicializa contagem de tempo
start_time = time.time()

# Lendo csv com spark
df = spark.read.option('header', False).option('sep',';').csv(dbfs_path)

# Renomeando colunas do df
df = df.withColumnRenamed('_c0', 'station').withColumnRenamed('_c1', 'measure')

# Convertendo a coluna de meddia para float
df = df.withColumn('measure', df['measure'].cast('float'))

# Agregando os dados
aggregated_df = df.groupBy('station').agg(
    min('measure').alias('min'),
    max('measure').alias('max'),
    avg('measure').alias('mean')
)

# Exibindo o resultado:
aggregated_df.show()

# Calculando tempo decorrido
took = time.time() - start_time
print(f'Spark Took: {took:.2f} sec')