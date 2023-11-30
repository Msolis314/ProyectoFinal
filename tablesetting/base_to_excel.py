import sqlite3 , os , openpyxl
from sqlite3 import Error
import pandas as pd
conn = sqlite3.connect('Mari.db')  
cursor = conn.cursor()
book = openpyxl.Workbook()
sheet = book.active


consulta = "SELECT * FROM ingresos"
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
book.save("excel.xlsx")
conn.close()
