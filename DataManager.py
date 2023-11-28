import pandas as pd
class DataManager:
    def __init__(self):
        self.excel_data = None

    def load_data_incomes_from_excel(self, file, sheet):
        try:
            # Cargalos datos desde el archivo Excel en un DataFrame.
            df = pd.read_excel(file, sheet_name=sheet)
            
            # Se extraen listas de ingrasos y gastos del DataFrame.
            salary = df['Salario'].tolist()
            commissions = df['Comisiones'].tolist()
            sales = df['Ventas'].tolist()
            others = df['Otros'].tolist()
            
            # Retorna las listas extraídas.
            return salary, commissions, sales, others
        except Exception as e:
            print(f"Error loading data from Excel: {e}")
            
    def load_data_expenses_from_excel(self, file, sheet):
        try:
            # Cargalos datos desde el archivo Excel en un DataFrame.
            df = pd.read_excel(file, sheet_name=sheet)
            
            # Se extraen listas de ingrasos y gastos del DataFrame.
            rent = df['Domicilio'].tolist()
            transport = df['Transporte'].tolist()
            entertainment = df['Entretenimiento'].tolist()
            services = df['Servicios'].tolist()
            personal_hygiene = df['Higiene'].tolist()
            insurance = df['Seguros'].tolist()
            debts = df['Deudas'].tolist()
            others = df['Otros'].tolist()
            
            # Retorna las listas extraídas.
            return rent, transport, entertainment, services, personal_hygiene, insurance, debts, others 
        except Exception as e:
            print(f"Error loading data from Excel: {e}")
            
    def load_data_budget_from_excel(self, file, sheet):
        try:
            # Cargalos datos desde el archivo Excel en un DataFrame.
            df = pd.read_excel(file, sheet_name=sheet)
            
            # Se extraen listas de ingrasos y gastos del DataFrame.
            rent = df['Domicilio'].tolist()
            transport = df['Transporte'].tolist()
            entertainment = df['Entretenimiento'].tolist()
            services = df['Servicios'].tolist()
            personal_hygiene = df['Higiene'].tolist()
            insurance = df['Seguros'].tolist()
            debts = df['Deudas'].tolist()
            others = df['Otros'].tolist()
            
            # Retorna las listas extraídas.
            return rent, transport, entertainment, services, personal_hygiene, insurance, debts, others
        except Exception as e:
            print(f"Error loading data from Excel: {e}")
            
    