import glob
import os
import pandas as pd
# import mysql.connector
from sqlalchemy import create_engine

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="ducinALTUM7!",
# )
#
# print(mydb)


# 'Iterate over all the files on CSV to create seperate dataframes'

os.chdir("/Users/mauri/github/DOE/CSV Files DOE")
globbed_files = glob.glob("*.csv")

Names = sorted({file[:-4] for file in globbed_files})
Frames = [pd.read_csv(file, encoding='latin1') for file in globbed_files]

# 'Create Database from list comprehension'

engine = create_engine('mysql+pymysql://mausolorio:ducinALTUM7!@localhost/doe')
for x in range(len(Names)):
    Frames[x].to_sql(Names[x][2:], con=engine, if_exists='replace')
