from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://mausolorio:ducinALTUM7!@localhost/doe',
                       echo=False)

print(engine.table_names())
