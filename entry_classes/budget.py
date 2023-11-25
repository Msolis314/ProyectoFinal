import customtkinter
import tkinter as tk
from .template import *
from system_vars import *
from tools.Usos import *
font_exam= 'Berlin Sans FB'
class PresupuestoFrame(Economy):
    def __init__(self,layout):
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
                                             command=self.event_enero)
        self.enero.grid(row=1,column=0,pady=5, sticky='nsew')
        feb_image=reader_image(Path_Image,'febrero.png',(30,30))
        self.febrero = customtkinter.CTkButton(self.month_frame,
                                               text=" ",
                                               font=set_font(font_exam,24),
                                               fg_color=FG_COLOR,hover_color=BUTTOM_HOVER,
                                               corner_radius=0,
                                               command=self.event_febrero,image=feb_image)
        self.febrero.grid(row=2,column=0,pady=5, sticky='nsew')
        marzo_image=reader_image(Path_Image,'marzo.png',(30,30))
        self.marzo = customtkinter.CTkButton(self.month_frame,
                                               text=" ",
                                               hover_color=HOVER_COLOR, 
                                               font=set_font(font_exam,24),
                                               fg_color=FG_COLOR,
                                               corner_radius=0,
                                               command=self.event_marzo,image=marzo_image)
        self.marzo.grid(row=3,column=0,pady=5, sticky='nsew')
        abril_image=reader_image(Path_Image,'abril.png',(30,30))
        self.abril = customtkinter.CTkButton(self.month_frame,
                                               text=" ",
                                               hover_color=HOVER_COLOR,
                                               text_color=TEXT_COLOR2, 
                                               font=set_font(font_exam,24),
                                               fg_color=FG_COLOR,
                                               corner_radius=0,command=self.event_abril,
                                               image=abril_image)
        self.abril.grid(row=4,column=0,pady=5, sticky='nsew')
        may_image=reader_image(Path_Image,'mayo.png',(30,30))
        self.mayo = customtkinter.CTkButton(self.month_frame,
                                               text=" ",
                                               hover_color=HOVER_COLOR,
                                               text_color=TEXT_COLOR2, 
                                               font=set_font(font_exam,24),
                                               fg_color=FG_COLOR,
                                               corner_radius=0,command=self.event_mayo,
                                               image=may_image)
        self.mayo.grid(row=5,column=0,pady=5, sticky='nsew')
        jun_image=reader_image(Path_Image,'junio.png',(30,30))
        self.junio = customtkinter.CTkButton(self.month_frame,
                                               text=" ",
                                               hover_color=HOVER_COLOR,
                                               text_color=TEXT_COLOR2, 
                                               font=set_font(font_exam,24),
                                               fg_color=FG_COLOR,
                                               corner_radius=0,
                                               image=jun_image,command=self.event_junio)
        self.junio.grid(row=6,column=0,pady=5, sticky='nsew')
        jul_image=reader_image(Path_Image,'julio.png',(30,30))
        self.julio = customtkinter.CTkButton(self.month_frame,
                                               text=" ",
                                               hover_color=HOVER_COLOR,
                                               text_color=TEXT_COLOR2, 
                                               font=set_font(font_exam,24),
                                               fg_color=FG_COLOR,
                                               corner_radius=0,command=self.event_julio,image=jul_image)
        self.julio.grid(row=7,column=0,pady=5, sticky='nsew')
        ago_image=reader_image(Path_Image,'agosto.png',(30,30))
        self.agosto = customtkinter.CTkButton(self.month_frame,
                                               text=" ",
                                               hover_color=HOVER_COLOR,
                                               text_color=TEXT_COLOR2, 
                                               font=set_font(font_exam,24),
                                               fg_color=FG_COLOR,
                                               corner_radius=0,command=self.event_agosto,image=ago_image)
        self.agosto.grid(row=8,column=0,pady=5, sticky='nsew')
        sep_image=reader_image(Path_Image,'septiembre.png',(30,30))
        self.septiembre = customtkinter.CTkButton(self.month_frame,
                                               text=" ",
                                               hover_color=HOVER_COLOR,
                                               text_color=TEXT_COLOR2, 
                                               font=set_font(font_exam,24),
                                               fg_color=FG_COLOR,
                                               corner_radius=0,command=self.event_sep,image=sep_image)
        self.septiembre.grid(row=9,column=0,pady=5, sticky='nsew')
        oc_image=reader_image(Path_Image,'octubre.png',(30,30))
        self.octubre = customtkinter.CTkButton(self.month_frame,
                                               text=" ",
                                               hover_color=HOVER_COLOR,
                                               text_color=TEXT_COLOR2, 
                                               font=set_font(font_exam,24),
                                               fg_color=FG_COLOR,
                                               corner_radius=0,command=self.event_oct,image=oc_image)
        self.octubre.grid(row=10,column=0,pady=5, sticky='nsew')
        nov_image=reader_image(Path_Image,'noviembre.png',(30,30))
        self.noviembre = customtkinter.CTkButton(self.month_frame,
                                               text=" ",
                                               hover_color=HOVER_COLOR,
                                               text_color=TEXT_COLOR2, 
                                               font=set_font(font_exam,24),
                                               fg_color=FG_COLOR,
                                               corner_radius=0,command=self.event_nov,image=nov_image)
        self.noviembre.grid(row=11,column=0,pady=5, sticky='nsew')
        dec_image=reader_image(Path_Image,'diciembre.png',(30,30))
        self.diciembre = customtkinter.CTkButton(self.month_frame,
                                               text=" ",
                                               hover_color=HOVER_COLOR,
                                               text_color=TEXT_COLOR2, 
                                               font=set_font(font_exam,24),
                                               fg_color=FG_COLOR,
                                               corner_radius=0,command=self.event_dic,image=dec_image)
        self.diciembre.grid(row=12,column=0,pady=5, sticky='nsew')
        self.final_frame= customtkinter.CTkFrame(layout)
        self.final_frame.pack(side=tk.RIGHT,fill='both',expand=False)
        self.safe_buttom= customtkinter.CTkButton(self.final_frame,text='Guardar',text_color=TEXT_COLOR,font=set_font('Cascadia mono SemiBold', 18),fg_color=FG_COLOR,hover_color=HOVER_COLOR)
        self.safe_buttom.pack(fill='both', expand=True)
        self.layout=layout
        
    
        self.user_entry= Entry(layout)
        self.user_entry.pack(side=tk.RIGHT,fill='both',expand=True)
    def event_enero(self):
        self.change_window('Enero')
    def event_febrero(self):
        self.change_window('Febrero')
    def event_marzo(self):
        self.change_window('Marzo')
    def event_abril(self):
        self.change_window('Abril')
    def event_mayo(self):
        self.change_window('Mayo')
    def event_junio(self):
        self.change_window('Junio')
    def event_julio(self):
        self.change_window('Julio')
    def event_agosto(self):
        self.change_window('Agosto')
    def event_sep(self):
        self.change_window('Septiembre')
    def event_oct(self):
        self.change_window('Octubre')
    def event_nov(self):
        self.change_window('Noviembre')
    def event_dic(self):
        self.change_window('Diciembre')
        
    def change_window(self,month):
        #Instancia del Frame del centro son para poder pasarle por argumento en caso de existir datos en el mes
        if month == 'Enero':
            #Aqui debe ir una funcion que revise si hay datos en enero y le dice al usuario
            self.enero.configure(fg_color=BUTTOM_HOVER)
           
        else:
            self.enero.configure(fg_color='transparent')
            
        if month == 'Febrero':

            self.febrero.configure(fg_color=BUTTOM_HOVER)
        else:
            self.febrero.configure(fg_color='transparent')
            
        if month == 'Marzo':
            self.marzo.configure(fg_color=BUTTOM_HOVER)
        else:
            self.marzo.configure(fg_color='transparent')
        if month == 'Abril':
            self.abril.configure(fg_color=BUTTOM_HOVER)
        else:
            self.abril.configure(fg_color='transparent')
        if month == 'Mayo':
            self.mayo.configure(fg_color=BUTTOM_HOVER)
        else:
            self.mayo.configure(fg_color='transparent')
        if month == 'Junio':
            self.junio.configure(fg_color=BUTTOM_HOVER)
        else:
            self.junio.configure(fg_color='transparent')
        if month == 'Julio':
            self.julio.configure(fg_color=BUTTOM_HOVER)
        else:
            self.julio.configure(fg_color='transparent')
        if month == 'Agosto':
            self.agosto.configure(fg_color=BUTTOM_HOVER)
        else:
            self.agosto.configure(fg_color='transparent')
        if month == 'Septiembre':
            self.septiembre.configure(fg_color=BUTTOM_HOVER)
        else:
            self.septiembre.configure(fg_color='transparent')
        if month == 'Octubre':
            self.octubre.configure(fg_color=BUTTOM_HOVER)
        else:
            self.octubre.configure(fg_color='transparent')
        if month == 'Noviembre':
            self.noviembre.configure(fg_color=BUTTOM_HOVER)
        else:
            self.noviembre.configure(fg_color='transparent')
        if month == 'Diciembre':
            self.diciembre.configure(fg_color=BUTTOM_HOVER)
        else:
            self.diciembre.configure(fg_color='transparent')

class Entry(customtkinter.CTkFrame):
    def __init__(self,master):
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
            
        #self.domicilio_label = customtkinter.CTkLabel(self,text="Domicilio",
                                               #  text_color=TEXT_COLOR,
                                               #  font=set_font('Cascadia Mono'))
        #self.domicilio_label.grid(row=1, column=1,pady=5)
        


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

        #self.transporte_label = customtkinter.CTkLabel(self,text="Transporte",
        #                                         text_color=TEXT_COLOR,
        #                                         font=set_font('Cascadia Mono'))
        #self.transporte_label.grid(row=5, column=1,pady=5)
        self.transporte_var = customtkinter.StringVar()
        self.transporte_entry = customtkinter.CTkEntry(self,
                                                 text_color=TEXT_COLOR,placeholder_text="descripcion", 
                                                 font=set_font('Cascadia Mono'),
                                                 textvariable=self.transporte_var)
        self.transporte_entry.grid(row=3, column=4,pady=5)

        #self.entretenimiento_label = customtkinter.CTkLabel(self,text="Entretenimiento",
        #                                         text_color=TEXT_COLOR,
        #                                         font=set_font('Cascadia Mono'))
        #self.entretenimiento_label.grid(row=7, column=1,pady=5)
        self.entretenimiento_var = customtkinter.StringVar()
        self.entretenimiento_entry = customtkinter.CTkEntry(self,
                                                 text_color=TEXT_COLOR,placeholder_text="descripcion", 
                                                 font=set_font('Cascadia Mono'),
                                                 textvariable=self.entretenimiento_var)
        self.entretenimiento_entry.grid(row=4, column=4,pady=5)
        
        #self.deudas_label = customtkinter.CTkLabel(self,text="Deudas",
        #                                         text_color=TEXT_COLOR,
        #                                         font=set_font('Cascadia Mono'))
        #self.deudas_label.grid(row=9, column=1,pady=5)
        self.deudas_var = customtkinter.StringVar()
        self.deudas_entry = customtkinter.CTkEntry(self,
                                                 text_color=TEXT_COLOR,placeholder_text="descripcion", 
                                                 font=set_font('Cascadia Mono'),
                                                 textvariable=self.deudas_var)
        self.deudas_entry.grid(row=5, column=4,pady=5)

        #self.seguros_label = customtkinter.CTkLabel(self,text="Seguros",
        #                                         text_color=TEXT_COLOR,
        #                                         font=set_font('Cascadia Mono'))
        #self.seguros_label.grid(row=11, column=1,pady=5)
        self.seguros_var = customtkinter.StringVar()
        self.seguros_entry = customtkinter.CTkEntry(self,
                                                 text_color=TEXT_COLOR,placeholder_text="descripcion", 
                                                 font=set_font('Cascadia Mono'),
                                                 textvariable=self.seguros_var)
        self.seguros_entry.grid(row=6, column=4,pady=5)

        #self.servicios_label = customtkinter.CTkLabel(self,text="Servicios",
        #                                         text_color=TEXT_COLOR,
        #                                         font=set_font('Cascadia Mono'))
        #self.servicios_label.grid(row=13, column=1,pady=5)
        self.servicios_var = customtkinter.StringVar()
        self.servicios_entry = customtkinter.CTkEntry(self,
                                                 text_color=TEXT_COLOR,placeholder_text="descripcion", 
                                                 font=set_font('Cascadia Mono'),
                                                 textvariable=self.servicios_var)
        self.servicios_entry.grid(row=7, column=4,pady=5)

        #self.otros_label = customtkinter.CTkLabel(self,text="Otros",
        #                                         text_color=TEXT_COLOR,
        #                                         font=set_font('Cascadia Mono'))
        #self.otros_label.grid(row=15, column=1,pady=5)
        self.otros_var = customtkinter.StringVar()
        self.otros_entry = customtkinter.CTkEntry(self,
                                                 text_color=TEXT_COLOR,placeholder_text="descripcion", 
                                                 font=set_font('Cascadia Mono'),
                                                 textvariable=self.otros_var)
        self.otros_entry.grid(row=8, column=4,pady=5)
        

        

