import tkinter as tk
from tkinter import ttk as tkk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from DataManager import DataManager

class AnnualBudgetGraph():
    
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
        salary, extra_income, annual_budget, annual_expense, savings, rent, transport, entertainment, services, micelane, feeding = self.data_manager.load_data_from_excel('FILE.xlsx', 'Data')
        annual_budget = [value for value in annual_budget if not pd.isna(value)]
        annual_expense = [value for value in annual_expense if not pd.isna(value)]
        
        # Oculta el marco actual.
        self.graphs.frame.grid_forget()

        # Crea un nuevo marco para la gráfica.
        self.graph_frame = tkk.Frame(self.root, padding="10")
        self.graph_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Crea una nueva figura y un eje para la gráfica de barras.
        fig = Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)

        # Configura posiciones de las barras y sus dimensiones.
        bar_width = 0.35
        bar_positions_budget = [i for i in range(len(self.months))]
        bar_positions_expenses = [i + bar_width for i in bar_positions_budget]

        # Agrega barras para el presupuesto y los gastos.
        ax.bar(bar_positions_budget, annual_budget, color='blue', width=bar_width, label='Budget')
        ax.bar(bar_positions_expenses, annual_expense, color='orange', width=bar_width, label= 'Expenses')
        ax.set_xticks([i + bar_width / 2 for i in bar_positions_budget])
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
