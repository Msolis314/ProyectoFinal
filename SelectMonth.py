import tkinter as tk
from tkinter import ttk as tkk

class SelctMonth:
    
    def __init__(self, root, graphs_instance):
        self.root = root
        self.root.title("Monthly Budget Graph Interface")
        self.month_var = tk.StringVar() # Variable para almacenar el mes seleccionado.
        self.graphs = graphs_instance
        self.months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        self.MonthlyBudget_fig = None
    
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
        btn_show_graph = tkk.Button(self.month_frame, text="Show Graph", command=self.show_month_graph)
        btn_show_graph.grid(pady=10)

        # Botón para regresar a la interfaz principal.
        btn_return = tkk.Button(self.month_frame, text="Back", command=self.graphs.return_to_main_interface, style='TButton')
        btn_return.grid(pady=10)