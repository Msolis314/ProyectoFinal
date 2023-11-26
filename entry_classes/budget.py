"""Modulo para configurar la entrada del presupuesto
    """
import customtkinter
import tkinter as tk
from .template import *
from system_vars import *
from tools.Usos import *
font_exam= 'Berlin Sans FB'
class PresupuestoFrame(Economy):
    """Clase para el manejo de la entrada del presupuesto

    :param Economy: Clase padre que maneja los atributos y la escritura en una base de datos
    :type Economy: Class
    :param month_frame: donde se posicionan los widgets con los meses
    :type month_frame : CTkFrame
    :param meses : botones para elegir cada meses llaman a una funcion para actualizar la ventana
    :type meses: CTkButtom
    :param final_frame: donde se coloca el boton de guardar
    :type final_frame: CTkFrame
    :param user_entry: instancia de la clase con las entradas del usuario
    :type user_entry: Entry

    """
    
    def __init__(self,layout):
        """Constructor de la clase

        :param layout: El frame padre donde se quieren posicionar todos los otros frames de la clase
        :type layout: CTkFrame
        """

        super().__init__()
        self.month_frame= customtkinter.CTkFrame(master=layout, width=1500, fg_color=FG_COLOR)
        self.month_frame.pack(side=tk.LEFT, fill='both', expand=False)
        self.month_frame.columnconfigure(0,weight=1)
        jan_image= reader_image(Path_Image,'enero.png',(30,30))
        self.enero = customtkinter.CTkButton(self.month_frame,text=" ",
                                             text_color=TEXT_COLOR2,
                                             corner_radius=0, font=set_font(font_exam, 24),
                                             hover_color=HOVER_COLOR,
                                             fg_color=FG_COLOR,image=jan_image,
                                             command=lambda : self.change_window("Enero"))
        self.enero.grid(row=1,column=0,pady=2, sticky='nsew')
        feb_image=reader_image(Path_Image,'febrero.png',(30,30))
        self.febrero = customtkinter.CTkButton(self.month_frame,
                                               text=" ",
                                               font=set_font(font_exam,24),
                                               fg_color=FG_COLOR,hover_color=BUTTOM_HOVER,
                                               corner_radius=0,
                                               command=lambda : self.change_window("Febrero"),image=feb_image)
        self.febrero.grid(row=2,column=0,pady=2, sticky='nsew')
        marzo_image=reader_image(Path_Image,'marzo.png',(30,30))
        self.marzo = customtkinter.CTkButton(self.month_frame,
                                               text=" ",
                                               hover_color=HOVER_COLOR, 
                                               font=set_font(font_exam,24),
                                               fg_color=FG_COLOR,
                                               corner_radius=0,
                                               command=lambda : self.change_window("Marzo"),image=marzo_image)
        self.marzo.grid(row=3,column=0,pady=2, sticky='nsew')
        abril_image=reader_image(Path_Image,'abril.png',(30,30))
        self.abril = customtkinter.CTkButton(self.month_frame,
                                               text=" ",
                                               hover_color=HOVER_COLOR,
                                               text_color=TEXT_COLOR2, 
                                               font=set_font(font_exam,24),
                                               fg_color=FG_COLOR,
                                               corner_radius=0,command=lambda : self.change_window("Abril"),
                                               image=abril_image)
        self.abril.grid(row=4,column=0,pady=2, sticky='nsew')
        may_image=reader_image(Path_Image,'mayo.png',(30,30))
        self.mayo = customtkinter.CTkButton(self.month_frame,
                                               text=" ",
                                               hover_color=HOVER_COLOR,
                                               text_color=TEXT_COLOR2, 
                                               font=set_font(font_exam,24),
                                               fg_color=FG_COLOR,
                                               corner_radius=0,command=lambda : self.change_window("Mayo"),
                                               image=may_image)
        self.mayo.grid(row=5,column=0,pady=2, sticky='nsew')
        jun_image=reader_image(Path_Image,'junio.png',(30,30))
        self.junio = customtkinter.CTkButton(self.month_frame,
                                               text=" ",
                                               hover_color=HOVER_COLOR,
                                               text_color=TEXT_COLOR2, 
                                               font=set_font(font_exam,24),
                                               fg_color=FG_COLOR,
                                               corner_radius=0,
                                               image=jun_image,command=lambda : self.change_window("Junio"))
        self.junio.grid(row=6,column=0,pady=2, sticky='nsew')
        jul_image=reader_image(Path_Image,'julio.png',(30,30))
        self.julio = customtkinter.CTkButton(self.month_frame,
                                               text=" ",
                                               hover_color=HOVER_COLOR,
                                               text_color=TEXT_COLOR2, 
                                               font=set_font(font_exam,24),
                                               fg_color=FG_COLOR,
                                               corner_radius=0,command=lambda : self.change_window("Julio"),image=jul_image)
        self.julio.grid(row=7,column=0,pady=2, sticky='nsew')
        ago_image=reader_image(Path_Image,'agosto.png',(30,30))
        self.agosto = customtkinter.CTkButton(self.month_frame,
                                               text=" ",
                                               hover_color=HOVER_COLOR,
                                               text_color=TEXT_COLOR2, 
                                               font=set_font(font_exam,24),
                                               fg_color=FG_COLOR,
                                               corner_radius=0,command=lambda : self.change_window("Agosto"),image=ago_image)
        self.agosto.grid(row=8,column=0,pady=2, sticky='nsew')
        sep_image=reader_image(Path_Image,'septiembre.png',(30,30))
        self.septiembre = customtkinter.CTkButton(self.month_frame,
                                               text=" ",
                                               hover_color=HOVER_COLOR,
                                               text_color=TEXT_COLOR2, 
                                               font=set_font(font_exam,24),
                                               fg_color=FG_COLOR,
                                               corner_radius=0,command=lambda : self.change_window("Septiembre"),image=sep_image)
        self.septiembre.grid(row=9,column=0,pady=2, sticky='nsew')
        oc_image=reader_image(Path_Image,'octubre.png',(30,30))
        self.octubre = customtkinter.CTkButton(self.month_frame,
                                               text=" ",
                                               hover_color=HOVER_COLOR,
                                               text_color=TEXT_COLOR2, 
                                               font=set_font(font_exam,24),
                                               fg_color=FG_COLOR,
                                               corner_radius=0,command=lambda : self.change_window("Octubre"),image=oc_image)
        self.octubre.grid(row=10,column=0,pady=2, sticky='nsew')
        nov_image=reader_image(Path_Image,'noviembre.png',(30,30))
        self.noviembre = customtkinter.CTkButton(self.month_frame,
                                               text=" ",
                                               hover_color=HOVER_COLOR,
                                               text_color=TEXT_COLOR2, 
                                               font=set_font(font_exam,24),
                                               fg_color=FG_COLOR,
                                               corner_radius=0,command=lambda : self.change_window("Noviembre"),image=nov_image)
        self.noviembre.grid(row=11,column=0,pady=2, sticky='nsew')
        dec_image=reader_image(Path_Image,'diciembre.png',(30,30))
        self.diciembre = customtkinter.CTkButton(self.month_frame,
                                               text=" ",
                                               hover_color=HOVER_COLOR,
                                               text_color=TEXT_COLOR2, 
                                               font=set_font(font_exam,24),
                                               fg_color=FG_COLOR,
                                               corner_radius=0,command=lambda : self.change_window("Diciembre"),image=dec_image)
        self.diciembre.grid(row=12,column=0,pady=2, sticky='nsew')
        self.final_frame= customtkinter.CTkFrame(layout,fg_color='transparent')
        self.final_frame.pack(side=tk.RIGHT,fill='both',expand=False)
        self.safe_buttom= customtkinter.CTkButton(self.final_frame,text='Guardar',border_color=BORDER_COLOR,
                                                  text_color=TEXT_COLOR,font=set_font('Cascadia mono SemiBold', 18),
                                                  fg_color=BORDER_COLOR,
                                                  hover_color=HOVER_COLOR)
        self.safe_buttom.pack(fill='both', expand=True,pady=20)
        self.layout=layout
        
    
        self.user_entry= Entry(layout)
        self.user_entry.pack(side=tk.RIGHT,fill='both',expand=True)
    
        
    def change_window(self,month):
        """_summary_

        :param month: mes correspondiente al boton 
        :type month: string
        """
        if month == 'Enero':
            #Aqui debe ir una funcion que revise si hay datos en enero y le dice al usuario
            self.enero.configure(fg_color=BUTTOM_HOVER)
            self.user_entry.title_label.configure(text='Presupuesto Enero')
           
        else:
            self.enero.configure(fg_color='transparent')
            
        if month == 'Febrero':

            self.febrero.configure(fg_color=BUTTOM_HOVER)
            self.user_entry.title_label.configure(text='Presupuesto Febrero')
        else:
            self.febrero.configure(fg_color='transparent')
            
        if month == 'Marzo':
            self.marzo.configure(fg_color=BUTTOM_HOVER)
            self.user_entry.title_label.configure(text='Presupuesto Marzo')
        else:
            self.marzo.configure(fg_color='transparent')
        if month == 'Abril':
            self.abril.configure(fg_color=BUTTOM_HOVER)
            self.user_entry.title_label.configure(text='Presupuesto Abril')
        else:
            self.abril.configure(fg_color='transparent')
        if month == 'Mayo':
            self.mayo.configure(fg_color=BUTTOM_HOVER)
            self.user_entry.title_label.configure(text='Presupuesto Mayo')
        else:
            self.mayo.configure(fg_color='transparent')
        if month == 'Junio':
            self.junio.configure(fg_color=BUTTOM_HOVER)
            self.user_entry.title_label.configure(text='Presupuesto Junio')
        else:
            self.junio.configure(fg_color='transparent')
        if month == 'Julio':
            self.julio.configure(fg_color=BUTTOM_HOVER)
            self.user_entry.title_label.configure(text='Presupuesto Julio')
        else:
            self.julio.configure(fg_color='transparent')
        if month == 'Agosto':
            self.agosto.configure(fg_color=BUTTOM_HOVER)
            self.user_entry.title_label.configure(text='Presupuesto Agosto')
        else:
            self.agosto.configure(fg_color='transparent')
        if month == 'Septiembre':
            self.septiembre.configure(fg_color=BUTTOM_HOVER)
            self.user_entry.title_label.configure(text='Presupuesto Septiembre')
        else:
            self.septiembre.configure(fg_color='transparent')
        if month == 'Octubre':
            self.octubre.configure(fg_color=BUTTOM_HOVER)
            self.user_entry.title_label.configure(text='Presupuesto Octubre')
        else:
            self.octubre.configure(fg_color='transparent')
        if month == 'Noviembre':
            self.noviembre.configure(fg_color=BUTTOM_HOVER)
            self.user_entry.title_label.configure(text='Presupuesto Noviembre')
        else:
            self.noviembre.configure(fg_color='transparent')
        if month == 'Diciembre':
            self.diciembre.configure(fg_color=BUTTOM_HOVER)
            self.user_entry.title_label.configure(text='Presupuesto Diciembre')
        else:
            self.diciembre.configure(fg_color='transparent')
    def event_guardar(self):
        """Aqui se debe verificar las entradas del usuario y escribirlas en la base de datos"""
        pass
class Entry(customtkinter.CTkFrame):
    """Clase con las entradas del presupuesto


    :param categoria_label: titulo de la categoria
    :type categoria_label: CTkLabel
    :param categoria_entry: Casilla de entrada de datos
    :type categoria_entry: CTkEntry
    :param categoria_var: variable donde se guarda lo digitado en la entrada de la categoria
    :type categoria_var: str

    :param title_frame: donde se coloca el titulo del widget
    :type title_frame: CTkFrame
    """
    def __init__(self,master):
        """Constructura de la clase en ella tambien se configura el frame y se cargan imagenes

        :param master: Frame superior donde se quiere colocar la instancia de esta clase
        :type master: CTkFrame
        """
        super().__init__(master)
        self.configure(master,fg_color=FG_COLOR,width=1500)
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(3,weight=1)
        self.grid_columnconfigure(5,weight=1)
        self.grid_rowconfigure(9,weight=1)
        self.title_frame=customtkinter.CTkFrame(self,fg_color=FG_COLOR)
        self.title_frame.grid(row=0,column=3,sticky='nsew')
        self.title_label = customtkinter.CTkLabel(self.title_frame,text="Presupuesto",
                                                 text_color=TEXT_COLOR,
                                                 font=set_font('Cascadia Mono SemiBold',15))
        self.title_label.pack(side=tk.TOP,fill=tk.BOTH,expand=True)
        economy_atr=['domicilio','higiene','transporte','entretenimiento','deudas','seguros','servicios','otros']
        for index,atr in enumerate(economy_atr):
            customtkinter.CTkLabel(self,text=atr,text_color=TEXT_COLOR,
                                                 font=set_font('Cascadia Mono')).grid(row = 1+ index, column=1,pady=5,padx=5)
            
        #Casillas para la entrada de datos
        self.domicilio_var = customtkinter.StringVar()
        self.domicilio_entry = customtkinter.CTkEntry(self,
                                                 text_color=TEXT_COLOR,placeholder_text="descripcion", 
                                                 font=set_font('Cascadia Mono'),
                                                 textvariable=self.domicilio_var)
        self.domicilio_entry.grid(row=1, column=4,pady=5)
    
        self.higiene_var = customtkinter.StringVar()
        self.higiene_entry = customtkinter.CTkEntry(self,
                                                 text_color=TEXT_COLOR,placeholder_text="descripcion", 
                                                 font=set_font('Cascadia Mono'),
                                                 textvariable=self.higiene_var)
        self.higiene_entry.grid(row=2, column=4,pady=5)

        
        self.transporte_var = customtkinter.StringVar()
        self.transporte_entry = customtkinter.CTkEntry(self,
                                                 text_color=TEXT_COLOR,placeholder_text="descripcion", 
                                                 font=set_font('Cascadia Mono'),
                                                 textvariable=self.transporte_var)
        self.transporte_entry.grid(row=3, column=4,pady=5)

        
        self.entretenimiento_var = customtkinter.StringVar()
        self.entretenimiento_entry = customtkinter.CTkEntry(self,
                                                 text_color=TEXT_COLOR,placeholder_text="descripcion", 
                                                 font=set_font('Cascadia Mono'),
                                                 textvariable=self.entretenimiento_var)
        self.entretenimiento_entry.grid(row=4, column=4,pady=5)
        
        
        self.deudas_var = customtkinter.StringVar()
        self.deudas_entry = customtkinter.CTkEntry(self,
                                                 text_color=TEXT_COLOR,placeholder_text="descripcion", 
                                                 font=set_font('Cascadia Mono'),
                                                 textvariable=self.deudas_var)
        self.deudas_entry.grid(row=5, column=4,pady=5)

        
        self.seguros_var = customtkinter.StringVar()
        self.seguros_entry = customtkinter.CTkEntry(self,
                                                 text_color=TEXT_COLOR,placeholder_text="descripcion", 
                                                 font=set_font('Cascadia Mono'),
                                                 textvariable=self.seguros_var)
        self.seguros_entry.grid(row=6, column=4,pady=5)

        
        self.servicios_var = customtkinter.StringVar()
        self.servicios_entry = customtkinter.CTkEntry(self,
                                                 text_color=TEXT_COLOR,placeholder_text="descripcion", 
                                                 font=set_font('Cascadia Mono'),
                                                 textvariable=self.servicios_var)
        self.servicios_entry.grid(row=7, column=4,pady=5)

        
        self.otros_var = customtkinter.StringVar()
        self.otros_entry = customtkinter.CTkEntry(self,
                                                 text_color=TEXT_COLOR,placeholder_text="descripcion", 
                                                 font=set_font('Cascadia Mono'),
                                                 textvariable=self.otros_var)
        self.otros_entry.grid(row=8, column=4,pady=5)
        

        

