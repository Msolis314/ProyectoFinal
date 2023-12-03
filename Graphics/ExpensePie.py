import tkinter as tk
from tkinter import ttk as tkk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from DataManager import DataManager


class ExpensePie():
    """
    The `ExpensePie` class creates a GUI interface for displaying a pie chart of monthly expenses based
    on selected month and data from an Excel file.
    
    :param root: The "root" parameter is the main window or the root window of the application. It is
    the top-level window that contains all other widgets and elements of the user interface
    :param graphs_instance: The `graphs_instance` parameter is an instance of a class that contains
    methods for creating and updating graphs. It is used to access the graph-related functionality in
    the code
    """
    
    """
        The function initializes the main graph interface and creates instances of various graph
        components.
        
        :param root: The "root" parameter is the main window or the root window of the application. It
        is the top-level window that contains all other widgets and elements of the user interface
        """
    def __init__(self, root, graphs_instance):
        """
        The above function is the initialization method for a class that creates a GUI interface for an
        expense graph.
        
        :param root: The "root" parameter is the main window or the root window of the application. It
        is typically an instance of the Tk class from the tkinter module
        :param graphs_instance: The `graphs_instance` parameter is an instance of a class that contains
        methods for creating and updating graphs. It is used to access the graph-related functionality
        in the code
        """
        self.root = root
        self.root.title("Expense Graph Interface")
        self.month_var = tk.StringVar() # Variable para almacenar el mes seleccionado.
        self.data_manager = DataManager()
        self.graphs = graphs_instance
        self.months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        self.expense_fig = None
        

    # Método para mostrar la gráfica de gastos.
    def show_expense_graph(self):
        """
        The function `show_expense_graph` displays a pie chart of monthly expenses based on selected
        month and data from an Excel file.
        """
        
        # Obtiene el mes seleccionado.
        selected_month_name = self.month_var.get()
        
        # Obtiene el índice del mes seleccionado.
        selected_month_index = self.months.index(selected_month_name)
        
        #Carga datos del excel.
        rent, transport, entertainment, services, personal_hygiene, insurance, debts, others = self.data_manager.load_data_expenses_from_excel('FILE.xlsx', 'Data')
        
        # Filtrar los valores no nulos para las categorías de gastos del excel.
        list_rent = [value for value in rent if not pd.isna(value)]
        selected_rent = list_rent[selected_month_index]
        list_transport = [value for value in transport if not pd.isna(value)]
        selected_transport = list_transport[selected_month_index]
        list_entertainment = [value for value in entertainment if not pd.isna(value)]
        selected_entertainment = list_entertainment[selected_month_index]
        list_services = [value for value in services if not pd.isna(value)]
        selected_services = list_services[selected_month_index]
        list_personal_hygiene = [value for value in personal_hygiene if not pd.isna(value)]
        selected_personal_hygiene = list_personal_hygiene[selected_month_index]
        list_insurance = [value for value in insurance if not pd.isna(value)]
        selected_insurance = list_insurance[selected_month_index]
        list_debts = [value for value in debts if not pd.isna(value)]
        selected_debts = list_debts[selected_month_index]
        list_others = [value for value in others if not pd.isna(value)]
        selected_others = list_others[selected_month_index]
        

        # Crea y muestra gráfica circular.
        self.graphs.frame.grid_forget()

        self.graph_frame = tkk.Frame(self.root, padding="10")
        self.graph_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        fig = Figure(figsize=(6, 6), dpi=100)
        ax = fig.add_subplot(111)

        # Crear la lista de categorias y la lista de gastos para la gráfica circular.
        categories = ['Domicilio', 'Transporte', 'Entretenimiento', 'Servicios', 'Higiene Personal', 'Seguros', 'Deudas', 'Otros']
        data = [selected_rent, selected_transport, selected_entertainment, selected_services, selected_personal_hygiene, selected_insurance, selected_debts, selected_others]

        # Configurar la gráfica circular con la leyenda y los porcentajes.
        pie_patches, texts, autotexts = ax.pie(data, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        
        ax.legend(pie_patches, categories, loc='lower right')
        
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.root.title("Monthly Expense Graph")