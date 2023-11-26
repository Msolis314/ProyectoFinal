"""Modulo para crear la clase base de funcionalidad para los gastos y el presupuesto"""
import customtkinter
import tkinter as tk
from tools.Usos import *
from system_vars.Vars import *
class Economy:
    """Clase padre para atributos y caracteristicas de las clases de presupuesto y gasto"""
    def __init__(self):
        self._date= None
        self._category= None
        self._domicilio = None
        self._higiene = None
        self._transporte = None
        self._vestimenta = None
        self._entretenimiento = None
        self._deudas = None
        self._seguros = None
        self._ahorros = None
        self._servicios = None
        self._otros = None
    def set_atr(self,entry):
        """Esta funcion seria para setear alguno de los atributos una vez resibida la entrada"""
        pass
    def get_atr(self):
        """Esta funcion deberia buscar en la base de datos por los atributos, seria para la del presupuesto"""
        pass
    def write_data(self):
        """Funcion para escibrir en la base de datos"""
        pass

class TopCalendar(customtkinter.CTkToplevel):
    """Clase para crear una ventana externa para elegir la fecha"""
    def __init__(self,update ,*args, **kwargs):
        super().__init__(*args, **kwargs)
        center(self,60,60)
        self.option_menu_var= customtkinter.StringVar(value="Enero")
        self.option_calendar=customtkinter.CTkOptionMenu(self, 
                                                         values=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"],
                                                         width=50,
                                                         height=50,
                                                         corner_radius=4,
                                                         command=self.option_menu_callback,
                                                         dropdown_hover_color=HOVER_COLOR,
                                                         font=set_font(),dropdown_font=set_font('Shanti'),
                                                         variable=self.option_menu_var)
        self.update_date=update
        self.option_calendar.pack(fill=tk.BOTH,expand=True)
    def option_menu_callback(self,var:str):
        """En esta funcion se llama a la funcion de la otra clase, se encarga de pasarle el valor elegido de fecha a la ventana principal
        :param var: mes seleccionado
        :type var: str
        ...
        :return: llama a la funcion que actualiza a la fecha
        """
        self.update_date(var)
        self.destroy()