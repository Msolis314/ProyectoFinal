"""Modulo para configurar el panel de ingresos de gastos del usuario"""
import customtkinter
from .template import *
from tools.Usos import *
from system_vars.Vars import *
import system_vars.config as config

class GastosFrame(Economy):
    """Clase que maneja el layout de la interfaz para los gastos

    :param Income: Clase padre que maneja los atributos de categoria en conjunto con los métodos de escritura en la base de datos
    :type Income: Class
    :param general_info: contiene los widgets que corresponde a la entrada de datos general 
    :type general_infor: CTkFrame
    :param name_entry:Donde se digita el nombre del gasto, se accede al valor con name_entry.get(), se debe validar que no este vacía la entrada
    :type name_entry:CTkEntry
    :param options_spend_var:variable donde se almacena la elección de la categoría de gasto, se accede al valor con options_spend_var.get()
    :type options_spend_var:str
    :param amount_entry_var:variable donde se almacena el mónto del ingreso, se accede al valor con amount_entry_var.get(), se debe convertir el valor a un float y validar está entrada
    :type amount_entry_var: str
    :param coin_var:variable donde se almacena el tipo de cambio, coin_var.get() para acceder 
    :type coin_var:str
    :param others_frame: contiene widgets de otras entradas
    :type others_frame: CTkFrame
    :param final_frame: frame con el boton de salida
    :type final_frame:CTkFrame
    :param final_buttom: Al presionar este botón se debe llamar un método que use métodos de la clase Economy para validar entradas, expulse error o guarde las entradas según sea el caso
    :type final_buttom: CTkButtom
    """  
    def __init__(self,layout):
        """Contructora de la clase, configura aspectos de la apariencia

        :param layout: Frame padre donde se quieren posicionar los widgets
        :type layout: CTkFrame
        """
        super().__init__()
        self.general_info = customtkinter.CTkFrame(master=layout)
        self.general_info.grid_columnconfigure(0,weight=1)
        self.general_info.grid_columnconfigure(5,weight=1)
        self.general_info.grid(row = 1 , column=0,sticky="nsew",pady=20)
        #Widgets para darle un nombre a la entrada de ingreso
        self.name_label = customtkinter.CTkLabel(self.general_info,text="Descripcion del gasto",
                                                 text_color=TEXT_COLOR,
                                                 font=set_font('Cascadia Mono'))
        self.name_label.grid(row=0, column=1,padx=20,pady=20)
        self.name_entry = customtkinter.CTkEntry(self.general_info,
                                                 text_color=TEXT_COLOR,placeholder_text="descripcion", 
                                                 font=set_font('Cascadia Mono'))
        self.name_entry.grid(row=1, column=1, padx=20,pady=20)
        #Eleccion del tipo de ingreso
        self.descriptive_label = customtkinter.CTkLabel(self.general_info,text="Categoría de Gasto",
                                                 text_color=TEXT_COLOR,
                                                 font=set_font('Cascadia mono'))
        self.descriptive_label.grid(row=0, column=2,padx=20,pady=20)
        #Variable que guarda la eleccion de la categoria
        self.options_spend_var = customtkinter.StringVar(value="Domicilio")

        self.options_spend= customtkinter.CTkOptionMenu(self.general_info, values=["Domicilio","Comida","Higene","Transporte","Vestimenta","Entretenimiento","Deudas","Ahorros","Seguros","Servicios","Otros"],
                                                         dropdown_hover_color=HOVER_COLOR,dropdown_font=set_font('Shanti'),variable=self.options_spend_var)
        #se accederia al valor self.options_spend_var.get() este hay que pasarlo por una funcion set de Economy y asignarlo al atributo categoria
        self.options_spend.grid(row=1, column=2,padx=20,pady=20)
        #Digitar el monto
        self.amount_label= customtkinter.CTkLabel(self.general_info, 
                                                  text="Mónto", text_color=TEXT_COLOR, 
                                                  font=set_font('Cascadia mono'))
        self.amount_label.grid(row=0, column=3,padx=20,pady=20)
        self.amount_entry_var= customtkinter.StringVar()

        self.amount_entry = customtkinter.CTkEntry(self.general_info, 
                                                   font=set_font('Cascadia mono'),textvariable= self.amount_entry_var,
                                                   text_color=TEXT_COLOR)
        self.amount_entry.grid(row=1,column=3,padx=20,pady=20)

        #Tipo de moneda 
        self.coin_label = customtkinter.CTkLabel(self.general_info,
                                                text='Tipo de cambio',
                                                font=set_font(), 
                                                text_color=TEXT_COLOR)
        self.coin_label.grid(row=0, column=4,padx=20,pady=20,sticky="nsew")
        self.coin_var=customtkinter.StringVar(value="Dolar")
        self.coin_entry = customtkinter.CTkSegmentedButton(self.general_info, values=["Dolar", "Colon", "Euro"],
                                                     command=self.coin_label_callback,font=set_font('Shanti'),
                                                     variable=self.coin_var)
        self.coin_entry.grid(row=1,column=4,padx=20,pady=20,sticky="nsew")
         #creo un nuevo frame
        self._others_frame= customtkinter.CTkFrame(master=layout,height=400)
        self._others_frame.grid_columnconfigure(0,weight=1)
        self._others_frame.grid_columnconfigure(4,weight=1)
        self._others_frame.grid(row=2,column=0,sticky="nsew",pady=40)
        #Boton de notas
        notas_image = reader_image(Path_Image,"notas.png",tam=(40,40))
        self.buttom_notas= customtkinter.CTkButton(master=self._others_frame,
                                                      text="Notas",height=50,
                                                      image=notas_image,font=set_font(), 
                                                      compound="top",
                                                      command=self.buttom_notas_callback)
        self.buttom_notas.grid(row=0 , column= 1, padx=20,pady=10, sticky ="nsew")

        #Boton de calendario
        calendar_image = reader_image(Path_Image,"calendario.png",tam=(40,40))
        self.calendario= customtkinter.CTkButton(master=self._others_frame,
                                                      text="Mes",height=50,
                                                      image=calendar_image,font=set_font(), 
                                                      compound="top",
                                                      command=self.buttom_calendar_callback)
        self.calendario.grid(row=0 , column= 2, padx=20,pady=10, sticky ="nsew")
        self.topCalendar=None
        self.topNotas=None
        self.final_frame=customtkinter.CTkFrame(master=layout,height=600)
        self.final_frame.grid(row=3,column=0,sticky="nsew",pady=40)

        self.final_buttom= customtkinter.CTkButton(master=self.final_frame,text="Guardar",height=100,width=500,font=set_font(tam=20))
        self.final_buttom.pack(fill=tk.BOTH,expand=True)

        
    def coin_label_callback(self,value):
        print(value)

    def buttom_notas_callback(self):
        """llama a la ventana para notas
        ...
        :return: actualiza el atributo de notas 
        :rtype: str
        
        """
        if self.topNotas is None or not self.topNotas.winfo_exists():
            self.topNotas = TopNotas(self.update_notas,config.app)  #Crear la ventana sino existe
            self.topNotas.wm_transient(config.app)
        else:
            self.topNotas.focus()  #Si existe la enfoca
    def buttom_calendar_callback(self):
        """llama a la ventana de elegir mes 
        """
        if self.topCalendar is None or not self.topCalendar.winfo_exists():
            self.topCalendar = TopCalendar(self.update_date,config.app)  # create window if its None or destroyed
            self.topCalendar.wm_transient(config.app)
        else:
            self.topCalendar.focus()  # if window exists focus it
    def update_date(self,n):
        """Esta en una funcion para pasar parametros entre ventanas, solamente actualiza uno de los atributos de la clase con un parametro elegido"""
        self._date=n
    def update_notas(self,n):
        """Esta en una funcion para pasar parametros entre ventanas, solamente actualiza uno de los atributos de la clase con un parametro elegido"""
        self._notas=n