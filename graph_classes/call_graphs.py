import customtkinter
from .DataManager import DataManager
from .IncomesPie import IncomesPie
from .ExpensePie import ExpensePie
from .MontlyBudget import MonthlyBudgetGraph
from .Annualgraph import AnnualGraph
from .Report import Report
from tablesetting.base_to_excel import data_to_excel
import os
class graph_choices:
    """Clase para llamar a los dintintos modulos que generan la grafica
    """
    def __init__(self,layout):
        """Constructura de la clase, necesita que se le pase el frame donde se quieren posicionar los graficos, llama al manejador de Datos

        :param layout: frame padre
        :type layout: CTkFrame
        """
        self.Data = DataManager()
        self.root = layout
    def call_income_budget(self,month,type_money:str):
        """Condicional para llamar a los graficos tipo pastel

        :param month: mes seleccionado
        :type month: _type_
        :param type_money: tipo de cambio
        :type type_money: str
        """
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
        """Clase para generar el grafico de presupuesto y expensas mensuales
        """
        data_to_excel('Gastos')
        data_to_excel('Presupuesto')
        pathb=f"basedata\Presupuesto.xlsx"
        pathg= f"basedata\Gastos.xlsx"

        montly_budget_instance = MonthlyBudgetGraph(self.root,pathb,pathg,'Sheet')
        montly_budget_instance.show_select_month()
    def call_anual_graph(self):
        """Clase para generar el grafico del historico anual
        """
        data_to_excel('Gastos')
        data_to_excel('Ingresos')
        pathg= f"basedata\Gastos.xlsx"
        pathi=f"basedata\Ingresos.xlsx"
        annual_graph_instance = AnnualGraph(self.root, pathg,pathi)
        annual_graph_instance.show_annual_graph()
    def call_report(self):
        """Clase para desplegar el reporte
        """
        data_to_excel('Gastos')
        data_to_excel('Presupuesto')
        pathb=f"basedata\Presupuesto.xlsx"
        pathg= f"basedata\Gastos.xlsx"
        report_instance = Report(self.root,pathg,pathb,'Sheet')
        report_instance.show_select_month()