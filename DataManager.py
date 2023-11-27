import pandas as pd
class DataManager:
    def __init__(self):
        self.excel_data = None

    def load_data_from_excel(self, file, sheet):
        try:
            # Cargalos datos desde el archivo Excel en un DataFrame.
            df = pd.read_excel(file, sheet_name=sheet)
            
            # Se extraen listas de ingrasos y gastos del DataFrame.
            salary = df['Salary'].tolist()
            extra_income = df['Extra Income'].tolist()
            savings = df['Savings'].tolist()
            rent = df['Rent'].tolist()
            transport = df['Transport'].tolist()
            entertainment = df['Entertainment'].tolist()
            services = df['Services'].tolist()
            micelane = df['Micelane'].tolist()
            feeding = df['Feeding'].tolist()
            annual_budget = df['Annual Budget'].tolist()
            annual_expense = df['Annual Expense'].tolist()
            
            # Retorna las listas extraídas.
            return salary, extra_income, annual_budget, annual_expense, savings, rent, transport, entertainment, services, micelane, feeding
        except Exception as e:
            print(f"Error loading data from Excel: {e}")
    