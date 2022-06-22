# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC Extract & Load Python-only
# MAGIC ==

# COMMAND ----------

# MAGIC %run ./lib/config

# COMMAND ----------

en_bronze_csv = spark.read.format("csv").option("header", True).load(england_file)

# COMMAND ----------

display(en_bronze_csv)

# COMMAND ----------

save_path = tables_path + "/en_bronze.delta"
dbutils.fs.rm(save_path, recurse=True)
spark.sql("DROP TABLE IF EXISTS en_bronze")
en_bronze_csv.write.format("delta").option("delta.columnMapping.mode", "name").option("path", save_path).saveAsTable("en_bronze")
en_bronze = spark.read.format("delta").load(save_path)
display(en_bronze)
