"""Modulo para pasar los datos a excel
"""
import sqlite3 , os , openpyxl
from sqlite3 import Error
import system_vars.config as config
import pandas as pd


def data_to_excel(nombre_tabla):
  """Funcion para cargar una tabla de la base de datos a un archivo excel 

  :param nombre_tabla: nombre de la tabla en la base de datos, ingresos, presupuesto o gastos
  :type nombre_tabla: str
  """
  current_database = f'{config.currentuser}.db'
  conn = sqlite3.connect(current_database)  
  cursor = conn.cursor()
  book = openpyxl.Workbook()
  sheet = book.active
  consulta = f"SELECT * FROM {nombre_tabla}"
  cursor.execute(consulta)
  results = cursor.fetchall()
  i = 0
  for row in results:
    i += 1
    j = 1
    for col in row:
      cell = sheet.cell(row = i, column = j)
      cell.value = col
      j += 1
  book.save(f"basedata\{nombre_tabla}.xlsx")
  conn.close()

def data_excel_save(nombre_tabla, path):
  """Funcion para guardar una tabla de la base de datos a un directorio de la computadore

  :param nombre_tabla: nombre de la tabla puede ser ingresos, presupuesto o gastos
  :type nombre_tabla: str
  :param path: path donde se desea guardas
  :type path: str
  """
  current_database = f'{config.currentuser}.db'
  conn = sqlite3.connect(current_database)  
  cursor = conn.cursor()
  book = openpyxl.Workbook()
  sheet = book.active
  consulta = f"SELECT * FROM {nombre_tabla}"
  cursor.execute(consulta)
  results = cursor.fetchall()
  i = 0
  for row in results:
    i += 1
    j = 1
    for col in row:
      cell = sheet.cell(row = i, column = j)
      cell.value = col
      j += 1
  path = f'{path}/{nombre_tabla}.xlsx'
  book.save(path)
  conn.close()
