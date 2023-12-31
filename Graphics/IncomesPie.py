import tkinter as tk
from tkinter import ttk as tkk
import customtkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from .DataManager import DataManager


class IncomesPie():
    
    def __init__(self, root,month):
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
        self.month_var = month # Variable para almacenar el mes seleccionado.
        self.data_manager = DataManager()
        self.incomes_fig = None
        
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
        btn_show_graph = tkk.Button(self.month_frame, text="Show Graph", command=self.show_income_graph)
        btn_show_graph.grid(pady=10)

        # Botón para regresar a la interfaz principal.
        btn_return = tkk.Button(self.month_frame, text="Back", command=self.graphs.return_to_main_interface, style='TButton')
        btn_return.grid(pady=10)
        
    # Método para mostrar la gráfica de ingresos.
    def show_income_graph(self,path,sheet):
        """
        The function `show_income_graph` displays a pie chart of income categories based on the selected
        month's data from an Excel file.
        """
        
        # Obtiene el mes seleccionado.
        selected_month_name = self.month_var
        
        # Obtiene el índice del mes seleccionado.
        #selected_month_index = self.months.index(selected_month_name)
        
        #Carga datos del excel.
        months_incomes_list, total_salary, total_commissions, total_sales, total_others = self.data_manager.load_data_incomes_from_excel(path, sheet)
        
        # Obtiene el índice del mes seleccionado.
        selected_month_index = months_incomes_list.index(selected_month_name)
        
        # Filtrar los valores no nulos para las categorías de ingresos.
        selected_salary = total_salary[selected_month_index]
        selected_commissions = total_commissions[selected_month_index]
        selected_sales = total_sales[selected_month_index]
        selected_others = total_others[selected_month_index]
        
        # Crea y muestra gráfica circular.
        #self.graphs.frame.grid_forget()

        self.graph_frame = customtkinter.CTkFrame(self.root, padding="10")
        self.graph_frame.grid(row=0, column=0, sticky='nsew')

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

        #self.root.title("Monthly Income Graph")

        #Botón para volver a la selección de mes.
        #btn_return = tkk.Button(self.graph_frame, text="Back", command=self.return_to_month_menu, style='TButton')
        #btn_return.grid(pady=10)

    #Método para volver a la selección de mes.
    def return_to_month_menu(self):
        """
        The function returns to the month menu and updates the title of the root window.
        """
        self.month_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        if hasattr(self, 'graph_frame') and hasattr(self.graph_frame, 'destroy'):
            self.graph_frame.destroy()

        self.root.title("Month Dropdown Menu")










