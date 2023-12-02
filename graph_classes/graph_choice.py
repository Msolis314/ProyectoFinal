"""Módulo para desplegar las opciones de elección para el gráfico"""
import customtkinter
import tkinter as tk
from tools.Usos import *
from system_vars.Vars import *
from tablesetting.base_to_excel import data_to_excel
import system_vars.config as config
from entry_classes.template import TopCalendar
from CTkMessagebox import CTkMessagebox
class GraphChoice:
    """Clase para el display de las opciones de graficos

    :param title_frame: frame donde se posiciona el titulo
    :type titile_frame: CTkFrame
    :param title_label: titulo de la seccion
    :type titile_label: CTkLabel 
    :param botton_frame: Frame donde se ponen los widgets de los botones de opciones graficos
    :type botton_frame: CTkFrame
    :param _date: Mes donde se quiere graficar
    :type _date: str
    :param topCalendar: instancia de la ventana Calendar
    :type topCalendar: TopCalendar
    :param pay_graph_bottom: Boton del grafico tipo pastel
    :type pay_graph_bottom: CTkBottom
    :param bar_graph_bottom: Boton del grafico tipo barras por mes
    :type bar_graph_bottom: CTkBottom
    :param year_graph_bottom: Boton del grafico tipo barras anual
    :type year_graph_bottom: CTkBottom
    :param report_bottom: Boton del informe 
    :type report_bottom: CTkBottom
    """
    def __init__(self,layout):
        self.title_frame= customtkinter.CTkFrame(layout, height=200,fg_color=FG_COLOR)
        self.title_frame.pack(fill='both',side=tk.TOP,pady=35)
        self.title_label = customtkinter.CTkLabel(self.title_frame, text= "Opciones de graficación",font=set_font('Cascadia mono SemiBold', 24))
        self.title_label.pack()


        self.botton_frame = customtkinter.CTkFrame(layout,fg_color=FG_COLOR)
        self.botton_frame.pack(fill='both',expand=True,side=tk.BOTTOM)
        self.botton_frame.grid_columnconfigure(0,weight=1)
        self.botton_frame.grid_columnconfigure(4,weight=1)
        self.botton_frame.grid_rowconfigure(0,weight=1)
        self.botton_frame.grid_rowconfigure(3,weight=1)
        self._graph_choice=None

        image_pay = reader_image(Path_Image,"graficoPay.png",(50,50))
        self.pay_graph_buttom = customtkinter.CTkButton(self.botton_frame,width=70,text='      Gráfico Pastel      ',
                                                        font=set_font(),fg_color=BORDER_COLOR, border_color=BORDER_COLOR,
                                                        corner_radius=10, 
                                                        image=image_pay,compound='top',hover_color=HOVER_COLOR,
                                                        command=self.pay_buttom_callback)
        self.pay_graph_buttom.grid(row=1, column=1,pady=20,padx=20)
        self.topCalendar= None
        self._date=None
        image_bar = reader_image(Path_Image,"graficoBarras1.png",(50,50))
        self.bar_graph_buttom = customtkinter.CTkButton(self.botton_frame,width=40,text='Gráfico de Barras por mes',
                                                        font=set_font(),fg_color=BORDER_COLOR, border_color=BORDER_COLOR,
                                                        corner_radius=10, 
                                                        image=image_bar,compound='top',hover_color=HOVER_COLOR,
                                                        command=self.bar_buttom_callback)
        self.bar_graph_buttom.grid(row=1, column=2,pady=20,padx=20)
        image_year= reader_image(Path_Image,"analitica.png",(50,50))
        self.year_graph_buttom = customtkinter.CTkButton(self.botton_frame,width=70,text='      Gráfico anual     ',
                                                        font=set_font(),fg_color=BORDER_COLOR, border_color=BORDER_COLOR,
                                                        corner_radius=10, 
                                                        image=image_year,compound='top',hover_color=HOVER_COLOR,
                                                        command=self.year_buttom_callback)
        self.year_graph_buttom.grid(row=2, column=1,pady=20,padx=20)
        image_report=reader_image(Path_Image,"reporte.png",(50,50))
        self.report_buttom = customtkinter.CTkButton(self.botton_frame,width=70,text='     Reporte Mensual     ',
                                                        font=set_font(),fg_color=BORDER_COLOR, border_color=BORDER_COLOR,
                                                        corner_radius=10,hover_color=HOVER_COLOR, 
                                                        image=image_report,compound='top',
                                                        command=self.reporte_buttom_callback)
        self.report_buttom.grid(row=2, column=2,pady=20,padx=20)


    def pay_buttom_callback(self):
        """Funcion para abrir una ventana de mensaje si se presiona el pie chart
        ....
        :return: Setea el atributo _graph_choice con la eleccion del grafico , si es de gastos o ingresos y el mes
        :rtype: tupla
        """
        msg = CTkMessagebox(title="Info",message="Genera un gráfico tipo pastel de los gastos o ingresos. Elija alguna de las siguientes opciones",
                            icon="question",option_1="Cancelar",option_2="Gastos",option_3="Ingresos")
        respuesta= msg.get()
        choices = ["Gastos","Ingresos"]
        if respuesta != "Cancelar" and respuesta in choices:
            if self.topCalendar is None or not self.topCalendar.winfo_exists():
                self.topCalendar = TopCalendar(self.update_date,config.app)  # create window if its None or destroyed
                self.topCalendar.wm_transient(config.app)
            else:
                self.topCalendar.focus()  # if window exists focus it
        self._graph_choice=("Pie",respuesta,self._date)
        self.title_frame.pack_forget()
        self.botton_frame.pack_forget()
        data_to_excel(respuesta)
        #Aqui va la funcion que llama a lo graficos tipo pie, se le pasa la fecha y si es de ingreso o gastos
    def bar_buttom_callback(self):
        """Funcion para abrir una ventana si se presiona el bar_graph

        ...
        :return: setea graph_choice con el grafico y el mes
        :rtype: tupla
        """
        msg = CTkMessagebox(title="info", message="Genera un gráfico de barras comparando lo proyectado para el presupuesto con los gastos por mes",option_1="Cancelar",option_2="Aceptar")
        respuesta = msg.get()
        if respuesta == "Aceptar":
            if self.topCalendar is None or not self.topCalendar.winfo_exists():
                self.topCalendar = TopCalendar(self.update_date,config.app)  # create window if its None or destroyed
                self.topCalendar.wm_transient(config.app)
            else:
                self.topCalendar.focus()  # if window exists focus it
        self._graph_choice= ("Barras_mes",self._date)
        self.title_frame.pack_forget()
        self.botton_frame.pack_forget()
    def year_buttom_callback(self):
        """Funcion para abrir una ventana si se presiona el year_graph
        """
        msg = CTkMessagebox(title="info", message="Genera un gráfico con las tendencias de ahorros,ingresos y gastos en el año",option_1="Cancelar",option_2="Aceptar")
        respuesta = msg.get()
        ###Aqui deberia haber un condicional que revisa si hay datos suficientes para generar el grafico
        self._graph_choice= ("Barras_anual")
        self.title_frame.pack_forget()
        self.botton_frame.pack_forget()
        
    def reporte_buttom_callback(self):
        """Funcion para abrir una ventana si se presiona el reporte
        """
        msg = CTkMessagebox(title="info", message="Genera el reporte mensual",option_1="Cancelar",option_2="Aceptar")
        respuesta = msg.get()
        if respuesta == "Aceptar":
            if self.topCalendar is None or not self.topCalendar.winfo_exists():
                self.topCalendar = TopCalendar(self.update_date,config.app)  # create window if its None or destroyed
                self.topCalendar.wm_transient(config.app)
            else:
                self.topCalendar.focus()  # if window exists focus it
        self._graph_choice= ("Reporte",self._date)
        self.title_frame.pack_forget()
        self.botton_frame.pack_forget()

    def update_date(self,choice):
        self._date=choice


        


