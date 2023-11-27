import tkinter as tk
from tkinter import ttk as tkk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from DataManager import DataManager


class ExpensePie():
    
    def __init__(self, root, graphs_instance):
        self.root = root
        self.root.title("Expense Graph Interface")
        self.month_var = tk.StringVar() # Variable para almacenar el mes seleccionado.
        self.data_manager = DataManager()
        self.graphs = graphs_instance
        self.months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        self.expense_fig = None
        
    # Método para mostrar el menú desplegable de selección de mes.
    def show_select_month(self):
        
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
        
        # Obtiene el mes seleccionado.
        selected_month_name = self.month_var.get()
        
        # Obtiene el índice del mes seleccionado.
        selected_month_index = self.months.index(selected_month_name)
        
        #Carga datos del excel.
        salary, extra_income, annual_budget, annual_expense, savings, rent, transport, entertainment, services, micelane, feeding = self.data_manager.load_data_from_excel('FILE.xlsx', 'Data')
        
        # Filtrar los valores no nulos para las categorías de gastos del excel.
        list_savings = [value for value in savings if not pd.isna(value)]
        selected_savings = list_savings[selected_month_index]
        list_rent = [value for value in rent if not pd.isna(value)]
        selected_rent = list_rent[selected_month_index]
        list_transport = [value for value in transport if not pd.isna(value)]
        selected_transport = list_transport[selected_month_index]
        list_entertainment = [value for value in entertainment if not pd.isna(value)]
        selected_entertainment = list_entertainment[selected_month_index]
        list_services = [value for value in services if not pd.isna(value)]
        selected_services = list_services[selected_month_index]
        list_micelane = [value for value in micelane if not pd.isna(value)]
        selected_micelane = list_micelane[selected_month_index]
        list_feeding = [value for value in feeding if not pd.isna(value)]
        selected_feeding = list_feeding[selected_month_index]

        # Crea y muestra gráfica circular.
        self.graphs.frame.grid_forget()

        self.graph_frame = tkk.Frame(self.root, padding="10")
        self.graph_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        fig = Figure(figsize=(5, 5), dpi=100)
        ax = fig.add_subplot(111)

        # Crear la lista de categorias y la lista de gastos para la gráfica circular.
        categories = ['Savings', 'Rent', 'Transport', 'Entertainment', 'Services', 'Micelane', 'Feeding']
        data = [selected_savings, selected_rent, selected_transport, selected_entertainment, selected_services, selected_micelane, selected_feeding]

        pie_patches, texts, autotexts = ax.pie(data, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')

        ax.legend(pie_patches, categories, loc='lower right')

        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.root.title("Monthly Expense Graph")
        
        #Botón para volver a la selección de mes.
        btn_return = tkk.Button(self.graph_frame, text="Back", command=self.return_to_month_menu, style='TButton')
        btn_return.grid(pady=10)

    #Método para volver a la selección de mes.   
    def return_to_month_menu(self):
        self.month_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        if hasattr(self, 'graph_frame') and hasattr(self.graph_frame, 'destroy'):
            self.graph_frame.destroy()

        self.root.title("Month Dropdown Menu")