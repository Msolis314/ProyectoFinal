import customtkinter
from .DataManager import DataManager
from .IncomesPie import IncomesPie
from .ExpensePie import ExpensePie
from tablesetting.base_to_excel import data_to_excel
import os
class graph_choices:
    def __init__(self,layout):
        self.Data = DataManager()
        self.root = layout
    def call_income_budget(self,month,type_money:str):
        path = f"basedata\{type_money}.xlsx"
        data_to_excel(type_money)
        if type_money == 'Ingresos':
            #months_incomes_list,total_salary, total_commissions, total_sales, total_others = self.Data.load_data_incomes_from_excel(path, 'Sheet')
            income_pie_instance = IncomesPie(self.root,month,type_money,path,'Sheet')
            income_pie_instance.show_select_month()

        if type_money == 'Gastos':
            expenses_pie_instance = ExpensePie(self.root,month,type_money,path,'Sheet')
            expenses_pie_instance.show_select_month()
    def call_montly_budget(self):
        data_to_excel('Gastos')
        data_to_excel('Presupuesto')
        pathb=f"basedata\Presupuesto.xlsx"
        pathg= f"basedata\Gastos.xlsx"