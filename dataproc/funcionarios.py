from pyspark.sql import SparkSession
import pandas

spark = SparkSession.builder.appName("Test").getOrCreate()

funcionarios = spark.read.csv("gs://database_cloud_engineer2_seu_nome/exports/export_usuarios.csv")
column_list = ['id','nome','departamento','salario','email','senha','cadastro']
funcionarios = funcionarios.toDF(*column_list)

funcionarios.createOrReplaceTempView("funcionarios")

sqlSALARIOS = spark.sql("SELECT * FROM funcionarios WHERE Salario > 5000").write.mode('Overwrite').csv('gs://dataproc_funcionarios_pyspark_seu_nome/output_csv')

sqlSALARIOS = spark.sql("SELECT * FROM funcionarios WHERE Salario > 5000").write.mode('Overwrite').json('gs://dataproc_funcionarios_pyspark_seu_nome/output_json')
