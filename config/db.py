from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+pymysql://root:Adriana5@localhost:3306/credito_cc')

meta = MetaData()

con = engine.connect()