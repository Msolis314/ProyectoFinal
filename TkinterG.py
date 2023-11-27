import tkinter as tk
from tkinter import ttk as tkk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

class Aplicacion:
    def __init__(self, root):
        # Configuración de la ventana principal
        self.root = root
        self.root.title("Interfaz Principal")

        # Configurar el estilo para cambiar el color de fondo
        style = tkk.Style()
        style.configure('TFrame', background='gray')
        style.configure('TButton', foreground='gray10', background='black')

        # Creación del frame principal
        self.frame = tkk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configurar para que la celda se expanda al maximizar la ventana
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Centrar los botones vertical y horizontalmente
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        # Crear un frame adicional para centrar los botones
        frame_central = tkk.Frame(self.frame, style='TFrame')
        frame_central.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)

        # Botones para mostrar diferentes gráficas
        self.btn_grafica1 = tkk.Button(self.frame, text="Gastos mensuales", command=self.mostrar_grafica_gastos, style='TButton')
        self.btn_grafica1.grid(pady=50, padx=400, row=0, column=0)

        self.btn_grafica2 = tkk.Button(self.frame, text="Ingresos", command=self.mostrar_grafica_ingresos, style='TButton')
        self.btn_grafica2.grid(pady=25, padx=400, row=1, column=0)

        self.btn_grafica_barras = tkk.Button(self.frame, text="Presupuesto", command=self.mostrar_grafica_presupuesto(ARCHIVO.xlsx), style='TButton')
        self.btn_grafica_barras.grid(pady=50, padx=400, row=2, column=0)

        # Botón de retroceso
        btn_atras = tkk.Button(self.frame, text="Atrás", command=self.volver_interfaz_principal, style='TButton')
        btn_atras.grid(pady=50, padx=400, row=3, column=0)

    def mostrar_grafica_gastos(self):
        # Función para mostrar la primera gráfica circular
        self.mostrar_grafica_circular("Gráfica gastos mensuales", [5000, 87500, 20000, 24500, 80000, 15000, 18000], ["Ahorros", "Vivienda", "Servicios", "Micelaneos", "Alimentación", "Transporte", "Entretenimiento"])

    def mostrar_grafica_ingresos(self):
        # Función para mostrar la segunda gráfica circular
        self.mostrar_grafica_circular("Gráfica ingresos", [250000, 40000], ["Salario", "Extras"])

    def mostrar_grafica_circular(self, title, data, category):
        # Ocultar la interfaz principal
        self.frame.grid_forget()

        # Crear la nueva interfaz con la gráfica circular
        self.frame_grafica = tkk.Frame(self.root, padding="10")
        self.frame_grafica.pack(expand=True, fill=tk.BOTH)  # Utilizar pack para ocupar todo el espacio

        # Crear la gráfica circular
        fig = Figure(figsize=(5, 5), dpi=100)
        ax = fig.add_subplot(111)
        ax.pie(data, labels=category, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')

        canvas = FigureCanvasTkAgg(fig, master=self.frame_grafica)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(expand=True, fill=tk.BOTH)

        # Configurar el título de la ventana
        self.root.title(title)

        # Botón de retroceso
        btn_retroceso = tkk.Button(self.frame_grafica, text="Volver", command=self.volver_interfaz_principal, style='TButton')
        btn_retroceso.pack(pady=10)

    def mostrar_grafica_presupuesto(self, archivo_excel):
        # Función para mostrar la gráfica de barras
        # Ocultar la interfaz principal
        self.frame.grid_forget()
        
        # Leer datos desde el archivo de Excel
        df = pd.read_excel(ARCHIVO.xlsx)

        # Crear la nueva interfaz con la gráfica de barras
        self.frame_grafica = tkk.Frame(self.root, padding="10")
        self.frame_grafica.pack(expand=True, fill=tk.BOTH)  # Utilizar pack para ocupar todo el espacio
         # Obtener datos para la gráfica de barras
        meses = df['Mes'].tolist()  # Asumiendo que tienes una columna llamada 'Mes' en tu archivo Excel
        budget = df['Presupuesto'].tolist()  # Asumiendo que tienes una columna llamada 'Presupuesto'
        expenses = df['Gastos'].tolist()  # Asumiendo que tienes una columna llamada 'Gastos'

       # Crear la gráfica de barras
        fig = Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)

        # Ancho de cada barra
        bar_width = 0.35

        # Configurar posiciones para las barras de presupuesto y gastos
        bar_positions_budget = [i for i in range(len(meses))]
        bar_positions_expenses = [i + bar_width for i in bar_positions_budget]

        # Crear barras de presupuesto
        ax.bar(bar_positions_budget, budget, color='blue', width=bar_width, label='Presupuesto')

        # Crear barras de gastos
        ax.bar(bar_positions_expenses, expenses, color='orange', width=bar_width, label='Gastos')

        # Configurar etiquetas y leyenda
        ax.set_xticks([i + bar_width / 2 for i in bar_positions_budget])
        ax.set_xticklabels(meses)
        ax.legend()

        canvas = FigureCanvasTkAgg(fig, master=self.frame_grafica)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(expand=True, fill=tk.BOTH)

        # Configurar el título de la ventana
        self.root.title("Gráfica de Barras")

        # Botón de retroceso
        btn_retroceso = tkk.Button(self.frame_grafica, text="Volver", command=self.volver_interfaz_principal, style='TButton')
        btn_retroceso.pack(pady=10)

    def volver_interfaz_principal(self):
        # Función para volver a la interfaz principal
        # Verificar si la interfaz con la gráfica existe
        if hasattr(self, 'frame_grafica') and hasattr(self.frame_grafica, 'destroy'):
            # Destruir la interfaz con la gráfica
            self.frame_grafica.destroy()
        # Volver a mostrar la interfaz principal
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        # Restaurar el título de la ventana principal
        self.root.title("Interfaz Principal")

if __name__ == "__main__":
    # Crear la aplicación
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
