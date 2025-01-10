import mysql
import mysql.connector
from google.cloud import bigquery
import os
import pandas as pd
conn_to_mysql = mysql.connector.connect(read_default_file="/Users/Maryam/.my.cnf")
client = bigquery.Client(project='etl-process-446323')

our_path = os.getcwd()
file = 'species.csv'
file_path = os.path.join(our_path,'data_files', file)
print(file_path)

target_table = 'etl-process-446323.etl.species'
job_config = bigquery.LoadJobConfig(
    skip_leading_rows=1,
    source_format=bigquery.SourceFormat.CSV,
    autodetect=True,
    write_disposition = 'WRITE_TRUNCATE',
)

sql = "select * from species"
df = pd.read_sql(sql, con=conn_to_mysql)
df.to_csv(file_path)


with open(file_path, 'rb') as source_file:
    load_job = client.load_table_from_file(
        source_file,
        target_table,
        job_config=job_config,
    )
load_job.result()

destination_table = client.get_table(target_table)
print(f"you have {destination_table.num_rows} rows in your table")