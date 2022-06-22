# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC Transform
# MAGIC ==

# COMMAND ----------

# MAGIC %run ./lib/config

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC SELECT * FROM en_bronze;

# COMMAND ----------

dbutils.fs.rm("/mnt/sources/tables/ae_england/en_silver.delta", recurse=True)

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC DROP TABLE IF EXISTS en_silver;
# MAGIC CREATE TABLE en_silver
# MAGIC   USING DELTA
# MAGIC   TBLPROPERTIES ("delta.columnMapping.mode" = "name")
# MAGIC   LOCATION '/mnt/sources/tables/ae_england/en_silver.delta'
# MAGIC   AS SELECT
# MAGIC     cast(_c0 AS INT) AS row_index,
# MAGIC     cast(`date` AS DATE) AS recorded_date,
# MAGIC     Name AS hospital_name,
# MAGIC     `Type 1 Departments - Major A&E` AS major_ae_count_orig,
# MAGIC     cast(`Type 1 Departments - Major A&E` AS INT) AS major_ae_count
# MAGIC     
# MAGIC     FROM en_bronze;

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC ALTER TABLE en_silver
# MAGIC   ALTER row_index SET NOT NULL;

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC DESCRIBE TABLE en_silver;

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC SELECT hospital_name, SUM(major_ae_count) FROM en_silver GROUP BY hospital_name;
