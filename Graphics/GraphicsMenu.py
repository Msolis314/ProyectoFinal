import tkinter as tk
import customtkinter
from tkinter import ttk as tkk
from DataManager import DataManager
from ExpensePie import ExpensePie
from IncomesPie  import IncomesPie
from MonthlyBudgetGraph import MonthlyBudgetGraph
from AnnualGraph import AnnualGraph

# The `Graphs` class is a main graph interface that creates instances of various graph components and
# provides buttons to display different types of graphs.
class Graphs:
    def __init__(self, root):
        """
        The function initializes the main graph interface and creates instances of various graph
        components.
        
        :param root: The "root" parameter is the main window or the root window of the application. It
        is the top-level window that contains all other widgets and elements of the user interface
        """
        self.root = root
        self.root.title("Main Graph Interface")
        self.datamanager= DataManager()
        self.expense_pie = ExpensePie(self.root, self)
        self.month_var = tk.StringVar()
        self.incomes_pie = IncomesPie(self.root, self)
        self.monthly_budget = MonthlyBudgetGraph(self.root, self)
        self.annual_graph = AnnualGraph(self.root, self)
        self.create_main_frame()

    # Método para crear el marco principal de la interfaz gráfica
    def create_main_frame(self):
        """
        The function creates the main frame of a GUI application and adds buttons for displaying
        different types of graphs.
        """
        frame = tkk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.frame = frame
        
        style = tkk.Style()
        style.configure('TButton', foreground='gray10', background='black')

        central_frame = tkk.Frame(self.frame, style='TFrame')
        central_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)

        #Botón para ver gráfica circular de gastos por mes.
        self.btn_expense_graph = tkk.Button(self.frame, text="Monthly Expenses", command=self.expense_pie.show_select_month, style='TButton')
        self.btn_expense_graph.grid(pady=50, padx=400, row=0, column=0)

        #Botón para ver gráfica circular de ingresos por mes.
        self.btn_income_graph = tkk.Button(self.frame, text="Monthly Incomes", command=self.incomes_pie.show_select_month, style='TButton')
        self.btn_income_graph.grid(pady=25, padx=400, row=1, column=0)
        
        #Botón para ver gráfica de gastos y presupuesto mensuales.
        self.btn_monthly_budget_graph = tkk.Button(self.frame, text="Monthly Budget", command=self.monthly_budget.show_select_month, style='TButton')
        self.btn_monthly_budget_graph.grid(pady=50, padx=400, row=2, column=0)

        #Botón para ver gráfica de gastos y presupuesto anuales.
        self.btn_budget_graph = tkk.Button(self.frame, text="Annual Graph", command=self.annual_graph.show_annual_graph, style='TButton')
        self.btn_budget_graph.grid(pady=50, padx=400, row=3, column=0)
    
    # Método para volver a la interfaz principal desde otras pantallas.    
    def return_to_main_interface(self):
        """
        The function returns to the main interface by destroying the current frame, creating a new main
        frame, and updating the title of the root window.
        """
        self.frame.destroy()
        self.create_main_frame()
        self.root.title("Main Graph Interface")

# Punto de entrada principal,           
# The code block `if __name__ == "__main__":` is a common Python idiom that allows a module to be run
# as a standalone script or imported by other modules.
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    graphs_instance = Graphs(root)
    Data = DataManager()
    # Cargar datos desde un archivo Excel.
    months_incomes_list,total_salary, total_commissions, total_sales, total_others = Data.load_data_incomes_from_excel('FILE.xlsx', 'Data')
    months_expenses_list, total_rent, total_transport, total_entertainment, total_services, total_hygiene, total_insurances, total_debts, total_others = Data.load_data_expenses_from_excel('FILE.xlsx', 'Data')
    months_budget_list, budget_rent, budget_transport, budget_entertainment, budget_services, budget_hygiene, budget_insurances, budget_debts, budget_others = Data.load_data_budget_from_excel('FILE.xlsx', 'Data')
    #Instancias de las clases.
    expense_pie_instance = ExpensePie(root, graphs_instance)
    incomes_pie_instance = IncomesPie(root, graphs_instance)
    monthly_budget_instance = MonthlyBudgetGraph(root, graphs_instance)
    annual_budget_instance = AnnualGraph(root, graphs_instance)
    root.mainloop()
