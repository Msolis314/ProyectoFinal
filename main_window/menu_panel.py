"""Módulo que contiene toda la estructura de la ventana principal del programa"""
import customtkinter 
import os
import ttkbootstrap as ttk
from PIL import Image
from tools.Usos import reader_image
from tools.Usos import center
from tools.Usos import set_font 
from tablesetting.data_base_user import new_data
from system_vars.Vars import *
from entry_classes.income import IncomeFrame
from entry_classes.spend import GastosFrame
from entry_classes.budget import PresupuestoFrame
from graph_classes.graph_choice import GraphChoice
from pathlib import Path
#path_image =path_image= os.path.join(os.path.dirname(os.path.realpath("Documents")),r"./Imagenes")
import system_vars.config  as config
global path_image
path_image=Path('.') / "Imagenes"

class MainWindow(customtkinter.CTk):
    """Clase que controla la ventana principal

    :param customtkinter: Clase padre de la biblioteca
    :type customtkinter: Class
    """
    def __init__(self, currentuser):
        """Constructora de la clase, se encarga de aspectos de la configuracion

        :param currentuser: Usuario actual que hizo login en el sistema
        :type currentuser: str
        """
        super().__init__()
        #Configurar la principal
        self.title("Presupuesto Mensual")
        self.iconbitmap(os.path.join(path_image,"icon.ico"))
        weight = 1000
        height = 600
        center(self,weight,height)
        self.resizable(False,False)
        self.user = currentuser
        config.currentuser = currentuser
        self.sections()

    def sections(self):
        """Funcion donde se crean las instancias de las diferentes secciones del programa

        :param up_panel: Panel superior
        :type up_panel: UpperBar
        :param menu_panel: Panel del menu
        :type menu_panel: MenuFrame
        :param body_panel: Panel de la seccion de display del programa
        :type body_panel:BodyFrame
        """
        #Frames de las secciones principales
        self.up_panel= UpperBar(self,self.user)
        #La declaracion de este widget sucede en esta seccion para acceder a la funcion que contrae y despliega el menu
        self.side_menu_image=reader_image(path_image,"sidemenu.png",(10,10))
        #Boton de abrir y cerrar menu
        self._menu_bottom= customtkinter.CTkButton(self.up_panel,
                                                   text=" ", 
                                                   border_width=0,width=20,
                                                   fg_color=COLOR_SUPERIOR,
                                                   hover_color=HOVER_COLOR,
                                                   text_color=TEXT_COLOR,
                                                   image=self.side_menu_image,
                                                   compound="left",
                                                   command=self.toggle_panel)
        self._menu_bottom.pack(side=ttk.LEFT)
        self.menu_panel= MenuFrame(self)
        self.body_panel=BodyFrame(self)

        #Metodos para desplegar widgets
        self.up_panel.widgets_upper_bar()
        self.menu_panel.widgets_menu(self.body_panel,self)
    
    def toggle_panel(self):
        """
        funcion para contraer o desplegar el menu lateral
        """
        if self.menu_panel.winfo_ismapped():
            self.menu_panel.pack_forget()
        else:
            self.menu_panel.pack(side=ttk.LEFT,fill='y')
""" 
Definicion de los Frames de cada seccion 
Heredan de customtkinter.CTkFrame
Necesitan que se les pase el Master
"""
class BodyFrame(customtkinter.CTkFrame):
    """Clase que configura la ventana principal"""
    def __init__(self,master):
        super().__init__(master)
        self.configure(master,fg_color=COLOR_BODY,width=150)
        self.pack(side=ttk.RIGHT, fill='both', expand=True)
        
        self.grid_columnconfigure(2, weight=1)
class UpperBar(customtkinter.CTkFrame):
    """Clase de la barra superior
    """
    def __init__(self,master,User):
        """Constructora de la clase, configura aspectos del Frame

        :param master: Ventana superior donde va la barra
        :type master: CTk
        :param User: Usuario actual
        :type User: str
        """
        super().__init__(master)
        self.configure(master, height=50,fg_color=FG_COLOR2,border_width=0)
        self.pack(side=ttk.TOP, fill ='both')
        self.User = User
    def widgets_upper_bar(self):
        #Display barra superior
        self.title=customtkinter.CTkLabel(self, 
                                          text_color=TEXT_COLOR,
                                          text="Presupuesto digital",
                                          font=("Cascadia Mono SemiBold",15),
                                          fg_color='transparent',padx=10,
                                          pady=10,
                                          width=16)
        self.title.pack(side=ttk.LEFT)
        #Usuario actual
        self._current_user= customtkinter.CTkLabel(self,
                                                    text=self.User,pady=10, padx=10,
                                                    text_color=TEXT_COLOR,
                                                    font=("Cascadia Mono SemiBold",12))
        self._current_user.pack(side=ttk.RIGHT)

class MenuFrame(customtkinter.CTkFrame):
    """Clase que define al menu lateral

    """
    def __init__(self,master):
        """Constructora de la clase, configura las imagenes

        :param master: Ventana principal donde se quiere posicionar el frame
        :type master: CTK
        """
        super().__init__(master)
        self.menu_icon=reader_image(path_image,"menu.png",(40,40))
        self.image2=reader_image(path_image,"salary.png",(20,20))
        self.image3=reader_image(path_image,"line-chart.png",(20,20))
        self.image4=reader_image(path_image,"file.png",(20,20))
        self.configure(master,width=400,fg_color=FG_COLOR2)
        self.pack(side=ttk.LEFT, fill='both', expand=False)
        self.grid_rowconfigure(5,weight=1)
   
    def widgets_menu(self,body,root):
        """Funcion que maneja los widgets del menu

        :param body: Frame donde se quieren posicionar los widgets
        :type body: CTkFrame
        :param root: Ventana Principal
        :type root: CTk
        :param data_user: Boton que despliega las opciones para la entrada del usuario
        :type data_user: CTkButtom
        :param _analisis: Boton que despliega las opciones para graficacion
        :type _analisis: CTkButtom
        :param exportar_datos: Boton que despliega las opciones para exportar
        :type exportar_datos: CTkButtom
        """
        self.Main=root
       #Opciones del menu lateral
        self.menu_label=customtkinter.CTkLabel(self, text = " ",compound="top",image=self.menu_icon)
        self.menu_label.grid(row=0, column=0,padx=20,pady=20,sticky="nsew")
        self.master=body
        self.data_user= customtkinter.CTkButton(self, text ="Datos del usuario",
                                                corner_radius=0,
                                                height=30,
                                                font=set_font(),
                                                border_spacing=10,
                                                fg_color='transparent', 
                                                text_color=("gray10", "gray90"), 
                                                hover_color=("gray70", "gray30"),
                                                image=self.image2, 
                                                anchor="w",
                                                command=self.evento_data_user)
        self.data_user.grid(row=2,column=0, sticky="nsew")
        self._analisis= customtkinter.CTkButton(self, text ="Visualizacion de datos",
                                            corner_radius=0,font=set_font(),
                                            height=30,
                                            border_spacing=10,
                                            fg_color='transparent', 
                                            text_color=("gray10", "gray90"), 
                                            hover_color=("gray70", "gray30"), 
                                            anchor="w",
                                            image=self.image3,
                                            command=self.evento_analisis)
        self._analisis.grid(row=3,column=0, sticky="nsew")
        self.exportar_datos= customtkinter.CTkButton(self, text ="Exportar Datos",
                                            corner_radius=0,
                                            height=30,font=set_font(),
                                            border_spacing=10,
                                            fg_color='transparent', 
                                            text_color=("gray10", "gray90"), 
                                            hover_color=("gray70", "gray30"), 
                                            anchor="w",
                                            image=self.image4,
                                            command=self.evento3)
        self.exportar_datos.grid(row=4,column=0, sticky="nsew")
        #self.menu_display= customtkinter.CTkOptionMenu(master=self,values = ['blue','dark-blue','green'], command=self.evento_color)
        #self.menu_display.grid(row =6, column=0,padx=20,pady=20 ,sticky = "s")
        self.logout=customtkinter.CTkButton(master=self,text='Log Out', font=set_font(),command=self.evento_logout)
        self.logout.grid(row=6,column=0,padx=20,pady=20,sticky='s')
        self.menu_display= customtkinter.CTkOptionMenu(master=self,
                                                       values = ['dark','system','light'], 
                                                       command=self.evento_apariencia,fg_color=BORDER_COLOR,dropdown_fg_color=BORDER_COLOR,
                                                       button_color=BORDER_COLOR,
                                                       button_hover_color=HOVER_COLOR,
                                                       font=set_font(),
                                                       dropdown_font=set_font())
        self.menu_display.grid(row =5, column=0,padx=20,pady=20 ,sticky = "s")
        self.change_window("data_user")
    def evento_apariencia(self,op):
        #Definir eventos para los botones y menus
        customtkinter.set_appearance_mode(op)
    def evento_logout(self):
        #Evento para logout
        self.Main.destroy()
         
    def evento_data_user(self):
        #Al clickear entrada de datos 
        self.change_window("data_user")
    def evento_analisis(self):
        #Evento para analisis
        self.change_window("analisis")
    def evento3(self):
        #evento para exportar datos
        self.change_window("export")

    def change_window(self,buttom:str):
        """
        Esta es la funcion que se encarga de cambiar lo que se ve en el panel principal
        :param buttom: Boton seleccionado
        :type buttom:str
        """
        #Esto es para que quede marcada la opcion que se muestra en el momento en pantalla
        if buttom == "analisis":
            self._analisis.configure(fg_color=BUTTOM_HOVER)
        else:
            self._analisis.configure(fg_color="transparent")
        if buttom == "data_user":
            self.data_user.configure(fg_color=BUTTOM_HOVER)
        else:
            self.data_user.configure(fg_color="transparent")
        if buttom == "export":
            self.exportar_datos.configure(fg_color=BUTTOM_HOVER)
        else:
            self.exportar_datos.configure(fg_color="transparent")
        #Creo las instancias de los frames 
        data = EntradaDatosFrame(self.master)
        analisis= Analisis(self.master)
        export = Exportardatos(self.master)
        #Posiciono los Frames
        if buttom == "data_user":   
            data.get_frame().grid(row=0, column=2, sticky = "nsew")
        else:
            data.get_frame().grid_forget()
        if buttom == "analisis":
            analisis.get_frame().grid(row=0, column=2, sticky = "nsew")
        else:
            analisis.get_frame().grid_forget()
        if buttom == "export":
            export.get_frame().grid(row=0, column=2, sticky = "nsew")
        else:
            export.get_frame().grid_forget()
class SubFrames(customtkinter.CTkFrame):
    #Clase abstracta para definir caracteristicas de las otras subclases de la ventana
    def __init__(self, master):
        super().__init__(master)
        self._layout= customtkinter.CTkFrame(master, corner_radius=0,fg_color="transparent")
        self._layout.grid_columnconfigure(0, weight=1)
    def get_frame(self):
         #Devuelve el Frame
         return self._layout
   



class EntradaDatosFrame(SubFrames):
    #Clase para el boton data_user
    def __init__(self,master):
        #Boton 1
        super().__init__(master)
        self.image_ingresos=customtkinter.CTkImage(Image.open(os.path.join(path_image,"profits.png")), size=(40,40))
        self.buttom_ingresos= customtkinter.CTkButton(master=self._layout,
                                                      text="Ingresos",
                                                      image=self.image_ingresos, 
                                                      compound="top",font=set_font(),
                                                      command=self.event_boton1)
        self.buttom_ingresos.grid(row=0 , column= 0, padx=20,pady=10, sticky ="nsew")
        # Boton 2 
        self.image_gastos=customtkinter.CTkImage(Image.open(os.path.join(path_image,"expense.png")), size=(40,40))
        self.buttom_gastos =customtkinter.CTkButton(master=self._layout,
                                                    text="Gastos",fg_color=BORDER_COLOR,
                                                    image=self.image_gastos,hover_color=HOVER_COLOR, 
                                                    compound="top",font=set_font(),
                                                    command=self.event_boton2)
        self.buttom_gastos.grid(row=1 , column= 0, padx=20,pady=10, sticky ="nsew")

        #Boton 3
        self.image_presupuesto= customtkinter.CTkImage(Image.open(os.path.join(path_image,"budget.png")), size=(40,40))
        self.buttom_budget=customtkinter.CTkButton(master=self._layout,
                                                   text="Presupuesto",font=set_font(),
                                                   image=self.image_presupuesto, 
                                                   compound="top",
                                                   command=self.event_boton3)
        self.buttom_budget.grid(row=2 , column= 0, padx=20,pady=10, sticky ="nsew")
        #Nuevo frame
        self.new_frame_income=SubFrames(master)
        self.new_frame_gastos= SubFrames(master)
        self.new_frame_budget = SubFrames(master)
    def event_boton1(self):
        #Para entrar un nuevo Frame de ingresos
        self._layout.grid_forget()
        self.new_frame_income._layout.grid(row=0, column=2, sticky = "nsew")
        self.new_frame_income._layout.columnconfigure(0, weight=1)
        self.new_frame_income._layout.rowconfigure(0,weight=1)
        IncomeFrame(self.new_frame_income._layout)
    def event_boton2(self):
        #Para entrar al nuevo frame de ingreso de gastos
        self._layout.grid_forget()
        self.new_frame_gastos._layout.grid(row=0,column=2,sticky='nsew')
        self.new_frame_gastos._layout.columnconfigure(0,weight=1)
        self.new_frame_gastos._layout.rowconfigure(0,weight=1)
        GastosFrame(self.new_frame_gastos._layout)
    def event_boton3(self):
        #Para entrar al nuevo frame de ingreso de presupuesto 
        self._layout.grid_forget()
        self.new_frame_budget._layout.grid(row=0,column=2,sticky='nsew')
        self.new_frame_budget._layout.columnconfigure(0,weight=1)
        self.new_frame_budget._layout.rowconfigure(0,weight=1)
        PresupuestoFrame(self.new_frame_budget._layout)
        
class Analisis(SubFrames):
    #Clase para el boton analisis
    def __init__(self,master):
        super().__init__(master)
        GraphChoice(self._layout)
        #self.option_men_var= customtkinter.StringVar(value = "grafica")
        #self.options_analisis= customtkinter.CTkOptionMenu(self._layout, values=["Grafica","Pie chart","muestreo","Comparacion"],command=self.get_option_menu_choice ,variable=self.option_men_var)

        #self.options_analisis.grid(row=0, column=0,padx=20,pady=10,sticky="nsew")
   #Prueba
    def get_option_menu_choice(self,choice):
        print(choice)

class Exportardatos(SubFrames):
    # Clase para el boton de exportar datos
    def __init__(self,master):
        super().__init__(master)
        self.title_frame3= customtkinter.CTkLabel(self._layout, text ="Opciones de descarga",font=customtkinter.CTkFont(family="Century Gothic", weight="bold"))
        self.title_frame3.grid(row=0, column=0, padx=20,pady=20, sticky="nsew",columnspan=2)
        #Radio buttoms
        self.radio_var = customtkinter.IntVar(value=0)
        self.op1=customtkinter.CTkRadioButton(self._layout, text="Excel",font=customtkinter.CTkFont(family="Century Gothic"),command=self.radio_event,variable=self.radio_var, value =1)
        self.op1.grid(row=1, column=0, padx=10, pady =(0,20),sticky="w")
        self.op2=customtkinter.CTkRadioButton(self._layout, text="Graficos",font=customtkinter.CTkFont(family="Century Gothic"),command=self.radio_event,variable=self.radio_var, value =2)
        self.op2.grid(row=1, column=1, padx=10, pady =(0,20), sticky="w")
        
    def radio_event(self):
        print(f'radio var is {self.radio_var.get()}')