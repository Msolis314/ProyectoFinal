import customtkinter 
import tkinter as tk
from tools.Usos import *
from system_vars.Vars import *
from tools.Usos import center
from .template import TopCalendar
from system_vars.Vars import *
import system_vars.config as config
"""Módulo para las caracteristicas de la entrada de ingresos"""
class Usuario:
    def __init__(self,nombre):
        self.name = nombre

class Income:
    """Clase padre para el manejo de ingresos, gestiona los atributos y los metodos para validar y escribir en la base de datos"""
    def __init__(self):
        self._date= None
        self._salario = None
        self._wages= None
        self._rentas=None
        self._comisiones = None
        self._ventas= None
        self._misc = None

class IncomeFrame(Income):
    """Clase que maneja el layout de la interfaz para los ingresos"""
    def __init__(self,layout):
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

        self.options_income= customtkinter.CTkOptionMenu(self.general_info, values=["Salario","Comisiones","Ventas","Otros"])
        self.options_income.grid(row=1, column=2,padx=20,pady=20)
        #Digitar el monto
        self.amount_label= customtkinter.CTkLabel(self.general_info, 
                                                  text="Mónto", text_color=TEXT_COLOR, 
                                                  font=set_font('Cascadia mono'))
        self.amount_label.grid(row=0, column=3,padx=20,pady=20)

        self.amount_entry = customtkinter.CTkEntry(self.general_info, 
                                                   font=set_font('Cascadia mono'),
                                                   text_color=TEXT_COLOR)
        self.amount_entry.grid(row=1,column=3,padx=20,pady=20)

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
        self.final_frame=customtkinter.CTkFrame(master=layout,height=600)
        self.final_frame.grid(row=3,column=0,sticky="nsew",pady=40)

        self.final_buttom= customtkinter.CTkButton(master=self.final_frame,text="Guardar",height=100,width=500,font=set_font(tam=20))
        self.final_buttom.pack(fill=tk.BOTH,expand=True)

        
    def coin_label_callback(self,value):
        print(value)

    def buttom_notas_callback(self):
        pass
    def buttom_calendar_callback(self):
        if self.topCalendar is None or not self.topCalendar.winfo_exists():
            self.topCalendar = TopCalendar(self.update_date,config.app)  # create window if its None or destroyed
            self.topCalendar.wm_transient(config.app)
        else:
            self.topCalendar.focus()  # if window exists focus it
    def update_date(self,n):
        """Esta en una funcion para pasar parametros entre ventanas, solamente actualiza uno de los atributos de la clase con un parametro elegido"""
        self._date=n



    

