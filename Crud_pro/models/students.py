from sqlalchemy import create_engine,MetaData
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String

engine=create_engine('mysql+pymysql://root:MayurT24#@localhost:3306/py_crud')
con=engine.connect()
meta= MetaData()
students=Table(
    'students',meta,
    Column('id',Integer,primary_key=True),
    Column('name',String(255)),
    Column('email',String(255)),
    Column('age',String(255)),
    Column('country',String(255)),
)
meta.create_all(engine)