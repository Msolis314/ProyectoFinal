import tkinter as tk
from tkinter import ttk as tkk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from DataManager import DataManager

class AnnualGraph():
    
    def __init__(self, root, graphs_instance):
        self.root= root
        self.root.title("Annual Budget Graph Interface")
        self.month_var = tk.StringVar()
        self.data_manager = DataManager()
        self.graphs = graphs_instance
        self.months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        self.AnnualBudget_fig = None
    
    # Método para mostrar la gráfica de gastos y presupuesto anuales.
    def show_annual_graph(self):
        
        # Carga datos desde un archivo Excel
        salary, commissions, sales, others = self.data_manager.load_data_incomes_from_excel('FILE.xlsx', 'Data')
        rent, transport, entertainment, services, personal_hygiene, insurance, debts, others = self.data_manager.load_data_expenses_from_excel('FILE.xlsx', 'Data')
    
        
        # Calcular ingresos totales por mes.
        list_incomes = zip(salary, commissions, sales, others)
        monthly_incomes = [sum(tupla) for tupla in list_incomes]
        
        # Calcular gastos totales por mes.
        list_expenses = zip(rent, transport, entertainment, services, personal_hygiene, insurance, debts, others)
        monthly_expenses = [sum(tupla) for tupla in list_expenses]
        
        #Calcular ahorros mensuales.
        savings = []
        for elemento1, elemento2 in zip(monthly_incomes, monthly_expenses):
            savings.append(elemento1 - elemento2)
        
        # Oculta el marco actual.
        self.graphs.frame.grid_forget()

        # Crea un nuevo marco para la gráfica.
        self.graph_frame = tkk.Frame(self.root, padding="10")
        self.graph_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Crea una nueva figura y un eje para la gráfica de barras.
        fig = Figure(figsize=(8, 6), dpi=100)
        ax = fig.add_subplot(111)

        # Configura posiciones de las barras y sus dimensiones.
        bar_width = 0.35
        bar_positions_incomes = [i for i in range(len(self.months))]
        bar_positions_expenses = [i + bar_width for i in bar_positions_incomes]
        bar_positions_savings = [i + 2 * bar_width for i in bar_positions_incomes]

        # Agrega barras para los ingresos,los gastos y los ahorros.
        ax.bar(bar_positions_incomes, monthly_incomes, color='blue', width=bar_width, label='Incomes')
        ax.bar(bar_positions_expenses, monthly_expenses, color='orange', width=bar_width, label= 'Expenses')
        ax.bar(bar_positions_savings, savings, color='green', width=bar_width, label= 'Savings')
        ax.set_xticks([i + bar_width / 2 for i in bar_positions_expenses])
        ax.set_xticklabels(self.months)

        # Muestra leyenda.
        ax.legend(loc='lower right')

        # Agrega la gráfica al marco de la interfaz.
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.root.title("Bar Graph")

        # Botón para regresar a la interfaz principal.
        btn_return = tkk.Button(self.graph_frame, text="Back", command=self.graphs.return_to_main_interface, style='TButton')
        btn_return.grid(pady=10)
