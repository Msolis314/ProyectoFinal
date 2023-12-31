"""Modulo para crear la clase base de funcionalidad para los gastos y el presupuesto"""
import customtkinter
from CTkMessagebox import CTkMessagebox
import tkinter as tk
from tools.Usos import *
from system_vars.Vars import *
class Economy:
    """Clase padre para atributos y caracteristicas de las clases de presupuesto y gasto"""
    def __init__(self):
        self._date= "Enero"
        self._notas=""
        self._domicilio = 0
        self._higiene = 0
        self._transporte = 0
        self._vestimenta = 0
        self._entretenimiento = 0
        self._deudas = 0
        self._seguros = 0
        self._ahorros = 0
        self._servicios = 0
        self._otros = 0
    def set_atr(self,entry,type,coin):
        """Esta funcion seria para setear alguno de los atributos una vez resibida la entrada

        :param entry: entrada del usuario
        :type entry: str
        :param type: Categoria del gasto
        :type type: moneda
        :param coin: Tipo de cambio
        :type coin: str
        :raises ExceptionSystem: Levanta una excepcion si no se puede convertir el valor a un float o si es negativa
        :raises ExceptionSystem: En caso que por alguna razon fallen los atributos preestablecidos
        """
        if valid_amount(entry,coin) == False:
            CTkMessagebox(title="Error",message="Valor invalido",icon='cancel')
            raise ExceptionSystem("Error en el valor")
        if type == "Domicilio":
            print(entry)
            self._domicilio= valid_amount(entry,coin)
        elif type == "Comida":
            self._domicilio = valid_amount(entry,coin)
        elif type == "Higiene":
            self._higiene = valid_amount(entry, coin)
        elif type == "Transporte":
            self._transporte = valid_amount(entry,coin)
        elif type == "Vestimenta":
            self._vestimenta = valid_amount(entry, coin)
        elif type == "Entretenimiento":
            self._entretenimiento = valid_amount(entry,coin)
        elif type == "Deudas":
            self._deudas = valid_amount(entry,coin)
        elif type == "Seguros":
            self._seguros = valid_amount(entry,coin)
        elif type == "Servicios":
            self._servicios= valid_amount(entry,coin)
        elif type == "Otros":
            self._otros = valid_amount(entry,coin)
        else:
            raise ExceptionSystem("Error en los atributos permitidos")
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
        print(var)
        self.update_date(var)
        self.destroy()

class TopNotas(customtkinter.CTkToplevel):
    """Clase para obtener la entrada de una nota cualquiera que el usuario quiera agregar al gasto o ingreso

    :param notas_text: donde se digita la entrada de texto
    :type notas_text: CTkTextbox
    :param notas_save_buttom: Boton para guardar el texto
    :types notas_save_buttom: CTkButton
    """
    def __init__(self,update ,*args, **kwargs):
        """Constructora de la clase, define caracteristicas de la apariencia

        :param update: funcion externa que sirve para conectar la ventana hija a la padre
        :type update: funcion
        """
        super().__init__(*args, **kwargs)
        center(self,200,200)
        self.notas_text= customtkinter.CTkTextbox(self,font=set_font(),text_color=TEXT_COLOR,height=100)
        self.notas_text.pack(fill='both',expand=False,side=tk.TOP)
        self.notas_save_buttom=customtkinter.CTkButton(self,text='Guardar', font=set_font(),text_color=TEXT_COLOR,command=self.notas_text_callback)
        self.notas_save_buttom.pack(fill='both',expand=False,side=tk.BOTTOM)
        self.update_text=update


    def notas_text_callback(self):
        text_var=self.notas_text.get("1.0",'end-1c')
        self.update_text(text_var)
        self.destroy()

def negative_value_excep(value):
    """Funcion para generar una excepcion con valores negativos

    :param value: numero ingresado
    :type value: float
    :raises ExceptionSystem: Levanta la excepcion si el numero es negativo
    """
    if value < 0 : 
        raise ExceptionSystem("Valor ingresado no puede ser negativo")
def valid_amount(money_amount,moneda:str):
    """Funcion para revisar que el monto ingresado es valido

    :param money_amount: entrada numerica del usuario
    :type money_amount: str
    :param moneda: tipo de cambio
    :type moneda: str
    :return: False si falla en convertir la entrada a un tipo entero
    :rtype: Boolean
    :return: valor convertido a colones si lo convierte a entero
    :rtype: float
    """
    try: 
        value = float(money_amount)
        negative_value_excep(value)
        return convertir_moneda(value,moneda)
    except ValueError as e:
        print(f"Error:{e}")
        return False
    except ExceptionSystem as e:
        print(f'Error:{e}')
        return False
       
    
