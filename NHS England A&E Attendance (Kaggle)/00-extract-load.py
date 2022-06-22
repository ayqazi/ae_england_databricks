# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC Extract & Load
# MAGIC ==

# COMMAND ----------

# MAGIC %run ./lib/config

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC A&E Attendences in England
# MAGIC ==
# MAGIC 
# MAGIC Original location: https://www.kaggle.com/datasets/treich/ae-attendances-england
# MAGIC 
# MAGIC Context
# MAGIC --
# MAGIC 
# MAGIC The NHS England publishes data about Emergency Department attendances. These data used to be published weekly but since 2015 only monthly counts are available. This is an aggregated form of the currently available data resampled to monthly numbers. The original data can be found here.
# MAGIC To allow the geopspacial representation the coordinates for each hospital were added. For more details see this dataset
# MAGIC 
# MAGIC Content
# MAGIC --
# MAGIC 
# MAGIC The dataset contains the monthly numbers since 2010 of patients that attended the Emergency Departments in England (UK). The geographic locations were added.
# MAGIC 
# MAGIC Explanation of the data:
# MAGIC * Code and Name: are identifiers for the hospital
# MAGIC 
# MAGIC Attendance numbers:
# MAGIC * Type 1 Departments - Major A&E: Is the area of the Emergency department where the more serious patients go.
# MAGIC * Type 2 Departments - Single Specialty: These are speciality Emergency departments for example a Paediatric department.
# MAGIC * Type 3 Departments - Other A&E/Minor Injury Unit: Minor Injury Units are basically walk in clinics for minor ailments, fractures, rashes etc. These have more available resources than a Doctor's surgery but operate similarly in an ambulant fashion.
# MAGIC * Total attendances: The total of the above.
# MAGIC 
# MAGIC _4 hours to decision:_
# MAGIC 
# MAGIC This is the number of patients who left the Emergency Department within 4 hours of attending (4 Hours is a NHS target). This means they could be discharged, referred somewhere else or admitted to a ward.
# MAGIC 
# MAGIC _Emergency Admission:_
# MAGIC 
# MAGIC These are the number of people that were admitted to a ward from any of the Emergency Department types. Additionally there is the column: 'Other Emergency admissions (i.e not via A&E)' for patient how were admitted to from somewhere else. This could be a doctor's surgery for example.
# MAGIC 
# MAGIC _Long stays_
# MAGIC 
# MAGIC Some patients stay in the emergency department for a long time for different reasons. These figures are given in: Number of patients spending >12 hours from decision to admit to admission'. Again this is a target monitored by the NHS.

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC DROP TABLE IF EXISTS en_bronze_csv;
# MAGIC CREATE TABLE en_bronze_csv
# MAGIC   USING CSV
# MAGIC   OPTIONS (path '/mnt/sources/a&e-england/AE_attendances_england_monthly.csv', 'header' 'true', 'mode' 'FAILFAST');
# MAGIC 
# MAGIC -- SELECT * FROM en_bronze_csv;

# COMMAND ----------

dbutils.fs.rm("/mnt/sources/tables/ae_england/en_bronze.delta", recurse=True)

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC DROP TABLE IF EXISTS en_bronze;
# MAGIC CREATE TABLE en_bronze
# MAGIC   USING DELTA
# MAGIC   TBLPROPERTIES ("delta.columnMapping.mode" = "name")
# MAGIC   LOCATION '/mnt/sources/tables/ae_england/en_bronze.delta'
# MAGIC   AS SELECT * FROM en_bronze_csv;

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC SELECT * FROM en_bronze;
