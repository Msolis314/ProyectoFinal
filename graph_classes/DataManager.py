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
            months = df['Months'].tolist()
            salary = df['Salario'].tolist()
            commissions = df['Comisiones'].tolist()
            sales = df['Ventas'].tolist()
            others = df['Otros'].tolist()
            
            data = {'Months': months, 'Salario': salary, 'Comisiones': commissions, 'Ventas': sales, 'Otros': others}
       
    
            # Crear un diccionario para almacenar los resultados agregados
            results = {}

            # Iterar sobre los datos
            for i in range(len(data['Months'])):
                month = data['Months'][i]
                salary = data['Salario'][i]
                commissions = data['Comisiones'][i]
                sales = data['Ventas'][i]
                others = data['Otros'][i]
                
                # Si el mes no está en el diccionario de resultados, agregarlo con los valores actuales
                if month not in results:
                    results[month] = {'Salario': salary, 'Comisiones': commissions, 'Ventas': sales, 'Otros': others}
                else:
                    # Si el mes ya está en el diccionario, sumar los valores actuales a los existentes
                    results[month]['Salario'] += salary
                    results[month]['Comisiones'] += commissions
                    results[month]['Ventas'] += sales
                    results[month]['Otros'] += others
            # Convertir los resultados a listas separadas
            months_incomes_list = list(results.keys())
            total_salary = [results[month]['Salario'] for month in months_incomes_list]
            total_commissions= [results[month]['Comisiones'] for month in months_incomes_list]
            total_sales = [results[month]['Ventas'] for month in months_incomes_list]
            total_others = [results[month]['Otros'] for month in months_incomes_list]
            
            # Retorna las listas extraídas.
            return months_incomes_list,total_salary, total_commissions, total_sales, total_others
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
            
            # Se extraen listas de ingresos y gastos del DataFrame.
            months = df['Meses'].tolist()
            rent = df['Domicilio'].tolist()
            transport = df['Transporte'].tolist()
            entertainment = df['Entretenimiento'].tolist()
            services = df['Servicios'].tolist()
            personal_hygiene = df['Higiene'].tolist()
            insurance = df['Seguros'].tolist()
            debts = df['Deudas'].tolist()
            others = df['Otros'].tolist()
            
            data = {'Meses': months, 'Domicilio': rent, 'Transporte': transport, 'Entretenimiento': entertainment, 'Servicios': services, 'Higiene': personal_hygiene, 'Seguros': insurance, 'Deudas': debts, 'Otros': others}
       
    
            # Crear un diccionario para almacenar los resultados agregados
            results = {}

            # Iterar sobre los datos
            for i in range(len(data['Meses'])):
                month = data['Meses'][i]
                rent = data['Domicilio'][i]
                transport = data['Transporte'][i]
                entertainment = data['Entretenimiento'][i]
                services = data['Servicios'][i]
                personal_hygiene = data['Higiene'][i]
                debts = data['Deudas'][i]
                insurance = data['Seguros'][i]
                others = data['Otros'][i]
                        
                # Si el mes no está en el diccionario de resultados, agregarlo con los valores actuales
                if month not in results:
                    results[month] = {'Domicilio': rent,'Transporte': transport,'Entretenimiento': entertainment,'Servicios': services, 'Higiene': personal_hygiene, 'Deudas': debts,'Seguros': insurance,'Otros': others}
                else:
                    # Si el mes ya está en el diccionario, sumar los valores actuales a los existentes
                    results[month]['Domicilio'] += rent
                    results[month]['Transporte'] += transport
                    results[month]['Entretenimiento'] += entertainment
                    results[month]['Servicios'] += services
                    results[month]['Higiene'] += personal_hygiene
                    results[month]['Deudas'] += debts
                    results[month]['Seguros'] += insurance
                    results[month]['Otros'] += others
                    
            # Convertir los resultados a listas separadas
            months_expenses_list = list(results.keys())
            total_rent = [results[month]['Domicilio'] for month in months_expenses_list]
            total_transport= [results[month]['Transporte'] for month in months_expenses_list]
            total_entertainment = [results[month]['Entretenimiento'] for month in months_expenses_list]
            total_services = [results[month]['Servicios'] for month in months_expenses_list]
            total_hygiene= [results[month]['Higiene'] for month in months_expenses_list]
            total_debts= [results[month]['Deudas'] for month in months_expenses_list]
            total_insurances= [results[month]['Seguros'] for month in months_expenses_list]
            total_others= [results[month]['Otros'] for month in months_expenses_list]
            
            # Retorna las listas extraídas.
            return months_expenses_list, total_rent, total_transport, total_entertainment, total_services, total_hygiene, total_insurances, total_debts, total_others 
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
            
            # Se extraen listas de presupuesto del DataFrame.
            months = df['Meses'].tolist()
            rent = df['Domicilio'].tolist()
            transport = df['Transporte'].tolist()
            entertainment = df['Entretenimiento'].tolist()
            services = df['Servicios'].tolist()
            personal_hygiene = df['Higiene'].tolist()
            insurance = df['Seguros'].tolist()
            debts = df['Deudas'].tolist()
            others = df['Otros'].tolist()
            
            data = {'Meses': months, 'Domicilio': rent, 'Transporte': transport, 'Entretenimiento': entertainment, 'Servicios': services, 'Higiene': personal_hygiene, 'Seguros': insurance, 'Deudas': debts, 'Otros': others}
       
    
            # Crear un diccionario para almacenar los resultados agregados
            results = {}

            # Iterar sobre los datos
            for i in range(len(data['Meses'])):
                month = data['Meses'][i]
                rent = data['Domicilio'][i]
                transport = data['Transporte'][i]
                entertainment = data['Entretenimiento'][i]
                services = data['Servicios'][i]
                personal_hygiene = data['Higiene'][i]
                debts = data['Deudas'][i]
                insurance = data['Seguros'][i]
                others = data['Otros'][i]
                        
                # Si el mes no está en el diccionario de resultados, agregarlo con los valores actuales
                if month not in results:
                    results[month] = {'Domicilio': rent,'Transporte': transport,'Entretenimiento': entertainment,'Servicios': services, 'Higiene': personal_hygiene, 'Deudas': debts,'Seguros': insurance,'Otros': others}
                else:
                    # Si el mes ya está en el diccionario, sumar los valores actuales a los existentes
                    results[month]['Domicilio'] += rent
                    results[month]['Transporte'] += transport
                    results[month]['Entretenimiento'] += entertainment
                    results[month]['Servicios'] += services
                    results[month]['Higiene'] += personal_hygiene
                    results[month]['Deudas'] += debts
                    results[month]['Seguros'] += insurance
                    results[month]['Otros'] += others
                    
            # Convertir los resultados a listas separadas
            months_budget_list = list(results.keys())
            budget_rent = [results[month]['Domicilio'] for month in months_budget_list]
            budget_transport= [results[month]['Transporte'] for month in months_budget_list]
            budget_entertainment = [results[month]['Entretenimiento'] for month in months_budget_list]
            budget_services = [results[month]['Servicios'] for month in months_budget_list]
            budget_hygiene= [results[month]['Higiene'] for month in months_budget_list]
            budget_debts= [results[month]['Deudas'] for month in months_budget_list]
            budget_insurances= [results[month]['Seguros'] for month in months_budget_list]
            budget_others= [results[month]['Otros'] for month in months_budget_list]
            
            # Retorna las listas extraídas.
            return months_budget_list, budget_rent, budget_transport, budget_entertainment, budget_services, budget_hygiene, budget_insurances, budget_debts, budget_others 
        except Exception as e:
            print(f"Error loading data from Excel: {e}")
            