from fastapi import APIRouter
from config.db import con
from models.user import users 
from schemas.user import User, UserOut
from unidecode import unidecode
from datetime import datetime

user = APIRouter()

@user.get('/users')
def get_users():
    return con.execute(users.select()).fetchall()

@user.post('/users', response_model=UserOut)
def create_user(user:User):

    aprobado = valida_credito(user.ingresos_mensuales, user.numero_dependientes_economicos)

    nombre = user.primer_nombre
    paterno = user.apellido_paterno
    materno = user.apellido_materno
    fecha = user.fecha_de_nacimiento

    rfc_final = creaRFC(nombre, paterno, materno, fecha)    
    
    new_user = {'primer_nombre': user.primer_nombre, 'apellido_paterno': user.apellido_paterno,
                'apellido_materno': user.apellido_materno, 'fecha_de_nacimiento': user.fecha_de_nacimiento,
                'RFC': rfc_final, 'ingresos_mensuales': user.ingresos_mensuales, 
                'numero_dependientes_economicos': user.numero_dependientes_economicos, 'APROBADO': aprobado}

    result = con.execute(users.insert().values(new_user))    
    return con.execute(users.select().where(users.c.id == result.lastrowid)).first()


def creaRFC(nombre, ap_paterno, ap_materno, fecha_nac):
    fecha_nac = fecha_nac.isoformat() 
    fecha_nac = fecha_nac.split('-')

    rfc = f"{ap_paterno[:2]}{ap_materno[0]}{nombre[0]}{fecha_nac[0][-2:]}{fecha_nac[1]}{fecha_nac[2]}"
    rfc = unidecode(rfc.upper())   
    return rfc

def valida_credito(ingresos, dependientes):
    aprobado = 0

    if ingresos > 25000.00:
        aprobado = 1
    elif 15000.00 <= ingresos <= 25000.00 and dependientes < 3:
        aprobado = 1
    elif ingresos < 15000.00:
        aprobado = 0 
    
    return aprobado