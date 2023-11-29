import pandas as pd
# The DataManager class provides methods to load data from an Excel file into separate lists
# representing different income and expense categories.
class DataManager:
    def __init__(self):
        """
        The function initializes a variable called "excel_data" with a value of None.
        """
        self.excel_data = None

    def load_data_incomes_from_excel(self, file, sheet):
        """
        The function `load_data_incomes_from_excel` loads data from an Excel file into a DataFrame and
        extracts lists of income categories from the DataFrame.
        
        :param file: The "file" parameter is the path or name of the Excel file from which you want to
        load the data. It can be a string representing the file path or just the file name if the file
        is in the same directory as your code
        :param sheet: The "sheet" parameter refers to the name of the sheet within the Excel file from
        which you want to load the data
        :return: four lists: salary, commissions, sales, and others.
        """
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
        """
        The function `load_data_expenses_from_excel` loads data from an Excel file into separate lists
        representing different expense categories.
        
        :param file: The "file" parameter represents the path or name of the Excel file from which you
        want to load the data
        :param sheet: The "sheet" parameter is the name of the sheet in the Excel file from which you
        want to load the data
        :return: multiple lists: rent, transport, entertainment, services, personal_hygiene, insurance,
        debts, and others.
        """
        try:
            # Carga los datos desde el archivo Excel en un DataFrame.
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
        """
        The function `load_data_budget_from_excel` loads data from an Excel file into separate lists
        representing different categories of expenses.
        
        :param file: The "file" parameter is the path or name of the Excel file from which you want to
        load the data. It can be a string representing the file path or name
        :param sheet: The "sheet" parameter is the name or index of the sheet in the Excel file from
        which you want to load the data. It specifies which sheet's data should be read into the
        DataFrame
        :return: multiple lists: rent, transport, entertainment, services, personal_hygiene, insurance,
        debts, and others.
        """
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
            
    