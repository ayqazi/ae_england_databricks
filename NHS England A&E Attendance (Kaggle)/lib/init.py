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

# MAGIC %sql
# MAGIC DROP SCHEMA IF EXISTS ae_england CASCADE;
# MAGIC CREATE SCHEMA ae_england;
# MAGIC USE ae_england;

# COMMAND ----------

dbutils.fs.unmount(mount_path)
dbutils.fs.mount("s3a://%s" % aws_bucket_name, mount_path)
dbutils.fs.ls(england_file)
