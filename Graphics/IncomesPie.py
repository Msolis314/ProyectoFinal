import tkinter as tk
from tkinter import ttk as tkk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from DataManager import DataManager


class IncomesPie():
    
    def __init__(self, root, graphs_instance):
        """
        The above function is the initialization method for a class that creates an interface for
        displaying income graphs.
        
        :param root: The "root" parameter is the main window or root window of the application. It is
        typically an instance of the Tk class from the tkinter module
        :param graphs_instance: The `graphs_instance` parameter is an instance of a class that contains
        methods for generating and displaying graphs. It is used to access the graphing functionality in
        the code
        """
        self.root = root
        self.root.title("Income Graph Interface")
        self.month_var = tk.StringVar() # Variable para almacenar el mes seleccionado.
        self.data_manager = DataManager()
        self.graphs = graphs_instance
        self.months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        self.incomes_fig = None
        
        
    # Método para mostrar la gráfica de ingresos.
    def show_income_graph(self):
        """
        The function `show_income_graph` displays a pie chart of income categories based on the selected
        month's data from an Excel file.
        """
        
        # Obtiene el mes seleccionado.
        selected_month_name = self.month_var.get()
        
        # Obtiene el índice del mes seleccionado.
        selected_month_index = self.months.index(selected_month_name)
        
        #Carga datos del excel.
        salary, commissions, sales, others = self.data_manager.load_data_incomes_from_excel('FILE.xlsx', 'Data')
        
        # Filtrar los valores no nulos para las categorías de ingresos del excel.
        list_salary = [value for value in salary if not pd.isna(value)]
        selected_salary = list_salary[selected_month_index]
        list_commissions = [value for value in commissions if not pd.isna(value)]
        selected_commissions = list_commissions[selected_month_index]
        list_sales = [value for value in sales if not pd.isna(value)]
        selected_sales = list_sales[selected_month_index]
        list_others = [value for value in others if not pd.isna(value)]
        selected_others = list_others[selected_month_index]
        
        # Crea y muestra gráfica circular.
        self.graphs.frame.grid_forget()

        self.graph_frame = tkk.Frame(self.root, padding="10")
        self.graph_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        fig = Figure(figsize=(5, 5), dpi=100)
        ax = fig.add_subplot(111)

        # Crear la lista de ingresos y la lista de sus montos para la gráfica circular.
        categories = ['Salario', 'Comisiones', 'Ventas', 'Otros']
        data = [selected_salary, selected_commissions, selected_sales, selected_others]

        pie_patches, texts, autotexts = ax.pie(data, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')

        ax.legend(pie_patches, categories, loc='lower right')

        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.root.title("Monthly Income Graph")
