import tkinter as tk
from tkinter import ttk as tkk
import customtkinter
from CTkMessagebox import CTkMessagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from .DataManager import DataManager
from entry_classes.template import TopCalendar
from tools.Usos import *
from system_vars.Vars import *
from tablesetting.base_to_excel import data_to_excel
import system_vars.config as config


class ExpensePie():
    
    def __init__(self, root,month,respuesta,path,sheet):
        """
        TThe `ExpensePie` class creates a GUI interface for displaying a pie chart of monthly expenses based
    on selected month and data from an Excel file.
    
        :param root: The "root" parameter is the main window or the root window of the application. It is
        the top-level window that contains all other widgets and elements of the user interface
        :param graphs_instance: The `graphs_instance` parameter is an instance of a class that contains
        methods for creating and updating graphs. It is used to access the graph-related functionality in
        the code
        """
        self.root = root
        self.respuesta = respuesta
        self.topCalendar = None
        self.month_var = None # Variable para almacenar el mes seleccionado.
        self.data_manager = DataManager()
        self.incomes_fig = None
        self.path = path
        self.sheet = sheet

        
    # Método para mostrar el menú desplegable de selección de mes.    
    def show_select_month(self):
        """
        The function creates a dropdown menu for selecting a month and includes buttons for showing a
        graph and returning to the main interface.
        """
        self.month_frame = customtkinter.CTkFrame(self.root,fg_color='transparent')
        self.month_frame.grid(row=0,column=0)
        # Ocultar el marco de la interfaz principal, si está visible.
        self.option_menu_var= customtkinter.StringVar(value="Enero")
        self.option_calendar=customtkinter.CTkOptionMenu(self.month_frame, 
                                                         values=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"],
                                                         width=50,
                                                         height=50,
                                                         corner_radius=4,
                                                         dropdown_hover_color=HOVER_COLOR,
                                                         font=set_font(),dropdown_font=set_font('Shanti'),
                                                         variable=self.option_menu_var)
        self.option_calendar.pack(fill=tk.BOTH,expand=True,pady=20)
        self.buttom_display = customtkinter.CTkButton(self.month_frame, text="Generar grafico",font=set_font(),command=self.update_date,fg_color=BUTTOM_HOVER)
        self.buttom_display.pack(fill= tk.BOTH,side=tk.BOTTOM, expand=True)
        
    # Método para mostrar la gráfica de ingresos.
    def show_expense_graph(self,path,sheet):
        """
        The function `show_expense_graph` displays a pie chart of monthly expenses based on selected
        month and data from an Excel file.
        """
        self.month_frame.pack_forget()
        self.month_frame.grid_forget()
        # Obtiene el mes seleccionado.
        selected_month_name = self.month_var
        if selected_month_name != None:
            
            
            # Obtiene el índice del mes seleccionado.
            #selected_month_index = self.months.index(selected_month_name)
            
            #Carga datos del excel.
            try:
                months_expenses_list, total_rent, total_transport, total_entertainment, total_services, total_hygiene, total_insurances, total_debts, total_others = self.data_manager.load_data_expenses_from_excel(path, sheet)
            except:
                data_to_excel(self.respuesta)
                months_expenses_list, total_rent, total_transport, total_entertainment, total_services, total_hygiene, total_insurances, total_debts, total_others = self.data_manager.load_data_expenses_from_excel(path, sheet)
            # Obtiene el índice del mes seleccionado.
            try:
                selected_month_index = months_expenses_list.index(selected_month_name)
            except:
                CTkMessagebox(title="Error",message="Datos insuficientes para el mes")
                self.return_to_month_menu()
                os.remove(path)
                raise Exception

            
            
            # Filtrar los valores para las categorías de gastos.
            selected_rent = total_rent[selected_month_index]
            selected_transport = total_transport[selected_month_index]
            selected_entertainment = total_entertainment[selected_month_index]
            selected_services = total_services[selected_month_index]
            selected_personal_hygiene = total_hygiene[selected_month_index]
            selected_insurance = total_insurances[selected_month_index]
            selected_debts = total_debts[selected_month_index]
            selected_others = total_others[selected_month_index]
            
            # Crea y muestra gráfica circular.
            #self.graphs.frame.grid_forget()
            print(self.root)

            self.graph_frame = customtkinter.CTkFrame(self.root,fg_color='transparent')
            self.graph_frame.grid_rowconfigure(0,weight=1)
            self.graph_frame.grid_columnconfigure(0,weight=1)
            self.graph_frame.grid_columnconfigure(2,weight=1)
            self.graph_frame.grid(row=0, column=0, sticky='nsew')
            title = f'Gráfico Pastel {selected_month_name}'
            self.titleLabel = customtkinter.CTkLabel(self.graph_frame,text=title,font=set_font(tam=15))
            self.titleLabel.grid(row=0,column=1,pady=5)

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
            canvas_widget.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))

            os.remove(path)

            #self.root.title("Monthly Income Graph")

            #Botón para volver a la selección de mes.
            btn_return = customtkinter.CTkButton(self.graph_frame, text="Volver",font=set_font(), command=self.return_to_month_menu)
            btn_return.grid(row=2, column=1,pady=5)
        else:
            CTkMessagebox(title="Error",message="Debe elegir un mes",icon='cancel')
        #Método para volver a la selección de mes.
    def return_to_month_menu(self):
        """
        The function returns to the month menu and updates the title of the root window.
        """
        self.show_select_month()

        if hasattr(self, 'graph_frame') and hasattr(self.graph_frame, 'destroy'):
            self.graph_frame.destroy()

        
    def update_date(self):
        self.month_var=self.option_menu_var.get()
        print(self.path)
        self.show_expense_graph(self.path,'Sheet')