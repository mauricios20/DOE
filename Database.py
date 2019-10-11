import glob
import os
import pandas as pd
from sqlalchemy import create_engine, Table, MetaData


# 'Iterate over all the files on CSV to create seperate dataframes'

os.chdir("/Users/mauri/github/DOE/CSV Files DOE")
globbed_files = glob.glob("*.csv")

Names = sorted({file[:-4] for file in globbed_files})
Frames = [pd.read_csv(file, encoding='latin1') for file in globbed_files]

# 'Create Database from list comprehension'

engine = create_engine('sqlite://', echo=False)


for x in range(10):
    Frames[x].to_sql(Names[x][2:], con=engine, if_exists='replace')

print(engine.table_names())
