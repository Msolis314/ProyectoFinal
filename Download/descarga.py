"""Modulo para crear las opciones de descarga de datos para el usuario
    """
import customtkinter
import tkinter as tk
import os
from tools.Usos import *
from system_vars.Vars import *
from tablesetting.base_to_excel import *
from tkinter import filedialog as fd
import system_vars.config as config
from entry_classes.template import TopCalendar
from CTkMessagebox import CTkMessagebox

class DescargaChoice:
    """ Clase para manejar los elementos que permiten la descarga de excel con las tablas
    """
    def __init__(self,layout):
        self.title_frame= customtkinter.CTkFrame(layout, height=200,fg_color=FG_COLOR)
        self.title_frame.pack(fill='both',side=tk.TOP,pady=35)
        self.title_label = customtkinter.CTkLabel(self.title_frame, text= "Opciones de descarga",font=set_font('Cascadia mono SemiBold', 24))
        self.title_label.pack()
        self.final_frame = customtkinter.CTkFrame(layout,height=200,fg_color=FG_COLOR)
        self.final_frame.pack(fill='both',side=tk.BOTTOM,expand=True)
        self.final_buttom= customtkinter.CTkButton(master=self.final_frame,
                                                   text="Descargar",height=200,width=500,font=set_font(tam=20),
                                                   command=self.event_descarga)
        self.final_buttom.pack(fill=tk.BOTH,expand=True,pady=20)
        self.botton_frame = customtkinter.CTkFrame(layout,fg_color=FG_COLOR)
        self.botton_frame.pack(fill='both',expand=True,side=tk.BOTTOM,pady=30)
        self.botton_frame.grid_columnconfigure(0,weight=1)
        self.botton_frame.grid_columnconfigure(3,weight=1)
        #Botones tipo checkbox 
        self.checkboxingresos_var = customtkinter.StringVar(value='off')
        checkboxingresos = customtkinter.CTkCheckBox(self.botton_frame,text = "Tabla de ingresos",fg_color=BORDER_COLOR,hover_color=HOVER_COLOR,font=set_font(),onvalue='on',offvalue='off',variable=self.checkboxingresos_var)
        checkboxingresos.grid(row=0,column=2,sticky='nsew', pady=20)
        self.checkboxgastos_var = customtkinter.StringVar(value='off')
        checkboxgastos = customtkinter.CTkCheckBox(self.botton_frame,text = "Tabla de gastos",font=set_font(),onvalue='on',offvalue='off',variable=self.checkboxgastos_var)
        checkboxgastos.grid(row=1,column=2,sticky='nsew',pady=20)
        self.checkboxbudget_var = customtkinter.StringVar(value='off')
        checkboxbudget = customtkinter.CTkCheckBox(self.botton_frame,text = "Tabla de presupuesto",fg_color=BORDER_COLOR,hover_color=HOVER_COLOR,font=set_font(),onvalue='on',offvalue='off',variable=self.checkboxbudget_var)
        checkboxbudget.grid(row=2,column=2,sticky='nsew',pady=20)

        
    def event_descarga(self):
        path_save = fd.askdirectory()
        if os.path.exists(path_save) != True:
            CTkMessagebox(title="Error",message="Debe ingresar un directorio valido",icon='cancel')
        else:
            if self.checkboxingresos_var.get() == 'on':
                data_excel_save('ingresos',path_save)
            if self.checkboxgastos_var.get() == 'on':
                data_excel_save('gastos',path_save)
            if self.checkboxbudget_var.get() == 'on':
                data_excel_save('presupuesto',path_save)
        print(path_save)
    

        

        