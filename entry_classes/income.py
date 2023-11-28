"""Módulo para las caracteristicas de la entrada de ingresos"""
import customtkinter 
from CTkMessagebox import CTkMessagebox
import tkinter as tk
from tools.Usos import *
from system_vars.Vars import *
from tools.Usos import center
from .template import TopCalendar
from .template import TopNotas
from .template import valid_amount
from system_vars.Vars import *
import system_vars.config as config
import sqlite3

class Usuario:
    def __init__(self,nombre):
        self.name = nombre

class Income:
    """Clase padre para el manejo de ingresos, gestiona los atributos y los metodos para validar y escribir en la base de datos"""
    def __init__(self):
        self._name : str
        self._date= "Enero"
        self._notas : str
        self._salario = None
        self._wages= None
        self._rentas=None
        self._comisiones = None
        self._ventas= None
        self._misc = None
    def escribir_base_data(self,data):
        # Insertar datos en la tabla
        escribir_valores = '''
        INSERT INTO ingresos (nombre, tipo, monto, moneda, notas, mes)
        VALUES (?, ?, ?, ?, ?, ?)
        '''
        current_data_base = f'{config.currentuser}.db'
        self.conn = sqlite3.connect(current_data_base)
        self.conn.execute(escribir_valores, data)
        self.conn.commit()

        self.conn.close()


class IncomeFrame(Income):
    """Clase que maneja el layout de la interfaz para los ingresos

    :param Income: Clase padre que maneja los atributos de categoria en conjunto con los métodos de escritura en la base de datos
    :type Income: Class
    
    :param name_entry:Donde se digita el nombre del gasto, se accede al valor con name_entry.get(), se debe validar que no este vacía la entrada
    :type name_entry:CTkEntry
    :param options_income_var:variable donde se almacena la elección de la categoría de gasto, se accede al valor con options_spend_var.get()
    :type options_income_var:str
    :param amount_entry_var:variable donde se almacena el mónto del ingreso, se accede al valor con amount_entry_var.get(), se debe convertir el valor a un float y validar está entrada
    :type amount_entry_var: str
    :param coin_var:variable donde se almacena el tipo de cambio, coin_var.get() para acceder 
    :type coin_var:str
    :param others_frame: contiene widgets de otras entradas
    :type others_frame: CTkFrame
    :param final_frame: frame con el boton de salida
    :type final_frame:CTkFrame
    :param final_buttom: Al presionar este botón se debe llamar un método que use métodos de la clase Economy para validar entradas, expulse error o guarde las entradas según sea el caso
    :type final_buttom: CTkButtom
    """
    def __init__(self,layout):
        """Constructor de la clase, configura aspectos de la ventana y carga otras carecteristicas de la apariencia

        :param layout: Frame padre donde se quiren posicionar los frames de la clase
        :type layout: CTkFrame
        """
        super().__init__()
        self.general_info = customtkinter.CTkFrame(master=layout)
        self.general_info.grid_columnconfigure(0,weight=1)
        self.general_info.grid_columnconfigure(5,weight=1)
        self.general_info.grid(row = 1 , column=0,sticky="nsew",pady=20)
        #Widgets para darle un nombre a la entrada de ingreso
        self.name_label = customtkinter.CTkLabel(self.general_info,text="Descripcion del ingreso",
                                                 text_color=TEXT_COLOR,
                                                 font=set_font('Cascadia mono'))
        self.name_label.grid(row=0, column=1,padx=20,pady=20)
        self.name_entry = customtkinter.CTkEntry(self.general_info,
                                                 text_color=TEXT_COLOR,placeholder_text="Nombre del ingreso", 
                                                 font=set_font('Cascadia mono'))
        self.name_entry.grid(row=1, column=1, padx=20,pady=20)
        #Eleccion del tipo de ingreso
        self.descriptive_label = customtkinter.CTkLabel(self.general_info,text="Tipo de ingreso",
                                                 text_color=TEXT_COLOR,
                                                 font=set_font('Cascadia mono'))
        self.descriptive_label.grid(row=0, column=2,padx=20,pady=20)
        self.options_income_var=customtkinter.StringVar(value="Salario")

        self.options_income= customtkinter.CTkOptionMenu(self.general_info, values=["Salario","Comisiones","Ventas","Otros"],variable=self.options_income_var)
        self.options_income.grid(row=1, column=2,padx=20,pady=20)
        #Digitar el monto
        self.amount_label= customtkinter.CTkLabel(self.general_info, 
                                                  text="Mónto", text_color=TEXT_COLOR, 
                                                  font=set_font('Cascadia mono'))
        self.amount_label.grid(row=0, column=3,padx=20,pady=20)
        #self.amount_entry_var= customtkinter.IntVar(value=0)
        self.amount_entry = customtkinter.CTkEntry(self.general_info, 
                                                   font=set_font('Cascadia mono'),
                                                   text_color=TEXT_COLOR)
        self.amount_entry.grid(row=1,column=3,padx=20,pady=20)
        #self.amount_entry_var_true= self.amount_entry_var.get()

        """self.amount_entry = customtkinter.CTkEntry(master=self.general_info, 
                                                   font=set_font('Cascadia mono'),
                                                   text_color=TEXT_COLOR,variable=self.amount_entry_var)
        self.amount_entry.grid(row=1,column=3,padx=20,pady=20)"""

        #Tipo de moneda 
        self.coin_label = customtkinter.CTkLabel(self.general_info,
                                                text='Tipo de cambio',
                                                font=set_font(), 
                                                text_color=TEXT_COLOR)
        self.coin_label.grid(row=0, column=4,padx=20,pady=20,sticky="nsew")
        self.coin_var=customtkinter.StringVar(value="Dólar")
        self.coin_entry = customtkinter.CTkSegmentedButton(self.general_info, values=["Dólar", "Colón", "Euro"],
                                                     command=self.coin_label_callback,
                                                     font=set_font('Shanti'),
                                                     variable=self.coin_var)
        self.coin_entry.grid(row=1,column=4,padx=20,pady=20,sticky="nsew")

        #creo un nuevo frame
        self._others_frame= customtkinter.CTkFrame(master=layout,height=400)
        self._others_frame.grid_columnconfigure(0,weight=1)
        self._others_frame.grid_columnconfigure(4,weight=1)
        self._others_frame.grid(row=2,column=0,sticky="nsew",pady=40)
        #Boton de notas
        notas_image = reader_image(Path_Image,"notas.png",tam=(40,40))
        self.buttom_notas= customtkinter.CTkButton(master=self._others_frame,
                                                      text="Notas",height=50,
                                                      image=notas_image,font=set_font(), 
                                                      compound="top",
                                                      command=self.buttom_notas_callback)
        self.buttom_notas.grid(row=0 , column= 1, padx=20,pady=10, sticky ="nsew")

        #Boton de calendario
        calendar_image = reader_image(Path_Image,"calendario.png",tam=(40,40))
        self.calendario= customtkinter.CTkButton(master=self._others_frame,
                                                      text="Mes",height=50,
                                                      image=calendar_image,font=set_font(), 
                                                      compound="top",
                                                      command=self.buttom_calendar_callback)
        self.calendario.grid(row=0 , column= 2, padx=20,pady=10, sticky ="nsew")
        self.topCalendar=None
        self.topNotas = None
        self.final_frame=customtkinter.CTkFrame(master=layout,height=600)
        self.final_frame.grid(row=3,column=0,sticky="nsew",pady=40)

        self.final_buttom= customtkinter.CTkButton(master=self.final_frame,
                                                   text="Guardar",height=100,width=500,font=set_font(tam=20),
                                                   command=self.event_guardar)
        self.final_buttom.pack(fill=tk.BOTH,expand=True)
         #Conectar con la base de datos
        self.conn=None
        self.conn = sqlite3.connect('ingresos.db')
        self.crear_tabla()
        self.conn.close()

    def crear_tabla(self):
        # Crear una tabla si no existe
        tabla_ingresos = '''
        CREATE TABLE IF NOT EXISTS ingresos (
            nombre TEXT,
            tipo TEXT,
            monto REAL,
            moneda TEXT,
            notas TEXT,
            mes TEXT
        )
        '''
        self.conn.execute(tabla_ingresos)
        self.conn.commit()
    def event_guardar(self):
        """Aqui se deben verificar las entradas del usuario y guardar el nuevo ingreso en la base de datos"""
        self.retrive_data()
        nombre = self._name
        tipo = self.options_income_var.get()
        monto = self._salario
        moneda = self.coin_var.get()
        notas = self._notas
        mes = self._date
        tuple_data = (nombre, tipo , monto,moneda,notas,mes)
        self.escribir_base_data(tuple_data)
        self.amount_entry.delete(0,'end')
        self.name_entry.delete(0,'end')

        
    def coin_label_callback(self,value):
        print(value)

    def buttom_notas_callback(self):
        """llama a la ventana para notas
        ...
        :return: actualiza el atributo de notas 
        :rtype: str
        
        """
        if self.topNotas is None or not self.topNotas.winfo_exists():
            self.topNotas = TopNotas(self.update_notas,config.app)  #Crear la ventana sino existe
            self.topNotas.wm_transient(config.app)
        else:
            self.topNotas.focus()  #Si existe la enfoca
    def buttom_calendar_callback(self):
        """llama a la ventana de elegir mes 
        """
        if self.topCalendar is None or not self.topCalendar.winfo_exists():
            self.topCalendar = TopCalendar(self.update_date ,config.app) 
            self.topCalendar.wm_transient(config.app)
        else:
            self.topCalendar.focus()  
    def update_date(self,n):
        """Esta en una funcion para pasar parametros entre ventanas, solamente actualiza uno de los atributos de la clase con un parametro elegido"""
        self._date=n
    def update_notas(self,n):
        """Esta en una funcion para pasar parametros entre ventanas, solamente actualiza uno de los atributos de la clase con un parametro elegido"""
        self._notas=n
    def retrive_data(self):
        if valid_amount(self.amount_entry.get(),self.coin_var.get()) == False:
            CTkMessagebox(title="Error",message="Entrada invalida de dinero",icon='cancel')
        else:
            self._salario= valid_amount(self.amount_entry.get(),self.coin_var.get())
        self._name = self.name_entry.get()
        





    

