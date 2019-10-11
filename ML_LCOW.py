from sqlalchemy import create_engine
engine = create_engine(r'sqlite:///C:\Users\mauri\github\DOE\DOE.db',
                       echo=False)

print(engine.table_names())
