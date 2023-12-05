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
        self.expense_fig = None
        
    # Método para mostrar el menú desplegable de selección de mes.
    def show_select_month(self):
        """
        The function creates a dropdown menu for selecting a month and includes buttons for showing a
        graph and returning to the main interface.
        """
        
        # Ocultar el marco de la interfaz principal, si está visible.
        self.graphs.frame.grid_forget()
        
        self.root.title("Month Dropdown Menu")

        # Crea el marco de selección de mes.
        self.month_frame = tkk.Frame(self.root, padding="10")
        self.month_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Crea el menú de selección de mes.
        month_menu = tkk.Combobox(self.month_frame, textvariable=self.month_var, values=self.months, state="readonly")
        month_menu.current(0)
        month_menu.grid(pady=10, padx=10)

        # Botón para mostrar la gráfica.
        btn_show_graph = tkk.Button(self.month_frame, text="Show Graph", command=self.show_expense_graph)
        btn_show_graph.grid(pady=10)

        # Botón para regresar a la interfaz principal.
        btn_return = tkk.Button(self.month_frame, text="Back", command=self.graphs.return_to_main_interface, style='TButton')
        btn_return.grid(pady=10)

    # Método para mostrar la gráfica de gastos.
    def show_expense_graph(self):
        """
        The function `show_expense_graph` displays a pie chart of monthly expenses based on selected
        month and data from an Excel file.
        """
        
        # Obtiene el mes seleccionado.
        selected_month_name = self.month_var.get()
        
        # Carga los datos del Excel.
        months_expenses_list, total_rent, total_transport, total_entertainment, total_services, total_hygiene, total_insurances, total_debts, total_others = self.data_manager.load_data_expenses_from_excel('FILE.xlsx', 'Data')
        
        # Obtiene el índice del mes seleccionado.
        selected_month_index = months_expenses_list.index(selected_month_name)
        
        # Filtrar los valores para las categorías de gastos.
        selected_rent = total_rent[selected_month_index]
        selected_transport = total_transport[selected_month_index]
        selected_entertainment = total_entertainment[selected_month_index]
        selected_services = total_services[selected_month_index]
        selected_personal_hygiene = total_hygiene[selected_month_index]
        selected_insurance = total_insurances[selected_month_index]
        selected_debts = total_debts[selected_month_index]
        selected_others = total_others[selected_month_index]
        
        # Crea y muestra la gráfica circular.
        self.graphs.frame.grid_forget()

        self.graph_frame = tkk.Frame(self.root, padding="10")
        self.graph_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        fig = Figure(figsize=(6, 6), dpi=100)
        ax = fig.add_subplot(111)

        # Crear la lista de categorías y la lista de gastos para la gráfica circular.
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
                
        # Botón para volver a la selección de mes.
        btn_return = tkk.Button(self.graph_frame, text="Back", command=self.return_to_month_menu, style='TButton')
        btn_return.grid(pady=10)

    #Método para volver a la selección de mes.   
    def return_to_month_menu(self):
        """
        The function returns to the month menu and updates the title of the root window.
        """
        self.month_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        if hasattr(self, 'graph_frame') and hasattr(self.graph_frame, 'destroy'):
            self.graph_frame.destroy()

        self.root.title("Month Dropdown Menu")