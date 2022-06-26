# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC Init
# MAGIC ==
# MAGIC 
# MAGIC ONLY RUN ONCE, OR IF YOU WANT TO WIPE THE SLATE AND START AGAIN

# COMMAND ----------

# MAGIC %run ./config

# COMMAND ----------

# Test S3 access works
dbutils.fs.ls(f"s3a://{sources_bucket_name}")
dbutils.fs.ls(f"s3a://{tables_bucket_name}")

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP SCHEMA IF EXISTS nhs_ae_attendance CASCADE;
# MAGIC CREATE SCHEMA nhs_ae_attendance;
# MAGIC USE nhs_ae_attendance;

# COMMAND ----------

try:
    dbutils.fs.unmount("/mnt/sources")
    dbutils.fs.unmount("/mnt/tables")
except:
    pass

dbutils.fs.mount("s3a://%s" % sources_bucket_name, "/mnt/sources")
dbutils.fs.mount("s3a://%s" % tables_bucket_name, "/mnt/tables")
