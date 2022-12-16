from pydantic import BaseModel, validator, Field
from typing import Optional
from datetime import date, datetime

class User(BaseModel):
    id: Optional[int]
    primer_nombre: str
    apellido_paterno: str
    apellido_materno: str 
    fecha_de_nacimiento: date = Field(example='DD-MM-YYYY')
    ingresos_mensuales: float
    numero_dependientes_economicos: int

    @validator("fecha_de_nacimiento", pre=True)
    def parse_fecha_nac(cls, value):
        return datetime.strptime(value,"%d-%m-%Y").date()


class UserOut(BaseModel):
    id: int
    RFC: str
    APROBADO: bool
