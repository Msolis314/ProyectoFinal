import customtkinter 
import os
import ttkbootstrap as ttk
from PIL import Image
from tools.Usos import reader_image
from tools.Usos import center
from tools.Usos import set_font 
from system_vars.Vars import COLOR_BG, COLOR_BODY , COLOR_MENU, COLOR_SUPERIOR, FG_COLOR,TEXT_COLOR,TEXT_COLOR2,HOVER_COLOR,BUTTOM_HOVER

global path_image
path_image =path_image= os.path.join(os.path.dirname(os.path.realpath("Documents")),r"./Imagenes")


class MainWindow(customtkinter.CTk):
    """
    Clase de la vetana princiapal
    hereda de customtkinter.CTk
    """
    def __init__(self, currentuser):
        super().__init__()
        #Configurar la principal
        self.title("Presupuesto Mensual")
        self.iconbitmap(os.path.join(path_image,"icon.ico"))
        weight = 1000
        height = 600
        center(self,weight,height)
        self.resizable(False,False)
        self.user = currentuser

        self.sections()

    def sections(self):
        """
         funcion donde se declaran las secciones presentes en el display
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
        self.menu_panel.widgets_menu(self.body_panel)
    
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
    ''' Clase de la barra superior'''
    def __init__(self,master,User):
        super().__init__(master)
        self.configure(master, fg_color=COLOR_SUPERIOR, height=50)
        self.pack(side=ttk.TOP, fill ='both')
        self.User = User
    #Display barra superior
    def widgets_upper_bar(self):
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
    """Clase que define al menu lateral"""
    def __init__(self,master):
        super().__init__(master)
        self.menu_icon=reader_image(path_image,"menu.png",(40,40))
        self.image2=reader_image(path_image,"salary.png",(20,20))
        self.image3=reader_image(path_image,"line-chart.png",(20,20))
        self.image4=reader_image(path_image,"file.png",(20,20))
        self.configure(master,width=400)
        self.pack(side=ttk.LEFT, fill='both', expand=False)
        self.grid_rowconfigure(5,weight=1)
   
    def widgets_menu(self,body):
        """
        funcion que maneja los widgets del menu
        recibe por parametro el body que representan donde se debe colocar cada widget
        """
       #Opciones del menu lateral
        self.menu_label=customtkinter.CTkLabel(self, text = " ",compound="top",image=self.menu_icon)
        self.menu_label.grid(row=0, column=0,padx=20,pady=20,sticky="nsew")
        self.master=body
        self.data_user= customtkinter.CTkButton(self, text ="Datos del usuario",
                                                corner_radius=0,
                                                height=30,
                                                border_spacing=10,
                                                fg_color='transparent', 
                                                text_color=("gray10", "gray90"), 
                                                hover_color=("gray70", "gray30"),
                                                image=self.image2, 
                                                anchor="w",
                                                command=self.evento_data_user)
        self.data_user.grid(row=2,column=0, sticky="nsew")
        self._analisis= customtkinter.CTkButton(self, text ="Visualizacion de datos",
                                            corner_radius=0,
                                            height=30,
                                            border_spacing=10,
                                            fg_color='transparent', 
                                            text_color=("gray10", "gray90"), 
                                            hover_color=("gray70", "gray30"), 
                                            anchor="w",
                                            image=self.image3,
                                            command=self.evento_analisis)
        self._analisis.grid(row=3,column=0, sticky="nsew")
        self.exportar_datos= customtkinter.CTkButton(self, text ="Exportar_Datos",
                                            corner_radius=0,
                                            height=30,
                                            border_spacing=10,
                                            fg_color='transparent', 
                                            text_color=("gray10", "gray90"), 
                                            hover_color=("gray70", "gray30"), 
                                            anchor="w",
                                            image=self.image4,
                                            command=self.evento3)
        self.exportar_datos.grid(row=4,column=0, sticky="nsew")
        self.menu_display= customtkinter.CTkOptionMenu(master=self,values = ['blue','dark-blue','green'], command=self.evento_color)
        self.menu_display.grid(row =6, column=0,padx=20,pady=20 ,sticky = "s")
        self.menu_display= customtkinter.CTkOptionMenu(master=self,
                                                       values = ['dark','system','light'], 
                                                       command=self.evento_apariencia)
        self.menu_display.grid(row =5, column=0,padx=20,pady=20 ,sticky = "s")
        self.change_window("data_user")
    def evento_apariencia(self,op):
        #Definir eventos para los botones y menus
        customtkinter.set_appearance_mode(op)
    def evento_color(self,color_theme):
        #Eventocolor
        customtkinter.set_default_color_theme(color_theme)   
    def evento_data_user(self):
        #Al clickear entrada de datos 
        self.change_window("data_user")
    def evento_analisis(self):
        #Evento para analisis
        self.change_window("analisis")
    def evento3(self):
        #evento para exportar datos
        self.change_window("export")

    def change_window(self,buttom):
        """
        Esta es la funcion que se encarga de cambiar lo que se ve en el panel principal
        parametro el boton elegido
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
                                                      compound="top",
                                                      command=self.event_boton1)
        self.buttom_ingresos.grid(row=0 , column= 0, padx=20,pady=10, sticky ="nsew")
        # Boton 2 
        self.image_gastos=customtkinter.CTkImage(Image.open(os.path.join(path_image,"expense.png")), size=(40,40))
        self.buttom_gastos =customtkinter.CTkButton(master=self._layout,
                                                    text="Gastos",
                                                    image=self.image_gastos, 
                                                    compound="top")
        self.buttom_gastos.grid(row=1 , column= 0, padx=20,pady=10, sticky ="nsew")

        #Boton 3
        self.image_presupuesto= customtkinter.CTkImage(Image.open(os.path.join(path_image,"budget.png")), size=(40,40))
        self.buttom_budget=customtkinter.CTkButton(master=self._layout,
                                                   text="Presupuesto",
                                                   image=self.image_presupuesto, 
                                                   compound="top")
        self.buttom_budget.grid(row=2 , column= 0, padx=20,pady=10, sticky ="nsew")
        #Nuevo frame
        self.new_frame=SubFrames(master)
    def event_boton1(self):
        #Para entrar un nuevo Frame
        self._layout.grid_forget()
        self.new_frame._layout.grid(row=0, column=2, sticky = "nsew")
        self.new_frame.columnconfigure(0, weight=1)
class Analisis(SubFrames):
    #Clase para el boton analisis
    def __init__(self,master):
        super().__init__(master)
        self.option_men_var= customtkinter.StringVar(value = "grafica")
        self.options_analisis= customtkinter.CTkOptionMenu(self._layout, values=["Grafica","Pie chart","muestreo","Comparacion"],command=self.get_option_menu_choice ,variable=self.option_men_var)

        self.options_analisis.grid(row=0, column=0,padx=20,pady=10,sticky="nsew")
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