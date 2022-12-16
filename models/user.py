from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Float, Date, Boolean
from config.db import meta, engine

users = Table('users',meta,Column('id', Integer, primary_key=True),
    Column('primer_nombre', String(255)),
    Column('apellido_paterno', String(255)),
    Column('apellido_materno', String(255)),
    Column('fecha_de_nacimiento', Date),
    Column('RFC', String(255)),
    Column('ingresos_mensuales', Float),
    Column('numero_dependientes_economicos', Integer),
    Column('APROBADO', Boolean)
    )

meta.create_all(engine)


