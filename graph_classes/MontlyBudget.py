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

class MonthlyBudgetGraph:
    
    def __init__(self,  root,pathexpense,pathbudget,sheet):
        """
        The function initializes a Monthly Budget Graph Interface with a given root and graphs instance.
        
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
        self.buttom_display = customtkinter.CTkButton(self.month_frame, text="Generar grafico",font=set_font(),command=self.update_date,fg_color=BUTTOM_HOVER)
        self.buttom_display.pack(fill= tk.BOTH,side=tk.BOTTOM, expand=True)
    def show_month_graph(self):
        """
        The function `show_month_graph` displays a bar graph showing the budget and expenses for a
        selected month.
        """
        # Obtiene el mes seleccionado y el índice de este mes.
        selected_month = self.month_var
        if selected_month !=None:
            #Para guardar los datos por mes.
            monthly_data = {
                'Months': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
                'Budget': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                'Expenses': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
            
            # Cargar datos desde un archivo Excel
            try:
                months_expenses_list, total_rent, total_transport, total_entertainment, total_services, total_hygiene, total_insurances, total_debts, total_others = self.data_manager.load_data_expenses_from_excel(self.pathexp, 'Sheet')
                months_budget_list, budget_rent, budget_transport, budget_entertainment, budget_services, budget_hygiene, budget_insurances, budget_debts, budget_others = self.data_manager.load_data_budget_from_excel(self.pathbud, 'Sheet')
            except:
                data_to_excel('Gastos')
                data_to_excel('Presupuesto')
                months_expenses_list, total_rent, total_transport, total_entertainment, total_services, total_hygiene, total_insurances, total_debts, total_others = self.data_manager.load_data_expenses_from_excel(self.pathexp, 'Sheet')
                months_budget_list, budget_rent, budget_transport, budget_entertainment, budget_services, budget_hygiene, budget_insurances, budget_debts, budget_others = self.data_manager.load_data_budget_from_excel(self.pathbud, 'Sheet')
            
            
            # Calcular gastos totales por mes.
            list_expenses = zip(total_rent, total_transport, total_entertainment, total_services, total_hygiene, total_insurances, total_debts, total_others)
            monthly_expenses = [sum(tupla) for tupla in list_expenses]
            #Gastos por meses
            data_expenses = {
                'Months': months_expenses_list,
                'Expenses': monthly_expenses}
            # Integrar datos de data_expenses en annual_data
            for month, expense in zip(data_expenses['Months'], data_expenses['Expenses']):
                index = monthly_data['Months'].index(month)
                monthly_data['Expenses'][index] = expense
                
            # Calcular presupuesto totales por mes.
            list_budget = zip(budget_rent, budget_transport, budget_entertainment, budget_services, budget_hygiene, budget_insurances, budget_debts, budget_others)
            monthly_budget = [sum(tupla) for tupla in list_budget]
            #Gastos por meses
            data_budget = {
                'Months': months_budget_list,
                'Budget': monthly_budget}
            # Integrar datos de data_expenses en annual_data
            for month, budget in zip(data_budget['Months'], data_budget['Budget']):
                index = monthly_data['Months'].index(month)
                monthly_data['Budget'][index] = budget
            
            # Obtiene el mes seleccionado y el índice de este mes.
            selected_month = self.month_var
            # Obtiene el índice del mes seleccionado.
            index = monthly_data['Months'].index(selected_month)

            # Oculta el marco actual.
            #self.month_frame.grid_forget()

            # Crear un nuevo marco para la gráfica.
            self.graph_month_frame = customtkinter.CTkFrame(self.root,fg_color='transparent')
            self.graph_month_frame.grid_rowconfigure(0,weight=1)
            self.graph_month_frame.grid_columnconfigure(0,weight=1)
            self.graph_month_frame.grid_columnconfigure(2,weight=1)
            self.graph_month_frame.grid(row=0, column=0, sticky='nsew')


            # Crea una nueva figura y un eje para la gráfica de barras.
            fig = Figure(figsize=(6, 4), dpi=100)
            ax = fig.add_subplot(111)

            # Configura posiciones de las barras y sus dimensiones.
            ax.bar(0, monthly_data['Budget'][index], width=0.4, label='Budget', align='center')
            ax.bar(1, monthly_data['Expenses'][index], width=0.4, label='Expenses', align='center')

            # Agrega barras para el presupuesto y los gastos.
            ax.set_xticks([0, 1])
            ax.set_xticklabels(['Budget', 'Expenses'])
            ax.set_ylabel('Amount')
            ax.set_title(f'Budget and Expenses for {selected_month}')
            
            # Muestra leyenda.
            ax.legend(loc='lower right')

            # Agrega la gráfica al marco de la interfaz.
            canvas = FigureCanvasTkAgg(fig, master=self.graph_month_frame)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))

            #Botón para volver a la selección de mes.
        #Botón para volver a la selección de mes.
            btn_return = customtkinter.CTkButton(self.graph_month_frame, text="Volver",font=set_font(), command=self.return_to_month_menu)
            btn_return.grid(row=2, column=1,pady=20)
            os.remove(self.pathbud)
            os.remove(self.pathexp)
        else:
            CTkMessagebox(title="Error",message="Debe elegir un mes",icon='cancel')

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