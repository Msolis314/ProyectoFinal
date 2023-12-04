import tkinter as tk
from tkinter import ttk as tkk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from DataManager import DataManager

# The AnnualGraph class is a Python class that creates a graphical interface for displaying an annual
# budget graph.
class AnnualGraph():
    
    def __init__(self, root, graphs_instance):
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
        self.root.title("Annual Budget Graph Interface")
        self.month_var = tk.StringVar()
        self.data_manager = DataManager()
        self.graphs = graphs_instance
        self.AnnualBudget_fig = None
    
    # Método para mostrar la gráfica de gastos y presupuesto anuales.
    def show_annual_graph(self):
        
        #Para guardar los datos por mes.
        annual_data = {
            'Months': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
            'Expenses': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'Incomes': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'Savings': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
        
        # Carga datos desde un archivo Excel
        months_incomes_list, total_salary, total_commissions, total_sales, total_others = self.data_manager.load_data_incomes_from_excel('FILE.xlsx', 'Data')
        months_expenses_list, total_rent, total_transport, total_entertainment, total_services, total_hygiene, total_insurances, total_debts, total_others_expenses = self.data_manager.load_data_expenses_from_excel('FILE.xlsx', 'Data')

        
        # Calcular ingresos totales por mes.
        list_incomes = zip(total_salary, total_commissions, total_sales, total_others)
        monthly_incomes = [sum(tupla) for tupla in list_incomes]
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
        self.graphs.frame.grid_forget()

        # Crea un nuevo marco para la gráfica
        self.graph_frame = tkk.Frame(self.root, padding="10")
        self.graph_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

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
        ax.set_xticklabels(self.months)

        # Muestra leyenda
        ax.legend(loc='lower right')

        # Agrega la gráfica al marco de la interfaz
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.root.title("Bar Graph")

        # Botón para regresar a la interfaz principal
        btn_return = tkk.Button(self.graph_frame, text="Back", command=self.graphs.return_to_main_interface, style='TButton')
        btn_return.grid(pady=10)
