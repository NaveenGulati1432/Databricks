# Databricks notebook source
from pyspark.sql.session import SparkSession
spark = SparkSession.builder.appName("Spark DataFrames").getOrCreate()
spark.conf.set(
    "fs.azure.account.key.navyamitstg.dfs.core.windows.net",
    "W8OWj30RV0Qf4oUemVerefbSXZ8gyDNYe2G7VTm3cbzI3yaBAq7kj5fhObsx5Glb+R1b/NoJNTP3+AStpyDgxQ=="
)

n_df = spark.read.format("csv").option('header', 'true').option('inferSchema', 'true').load("abfss://input@navyamitstg.dfs.core.windows.net/demotest.csv")
display(df)



# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE CATALOG my_catalog;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC -- SHOW CATALOGS
# MAGIC --CREATE CATALOG product_catalog COMMENT "Catalog for my Databricks project";
# MAGIC CREATE DATABASE IF NOT EXISTS product_db;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW DATABASES

# COMMAND ----------

df = df.select("Product_ID","Product_Name")
df.write.format("delta") \
  .mode("overwrite") \
  .saveAsTable("product_db.product_data")


# COMMAND ----------

# MAGIC %sql
# MAGIC use product_db;
# MAGIC Select * from product_data;

# COMMAND ----------

# Example update or insert
# df_new = n_df.select("Product_ID","Product_Name","Category")
# df_new.write.format("delta").mode("append").option("mergeSchema","true").saveAsTable("product_db.product_data")



# -- ALTER TABLE product_data SET TBLPROPERTIES (delta.enableChangeDataFeed = true);



# COMMAND ----------

# MAGIC %sql
# MAGIC -- SELECT * FROM table_changes('product_data', '2025-04-10 07:06:54.0', '2025-04-10 07:06:54.0');
# MAGIC
# MAGIC DESCRIBE TABLE EXTENDED product_data
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM table_changes('product_data', 3, 4);
# MAGIC

# COMMAND ----------

