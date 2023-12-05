"""Modulo para reporte

    :raises Exception: _description_
    :return: _description_
    :rtype: _type_
    """
import tkinter as tk
from tkinter import ttk as tkk
import customtkinter
from CTkMessagebox import CTkMessagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from .DataManager import DataManager
from entry_classes.template import TopCalendar
from tools.Usos import *
from system_vars.Vars import *
from tablesetting.base_to_excel import data_to_excel
import system_vars.config as config

class Report:
    
    def __init__(self,  root,pathexpense,pathbudget,sheet):
        """
        funcion para darle al usuario un reporte de sus gastos y presupuesto
        
        :param root: The "root" parameter is the main window or root window of the application. It is
        typically created using the Tk() function from the tkinter module
        :param graphs_instance: The parameter "graphs_instance" is an instance of a class that contains
        methods for creating and updating graphs. It is used in the code to access the graph-related
        functionality
        """
        self.root = root
        self.month_var = None # Variable para almacenar el mes seleccionado.
        self.data_manager = DataManager()
        self.MonthlyBudget_fig = None
        self.pathexp = pathexpense
        self.pathbud = pathbudget
        self.sheet = sheet
    
    def show_select_month(self):
        """
        The function creates a dropdown menu for selecting a month and includes buttons for showing a
        graph and returning to the main interface.
        """
        self.month_frame = customtkinter.CTkFrame(self.root,fg_color='transparent')
        self.month_frame.grid(row=0,column=0)
        # Ocultar el marco de la interfaz principal, si está visible.
        self.option_menu_var= customtkinter.StringVar(value="Enero")
        self.option_calendar=customtkinter.CTkOptionMenu(self.month_frame, 
                                                         values=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"],
                                                         width=50,
                                                         height=50,
                                                         corner_radius=4,
                                                         dropdown_hover_color=HOVER_COLOR,
                                                         font=set_font(),dropdown_font=set_font('Shanti'),
                                                         variable=self.option_menu_var)
        self.option_calendar.pack(fill=tk.BOTH,expand=True,pady=20)
        self.buttom_display = customtkinter.CTkButton(self.month_frame, text="Generar Reporte",font=set_font(),command=self.update_date,fg_color=BUTTOM_HOVER)
        self.buttom_display.pack(fill= tk.BOTH,side=tk.BOTTOM, expand=True)
    def show_month_graph(self):
        """
        funcion para desplegar el reporte
        """
        selected_month_name = self.month_var
        #Para guardar los datos por mes.
        monthly_data = {
            'Categories': ['Domicilio','Higiene','Transporte','Entretenimiento','Deudas','Seguros','Servicios','Otros'],
            'Budget': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'Expenses': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
        dict_compare = {'Domicilio':[],'Higiene':[],'Transporte':[],'Entretenimiento':[],'Deudas':[],'Seguros':[],'Servicios':[],'Otros':[]}
        # Cargar datos desde un archivo Excel
        try:
            months_expenses_list, total_rent, total_transport, total_entertainment, total_services, total_hygiene, total_insurances, total_debts, total_others = self.data_manager.load_data_expenses_from_excel(self.pathexp, 'Sheet')
            months_budget_list, budget_rent, budget_transport, budget_entertainment, budget_services, budget_hygiene, budget_insurances, budget_debts, budget_others = self.data_manager.load_data_budget_from_excel(self.pathbud, 'Sheet')
        except:
            data_to_excel('Gastos')
            data_to_excel('Presupuesto')
            months_expenses_list, total_rent, total_transport, total_entertainment, total_services, total_hygiene, total_insurances, total_debts, total_others = self.data_manager.load_data_expenses_from_excel(self.pathexp, 'Sheet')
            months_budget_list, budget_rent, budget_transport, budget_entertainment, budget_services, budget_hygiene, budget_insurances, budget_debts, budget_others = self.data_manager.load_data_budget_from_excel(self.pathbud, 'Sheet')
        
        try:
            selected_month_index_ex = months_expenses_list.index(selected_month_name)
            selected_month_index_bud=months_budget_list.index(selected_month_name)
        except:
            CTkMessagebox(title="Error",message="Datos insuficientes para el mes")
            self.return_to_month_menu()
            os.remove(self.pathexp)
            os.remove(self.pathbud)
            raise Exception
        dict_compare['Domicilio'].append(total_rent[selected_month_index_ex])
        dict_compare['Transporte'].append(total_transport[selected_month_index_ex])
        dict_compare['Entretenimiento'].append(total_entertainment[selected_month_index_ex])
        dict_compare['Servicios'].append(total_services[selected_month_index_ex])
        dict_compare['Seguros'].append(total_insurances[selected_month_index_ex])
        dict_compare['Deudas'].append(total_debts[selected_month_index_ex])
        dict_compare['Higiene'].append(total_hygiene[selected_month_index_ex])
        dict_compare['Otros'].append(total_others[selected_month_index_ex])
        
        dict_compare['Domicilio'].append(budget_rent[selected_month_index_bud])
        dict_compare['Transporte'].append(budget_transport[selected_month_index_bud])
        dict_compare['Entretenimiento'].append(budget_entertainment[selected_month_index_bud])
        dict_compare['Servicios'].append(budget_services[selected_month_index_bud])
        dict_compare['Seguros'].append(budget_insurances[selected_month_index_bud])
        dict_compare['Deudas'].append(budget_debts[selected_month_index_bud])
        dict_compare['Higiene'].append(budget_hygiene[selected_month_index_bud])
        dict_compare['Otros'].append(budget_others[selected_month_index_bud])
        
        for key in dict_compare:
            try:
                
                dif = dict_compare[key][1]- dict_compare[key][0]
            except:
                dif = 0
            dict_compare[key].append(dif)
        

        # Oculta el marco actual.
        #self.month_frame.grid_forget()

        # Crear un nuevo marco para la gráfica.
        self.graph_month_frame = customtkinter.CTkFrame(self.root,fg_color='transparent')
        self.graph_month_frame.grid_rowconfigure(0,weight=1)
        self.graph_month_frame.grid_columnconfigure(0,weight=1)
        self.graph_month_frame.grid_columnconfigure(4,weight=1)
        self.graph_month_frame.grid(row=0, column=0, sticky='nsew')
        self.Label_bud = customtkinter.CTkLabel(self.graph_month_frame,text='Gasto',font=set_font(),text_color=TEXT_COLOR)
        self.Label_bud.grid(row=0, column=1,padx=30)
        self.Label_spend = customtkinter.CTkLabel(self.graph_month_frame,text='Presupuesto',font=set_font(),text_color=TEXT_COLOR)
        self.Label_spend.grid(row=0, column=2,padx=30)
        self.Label_dif = customtkinter.CTkLabel(self.graph_month_frame,text='Diferencia',font=set_font(),text_color=TEXT_COLOR)
        self.Label_dif.grid(row=0, column=3,padx=30)
        for index,type_cat in enumerate(monthly_data['Categories']):
             customtkinter.CTkLabel(self.graph_month_frame,text=type_cat,text_color=TEXT_COLOR,
                                                 font=set_font('Cascadia Mono')).grid(row = 1+ index, column=0,pady=5,padx=5)
        
        for index, key in enumerate(dict_compare):
            customtkinter.CTkLabel(self.graph_month_frame,text=f'{dict_compare[key][0]}',text_color=TEXT_COLOR,
                                                 font=set_font('Cascadia Mono')).grid(row = 1+ index, column=1,pady=5,padx=5)
        
        for index, key in enumerate(dict_compare):
            customtkinter.CTkLabel(self.graph_month_frame,text=f'{dict_compare[key][1]}',text_color=TEXT_COLOR,
                                                 font=set_font('Cascadia Mono')).grid(row = 1+ index, column=2,pady=5,padx=5)
        for index, key in enumerate(dict_compare):
            customtkinter.CTkLabel(self.graph_month_frame,text=f'{dict_compare[key][2]}',text_color=TEXT_COLOR,
                                                 font=set_font('Cascadia Mono')).grid(row = 1+ index, column=3,pady=5,padx=5)





        # Crea una nueva figura y un eje para la gráfica de barras.
       

        #Botón para volver a la selección de mes.
       #Botón para volver a la selección de mes.
        btn_return = customtkinter.CTkButton(self.graph_month_frame,hover_color=HOVER_COLOR,fg_color=BORDER_COLOR ,text="Volver",font=set_font(), command=self.return_to_month_menu)
        btn_return.grid(row=12, column=0,columnspan=7,pady=40,sticky='nsew')
        os.remove(self.pathbud)
        os.remove(self.pathexp)

    def return_to_month_menu(self):
        """
        The function returns to the month menu and updates the title of the root window.
        """
        self.show_select_month()

        if hasattr(self, 'graph_month_frame') and hasattr(self.graph_month_frame, 'destroy'):
            self.graph_month_frame.destroy()

        
    def update_date(self):
        self.month_var=self.option_menu_var.get()
        self.show_month_graph()