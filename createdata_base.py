import sqlalchemy as db
import tablesetting.tablelogin as mod
#creo la base de datos en el repo actual
""" el primer argumento (Url) indica 
1.Que tipo de database se intenta conectar
2.DPAPI third party driver 
3.donde ponemos la database
"""
en = db.create_engine('sqlite:///basedata/login.sqlite',echo=True,future=True)
#Creo todas las tablas en la engine
mod.Base.metadata.create_all(en)