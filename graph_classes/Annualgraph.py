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

class AnnualGraph():
    
    def __init__(self, root, pathex,pathin):
        """
        The above function is the initialization method for a class that creates an interface for an
        annual budget graph.
        
        :param root: The "root" parameter is the main window or the root window of the application. It
        is typically an instance of the Tk class from the tkinter module in Python
        :param graphs_instance: The `graphs_instance` parameter is an instance of a class that contains
        methods for creating and updating graphs. It is used to access the graphing functionality in the
        code
        """
        self.root= root
        self.month_var = tk.StringVar()
        self.data_manager = DataManager()
        self.pathexpenses= pathex
        self.pathincomes = pathin
        self.AnnualBudget_fig = None
    
    # Método para mostrar la gráfica de gastos y presupuesto anuales.
    def show_annual_graph(self):
        """Para generar el grafico del historial anual
        """
        
        #Para guardar los datos por mes.
        annual_data = {
            'Months': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
            'Expenses': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'Incomes': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'Savings': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
        
        # Carga datos desde un archivo Excel
        try:
            months_incomes_list, total_salary, total_commissions, total_sales, total_others = self.data_manager.load_data_incomes_from_excel(self.pathincomes, 'Sheet')
            months_expenses_list, total_rent, total_transport, total_entertainment, total_services, total_hygiene, total_insurances, total_debts, total_others_expenses = self.data_manager.load_data_expenses_from_excel(self.pathexpenses, 'Sheet')
        except:
            data_to_excel('Gastos')
            data_to_excel('Ingresos')
            months_incomes_list, total_salary, total_commissions, total_sales, total_others = self.data_manager.load_data_incomes_from_excel(self.pathincomes, 'Sheet')
            months_expenses_list, total_rent, total_transport, total_entertainment, total_services, total_hygiene, total_insurances, total_debts, total_others_expenses = self.data_manager.load_data_expenses_from_excel(self.pathexpenses, 'Sheet')
        # Calcular ingresos totales por mes.
        list_incomes = zip(total_salary, total_commissions, total_sales, total_others)
        monthly_incomes = [sum(tupla) for tupla in list_incomes]
        print(monthly_incomes)
        #Ingresos por meses.
        data_incomes = {
            'Months': months_incomes_list,
            'Incomes': monthly_incomes}
        # Integrar datos de data_incomes en data
        for month, income in zip(data_incomes['Months'], data_incomes['Incomes']):
            index = annual_data['Months'].index(month)
            annual_data['Incomes'][index] = income
            
        # Calcular gastos totales por mes.
        list_expenses = zip(total_rent, total_transport, total_entertainment, total_services, total_hygiene, total_insurances, total_debts, total_others)
        monthly_expenses = [sum(tupla) for tupla in list_expenses]
        #Gastos por meses
        data_expenses = {
            'Months': months_expenses_list,
            'Expenses': monthly_expenses}
        # Integrar datos de data_expenses en annual_data
        for month, expense in zip(data_expenses['Months'], data_expenses['Expenses']):
            index = annual_data['Months'].index(month)
            annual_data['Expenses'][index] = expense

        # Calcular los ahorros y actualizar la lista 'data'
        annual_data['Savings'] = [income - expense for income, expense in zip(annual_data['Incomes'], annual_data['Expenses'])]

            
        
            
        # Oculta el marco actual

        # Crea un nuevo marco para la gráfica
        self.graph_frame = customtkinter.CTkFrame(self.root,fg_color='transparent')
        self.graph_frame.grid_rowconfigure(0,weight=1)
        self.graph_frame.grid_columnconfigure(0,weight=1)
        self.graph_frame.grid_columnconfigure(2,weight=1)
        self.graph_frame.grid(row=0, column=0, sticky='nsew')
        self.Label = customtkinter.CTkLabel(self.graph_frame,text="Reporte Anual", font=set_font(tam=15),text_color=TEXT_COLOR)
        self.Label.grid(row=0,column=1,pady=10)
        

        # Crea una nueva figura y un eje para la gráfica de barras
        fig = Figure(figsize=(8, 6), dpi=100)
        ax = fig.add_subplot(111)

        # Configura posiciones de las barras y sus dimensiones
        bar_width = 0.35
        bar_positions_incomes = [i for i in range(len(annual_data['Months']))]
        bar_positions_expenses = [i + bar_width for i in bar_positions_incomes]
        bar_positions_savings = [i + 2 * bar_width for i in bar_positions_incomes]

        # Agrega barras para los ingresos, los gastos y los ahorros
        ax.bar(bar_positions_incomes, annual_data['Incomes'], color='blue', width=bar_width, label='Incomes')
        ax.bar(bar_positions_expenses, annual_data['Expenses'], color='orange', width=bar_width, label='Expenses')
        ax.bar(bar_positions_savings, annual_data['Savings'], color='green', width=bar_width, label='Savings')
        ax.set_xticks([i + bar_width / 2 for i in bar_positions_expenses])
        month_labels = ['En','feb','Mar','Abr','May','Jun','Jul',"Agu",'Sep','Oct',"Nov","Dic"]
        ax.set_xticklabels(month_labels)

        # Muestra leyenda
        ax.legend(loc='lower right')

        # Agrega la gráfica al marco de la interfaz
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        os.remove(self.pathexpenses)
        os.remove(self.pathincomes)

        # Botón para regresar a la interfaz principal
        #btn_return = tkk.Button(self.graph_frame, text="Back", command=self.graphs.return_to_main_interface, style='TButton')
        #btn_return.grid(pady=10)
