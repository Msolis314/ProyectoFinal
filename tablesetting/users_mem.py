import sqlalchemy as db
from .tablelogin import Usuario
from sqlalchemy.orm import Session
"""Módulo con la operaciones para buscar en la bse de datos"""
class Usuario_mem():
    """Clase que se encarga de gestionar la tabla de datos del usuario"""
    def __init___(self):
        self.engine= db.create_engine('sqlite:///basedata/login.sqlite',echo=False,future=True)
    def get_user(self,user_name:str):
        self.engine= db.create_engine('sqlite:///basedata/login.sqlite',echo=False,future=True)
        user: Usuario = None
        """Se utiliza el with para limitar el
          uso del operador de transacciones 
        Session, que sirve para conectarse a 
        la database, es para utilizar los objetos de la base de datos"""
        with Session(self.engine) as session:
            user= session.query(Usuario).filter_by(username=user_name).first()
            #Sino lo encuentra retorna None
        return user
    def new_user(self,user : Usuario):
        self.engine= db.create_engine('sqlite:///basedata/login.sqlite',echo=False,future=True)
        with Session(self.engine) as session:
            session.add(user)
            session.commit()

