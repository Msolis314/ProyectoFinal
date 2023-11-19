from sqlalchemy import Column
from sqlalchemy.orm import declarative_base
from sqlalchemy import String,Integer
"""Módulo para crear el frame de la base de datos"""
Base = declarative_base()
class Usuario(Base):
    """Clase para crear el frame de la tabla que contiene los datos del usuario"""
    __tablename__='Usuario'
    #Defino los headers de la tabla
    number= Column(Integer, primary_key=True, autoincrement=True)
    username= Column(String(200))
    password= Column(String(200))