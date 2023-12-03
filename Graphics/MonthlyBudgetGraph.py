import tkinter as tk
from tkinter import ttk as tkk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from DataManager import DataManager


class MonthlyBudgetGraph():
    
    def __init__(self, root, graphs_instance):
        """
        The function initializes a Monthly Budget Graph Interface with a given root and graphs instance.
        
        :param root: The "root" parameter is the main window or root window of the application. It is
        typically created using the Tk() function from the tkinter module
        :param graphs_instance: The parameter "graphs_instance" is an instance of a class that contains
        methods for creating and updating graphs. It is used in the code to access the graph-related
        functionality
        """
        self.root = root
        self.root.title("Monthly Budget Graph Interface")
        self.month_var = tk.StringVar() # Variable para almacenar el mes seleccionado.
        self.data_manager = DataManager()
        self.graphs = graphs_instance
        self.months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        self.MonthlyBudget_fig = None

    # Método para mostrar la gráfica de gastos y presupuesto mensuales.
    def show_month_graph(self):
        """
        The function `show_month_graph` displays a bar graph showing the budget and expenses for a
        selected month.
        """
        
        # Cargar datos desde un archivo Excel
        rent, transport, entertainment, services, personal_hygiene, insurance, debts, others = self.data_manager.load_data_expenses_from_excel('FILE.xlsx', 'Data')
        rent, transport, entertainment, services, personal_hygiene, insurance, debts, others = self.data_manager.load_data_budget_from_excel('FILE.xlsx', 'Data')
        
        # Calcular gastos totales por mes.
        list_expenses = zip(rent, transport, entertainment, services, personal_hygiene, insurance, debts, others)
        monthly_expenses = [sum(tupla) for tupla in list_expenses]
        
        # Calcular presupuesto totales por mes.
        list_budget = zip(rent, transport, entertainment, services, personal_hygiene, insurance, debts, others)
        monthly_budget = [sum(tupla) for tupla in list_budget]
            
        
        # Obtiene el mes seleccionado y el índice de este mes.
        selected_month = self.month_var.get()
        index = self.months.index(selected_month)

        # Oculta el marco actual.
        self.month_frame.grid_forget()

        # Crear un nuevo marco para la gráfica.
        self.graph_month_frame = tkk.Frame(self.root, padding="10")
        self.graph_month_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Crea una nueva figura y un eje para la gráfica de barras.
        fig = Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)

        # Configura posiciones de las barras y sus dimensiones.
        ax.bar(0, monthly_budget[index], width=0.4, label='Budget', align='center')
        ax.bar(1, monthly_expenses[index], width=0.4, label='Expenses', align='center')

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
        canvas_widget.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))