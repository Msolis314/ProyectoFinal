import tkinter as tk
from tkinter import ttk as tkk
from DataManager import DataManager
from ExpensePie import ExpensePie
from IncomesPie  import IncomesPie
from MonthlyBudgetGraph import MonthlyBudgetGraph
from AnnualBudgetGraph import AnnualBudgetGraph

class Graphs:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Graph Interface")
        self.datamanager= DataManager()
        self.expense_pie = ExpensePie(self.root, self)
        self.month_var = tk.StringVar()
        self.incomes_pie = IncomesPie(self.root, self)
        self.monthly_budget = MonthlyBudgetGraph(self.root, self)
        self.annual_budget = AnnualBudgetGraph(self.root, self)
        self.create_main_frame()

    # Método para crear el marco principal de la interfaz gráfica
    def create_main_frame(self):
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
        self.btn_budget_graph = tkk.Button(self.frame, text="Annual Budget", command=self.annual_budget.show_annual_graph, style='TButton')
        self.btn_budget_graph.grid(pady=50, padx=400, row=3, column=0)
    
    # Método para volver a la interfaz principal desde otras pantallas.    
    def return_to_main_interface(self):
        self.frame.destroy()
        self.create_main_frame()
        self.root.title("Main Graph Interface")

# Punto de entrada principal,           
if __name__ == "__main__":
    root = tk.Tk()
    graphs_instance = Graphs(root)
    Data = DataManager()
    # Cargar datos desde un archivo Excel.
    salary, extra_income, annual_budget, annual_expense, savings, rent, transport, entertainment, services, micelane, feeding = Data.load_data_from_excel('FILE.xlsx', 'Data')
    
    #Instancias de las clases.
    expense_pie_instance = ExpensePie(root, graphs_instance)
    incomes_pie_instance = IncomesPie(root, graphs_instance)
    monthly_budget_instance = MonthlyBudgetGraph(root, graphs_instance)
    annual_budget_instance = AnnualBudgetGraph(root, graphs_instance)
    root.mainloop()
