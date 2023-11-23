from tkinter import *
from PIL import ImageTk, Image
import sqlite3

# Ventana de interfaz
root = Tk()
root.title('Presupuesto') 
#root.iconbitmap()
root.geometry("400x400")

# Base de datos

# Conectar con base de datos o crearla
conn = sqlite3.connect('ingresos.db')

# Crear cursor
cursor = conn.cursor()

# Crear tabla
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ingresos (
        id INTEGER PRIMARY KEY,
        fecha DATE,
        salario REAL,
        comisiones REAL,
        ventas REAL,
        otros REAL
    )
''')

# Commit cambios
conn.commit()

# Cerrar conexión
conn.close()

# Iniciar loop de Tkinter
root.mainloop()