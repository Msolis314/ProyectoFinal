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
        self.MonthlyBudget_fig = None
    
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
        btn_show_graph = tkk.Button(self.month_frame, text="Show Graph", command=self.show_month_graph)
        btn_show_graph.grid(pady=10)

        # Botón para regresar a la interfaz principal.
        btn_return = tkk.Button(self.month_frame, text="Back", command=self.graphs.return_to_main_interface, style='TButton')
        btn_return.grid(pady=10)

    # Método para mostrar la gráfica de gastos y presupuesto mensuales.
    def show_month_graph(self):
        """
        The function `show_month_graph` displays a bar graph showing the budget and expenses for a
        selected month.
        """
        #Para guardar los datos por mes.
        monthly_data = {
            'Months': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
            'Budget': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'Expenses': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
        
        # Cargar datos desde un archivo Excel
        months_expenses_list, total_rent, total_transport, total_entertainment, total_services, total_hygiene, total_insurances, total_debts, total_others = self.data_manager.load_data_expenses_from_excel('FILE.xlsx', 'Data')
        months_budget_list, budget_rent, budget_transport, budget_entertainment, budget_services, budget_hygiene, budget_insurances, budget_debts, budget_others = self.data_manager.load_data_budget_from_excel('FILE.xlsx', 'Data')
        
        
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
        selected_month = self.month_var.get()
        # Obtiene el índice del mes seleccionado.
        index = monthly_data['Months'].index(selected_month)

        # Oculta el marco actual.
        self.month_frame.grid_forget()

        # Crear un nuevo marco para la gráfica.
        self.graph_month_frame = tkk.Frame(self.root, padding="10")
        self.graph_month_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

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
        canvas_widget.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        #Botón para volver a la selección de mes.
        btn_return_months = tkk.Button(self.graph_month_frame, text="Back", command=self.return_to_month_menu, style='TButton')
        btn_return_months.grid(pady=10)
        
    #Método para volver a la selección de mes.    
    def return_to_month_menu(self):
        """
        The function returns to the month menu and updates the title of the root window.
        """
        self.month_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        if hasattr(self, 'graph_month_frame') and hasattr(self.graph_month_frame, 'destroy'):
            self.graph_month_frame.destroy()

        self.root.title("Month Dropdown Menu")
   
   
   