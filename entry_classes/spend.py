import customtkinter
from .template import *
from tools.Usos import *
from system_vars.Vars import *
import system_vars.config as config
"""Modulo para configurar el panel de ingresos de gastos del usuario"""
class GastosFrame(Economy):
    """Clase para gesionar la interfaz para la entrada de una gasto por parte del usuario"""
    def __init__(self,layout):
        super().__init__()
        self.general_info = customtkinter.CTkFrame(master=layout)
        self.general_info.grid_columnconfigure(0,weight=1)
        self.general_info.grid_columnconfigure(5,weight=1)
        self.general_info.grid(row = 1 , column=0,sticky="nsew",pady=20)
        #Widgets para darle un nombre a la entrada de ingreso
        self.name_label = customtkinter.CTkLabel(self.general_info,text="Descripcion del gasto",
                                                 text_color=TEXT_COLOR,
                                                 font=set_font('Cascadia mono'))
        self.name_label.grid(row=0, column=1,padx=20,pady=20)
        self.name_entry = customtkinter.CTkEntry(self.general_info,
                                                 text_color=TEXT_COLOR,placeholder_text="descripcion", 
                                                 font=set_font('Cascadia mono'))
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

        self.amount_entry = customtkinter.CTkEntry(self.general_info, 
                                                   font=set_font('Cascadia mono'),
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
                                                     command=self.coin_label_callback,font=set_font('Shanti')
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
        self.final_frame=customtkinter.CTkFrame(master=layout,height=600)
        self.final_frame.grid(row=3,column=0,sticky="nsew",pady=40)

        self.final_buttom= customtkinter.CTkButton(master=self.final_frame,text="Guardar",height=100,width=500,font=set_font(tam=20))
        self.final_buttom.pack(fill=tk.BOTH,expand=True)

        
    def coin_label_callback(self,value):
        print(value)

    def buttom_notas_callback(self):
        pass
    def buttom_calendar_callback(self):
        if self.topCalendar is None or not self.topCalendar.winfo_exists():
            self.topCalendar = TopCalendar(self.update_date,config.app)  # create window if its None or destroyed
            self.topCalendar.wm_transient(config.app)
        else:
            self.topCalendar.focus()  # if window exists focus it
    def update_date(self,n):
        """Esta en una funcion para pasar parametros entre ventanas, solamente actualiza uno de los atributos de la clase con un parametro elegido"""
        self._date=n