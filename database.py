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

cursor.execute("""
    CREATE TABLE IF NOT EXISTS ingresos (
        fecha DATE,
        salario REAL,
        comisiones REAL,
        ventas REAL,
        otros REAL
    )
""")


# Crear función submit para la database
def submit():
    # Conectar con base de datos o crearla
    conn = sqlite3.connect('ingresos.db')
    # Crear cursor
    cursor = conn.cursor()

    # Insertar en la tabla
    cursor.execute("INSERT INTO ingresos VALUES (:fecha, :salario, :comisiones, :ventas, :otros)",
        {
            'fecha': fecha.get(),
            'salario': salario.get(),
            'comisiones': comisiones.get(),
            'ventas': ventas.get(),
            'otros': otros.get()
        }
    )

    # Commit cambios
    conn.commit()
    # Cerrar conexión
    conn.close()

    # Limpiar text boxes
    fecha.delete(0, END)
    salario.delete(0, END)
    comisiones.delete(0, END)
    ventas.delete(0, END)
    otros.delete(0, END)

# Crear función query
def query():
    # Conectar con base de datos o crearla
    conn = sqlite3.connect('ingresos.db')
    # Crear cursor
    cursor = conn.cursor()

    # Query database
    cursor.execute("SELECT *, oid FROM ingresos")
    records = cursor.fetchall()
    print(records)

    # Loop a través de los resultados
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=7, column=0, columnspan=2)

    # Commit cambios
    conn.commit()
    # Cerrar conexión
    conn.close()

# Crear text boxes
fecha = Entry(root, width=30)
fecha.grid(row=0, column=1)
salario = Entry(root, width=30)
salario.grid(row=1, column=1)
comisiones = Entry(root, width=30)
comisiones.grid(row=2, column=1)
ventas = Entry(root, width=30)
ventas.grid(row=3, column=1)
otros = Entry(root, width=30)
otros.grid(row=4, column=1)

# Crear text box labels
fecha_label = Label(root, text="Fecha")
fecha_label.grid(row=0, column=0)
salario_label = Label(root, text="Salario")
salario_label.grid(row=1, column=0)
comisiones_label = Label(root, text="Comisiones")
comisiones_label.grid(row=2, column=0)
ventas_label = Label(root, text="Ventas")
ventas_label.grid(row=3, column=0)
otros_label = Label(root, text="Otros")
otros_label.grid(row=4, column=0)

# Crear submit button
submit_btn = Button(root, text="Guardar ingresos", command=submit)
submit_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Crear query button
query_btn = Button(root, text="Mostrar valores", command=query)
query_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Commit cambios
conn.commit()

# Cerrar conexión
conn.close()

# Iniciar loop de Tkinter
root.mainloop()