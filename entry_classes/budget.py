"""Modulo para configurar la entrada del presupuesto
    """
import customtkinter
import tkinter as tk
import sqlite3
from .template import *
from system_vars import *
from tools.Usos import *
import system_vars.config as config

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
        self._date = None
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
                                                  hover_color=HOVER_COLOR,
                                                  command=self.event_guardar)
        self.safe_buttom.pack(fill='both', expand=True,pady=20)
        self.layout=layout
        
    
        self.user_entry= Entry(layout)
        self.user_entry.pack(side=tk.RIGHT,fill='both',expand=True)
    
        
    def change_window(self,month):
        """Funcion para elegir el mes 

        :param month: mes correspondiente al boton 
        :type month: string
        """
        self._date = None
        if month == 'Enero':
            #Aqui debe ir una funcion que revise si hay datos en enero y le dice al usuario
            if self.check_existing_data('Enero') == False:

                self.enero.configure(fg_color=BUTTOM_HOVER)
                self.user_entry.title_label.configure(text='Presupuesto Enero')
                self._date='Enero'
            else:
                mag = CTkMessagebox(title="?",message="Existen datos en el mes seleccionado desea reescribirlos?",icon="question", option_1="Cancel", option_2="No", option_3="Yes")
                response = mag.get()
                if response == 'Yes':
                    self.delete_row('Enero')
                    self.enero.configure(fg_color=BUTTOM_HOVER)
                    self.user_entry.title_label.configure(text='Presupuesto Enero')
                    self._date='Enero'
                else:
                    self._date=None
                    self.enero.configure(fg_color='transparent')

           
        else:
            self.enero.configure(fg_color='transparent')
            
        if month == 'Febrero':
            if self.check_existing_data('Febrero') == False:

                self.febrero.configure(fg_color=BUTTOM_HOVER)
                self.user_entry.title_label.configure(text='Presupuesto Febrero')
                self._date='Febrero'
            else:
                mag = CTkMessagebox(title="?",message="Existen datos en el mes seleccionado desea reescribirlos?",icon="question", option_1="Cancel", option_2="No", option_3="Yes")
                response = mag.get()
                if response == 'Yes':
                    self.delete_row('Febrero')
                    self.febrero.configure(fg_color=BUTTOM_HOVER)
                    self.user_entry.title_label.configure(text='Presupuesto Febrero')
                    self._date='Febrero'
                else:
                    self._date=None
                    self.febrero.configure(fg_color='transparent')

        else:
            self.febrero.configure(fg_color='transparent')
            
        if month == 'Marzo':
            if self.check_existing_data('Marzo') == False:

                self.marzo.configure(fg_color=BUTTOM_HOVER)
                self.user_entry.title_label.configure(text='Presupuesto Marzo')
                self._date='Marzo'
            else:
                mag = CTkMessagebox(title="?",message="Existen datos en el mes seleccionado desea reescribirlos?",icon="question", option_1="Cancel", option_2="No", option_3="Yes")
                response = mag.get()
                if response == 'Yes':
                    self.delete_row('Marzo')
                    self.marzo.configure(fg_color=BUTTOM_HOVER)
                    self.user_entry.title_label.configure(text='Presupuesto Marzo')
                    self._date='Marzo'
                else:
                    self._date=None
                    self.marzo.configure(fg_color='transparent')
        else:
            self.marzo.configure(fg_color='transparent')
        if month == 'Abril':
            if self.check_existing_data('Abril') == False:

                self.abril.configure(fg_color=BUTTOM_HOVER)
                self.user_entry.title_label.configure(text='Presupuesto Abril')
                self._date='Abril'
            else:
                mag = CTkMessagebox(title="?",message="Existen datos en el mes seleccionado desea reescribirlos?",icon="question", option_1="Cancel", option_2="No", option_3="Yes")
                response = mag.get()
                if response == 'Yes':
                    self.delete_row('Enero')
                    self.abril.configure(fg_color=BUTTOM_HOVER)
                    self.user_entry.title_label.configure(text='Presupuesto Enero')
                    self._date='Abril'
                else:
                    self._date=None
                    self.abril.configure(fg_color='transparent')
        else:
            self.abril.configure(fg_color='transparent')
        if month == 'Mayo':
            if self.check_existing_data('Mayo') == False:

                self.mayo.configure(fg_color=BUTTOM_HOVER)
                self.user_entry.title_label.configure(text='Presupuesto Enero')
                self._date='Mayo'
            else:
                mag = CTkMessagebox(title="?",message="Existen datos en el mes seleccionado desea reescribirlos?",icon="question", option_1="Cancel", option_2="No", option_3="Yes")
                response = mag.get()
                if response == 'Yes':
                    self.delete_row('Mayo')
                    self.mayo.configure(fg_color=BUTTOM_HOVER)
                    self.user_entry.title_label.configure(text='Presupuesto Mayo')
                    self._date='Mayo'
                else:
                    self._date=None
                    self.mayo.configure(fg_color='transparent')
        else:
            self.mayo.configure(fg_color='transparent')
        if month == 'Junio':
            if self.check_existing_data('Junio') == False:

                self.junio.configure(fg_color=BUTTOM_HOVER)
                self.user_entry.title_label.configure(text='Presupuesto Junio')
                self._date='Junio'
            else:
                mag = CTkMessagebox(title="?",message="Existen datos en el mes seleccionado desea reescribirlos?",icon="question", option_1="Cancel", option_2="No", option_3="Yes")
                response = mag.get()
                if response == 'Yes':
                    self.delete_row('Junio')
                    self.junio.configure(fg_color=BUTTOM_HOVER)
                    self.user_entry.title_label.configure(text='Presupuesto Junio')
                    self._date='Junio'
                else:
                    self._date=None
                    self.junio.configure(fg_color='transparent')
        else:
            self.junio.configure(fg_color='transparent')
        if month == 'Julio':
            if self.check_existing_data('Julio') == False:

                self.julio.configure(fg_color=BUTTOM_HOVER)
                self.user_entry.title_label.configure(text='Presupuesto Julio')
                self._date='Julio'
            else:
                mag = CTkMessagebox(title="?",message="Existen datos en el mes seleccionado desea reescribirlos?",icon="question", option_1="Cancel", option_2="No", option_3="Yes")
                response = mag.get()
                if response == 'Yes':
                    self.delete_row('Julio')
                    self.julio.configure(fg_color=BUTTOM_HOVER)
                    self.user_entry.title_label.configure(text='Presupuesto Julio')
                    self._date='Julio'
                else:
                    self._date=None
                    self.julio.configure(fg_color='transparent')
            self.julio.configure(fg_color=BUTTOM_HOVER)
            self.user_entry.title_label.configure(text='Presupuesto Julio')
            self._date = 'Julio'
        else:
            self.julio.configure(fg_color='transparent')
        if month == 'Agosto':
            if self.check_existing_data('Agosto') == False:

                self.agosto.configure(fg_color=BUTTOM_HOVER)
                self.user_entry.title_label.configure(text='Presupuesto Agosto')
                self._date='Agosto'
            else:
                mag = CTkMessagebox(title="?",message="Existen datos en el mes seleccionado desea reescribirlos?",icon="question", option_1="Cancel", option_2="No", option_3="Yes")
                response = mag.get()
                if response == 'Yes':
                    self.delete_row('Agosto')
                    self.agosto.configure(fg_color=BUTTOM_HOVER)
                    self.user_entry.title_label.configure(text='Presupuesto Agosto')
                    self._date='Agosto'
                else:
                    self._date=None
                    self.agosto.configure(fg_color='transparent')
            
        else:
            self.agosto.configure(fg_color='transparent')
        if month == 'Septiembre':
            if self.check_existing_data('Septiembre') == False:

                self.septiembre.configure(fg_color=BUTTOM_HOVER)
                self.user_entry.title_label.configure(text='Presupuesto Septiembre')
                self._date='Septiembre'
            else:
                mag = CTkMessagebox(title="?",message="Existen datos en el mes seleccionado desea reescribirlos?",icon="question", option_1="Cancel", option_2="No", option_3="Yes")
                response = mag.get()
                if response == 'Yes':
                    self.delete_row('Septiembre')
                    self.septiembre.configure(fg_color=BUTTOM_HOVER)
                    self.user_entry.title_label.configure(text='Presupuesto Septiembre')
                    self._date='Septiembre'
                else:
                    self._date=None
                    self.septiembre.configure(fg_color='transparent')
            
        else:
            self.septiembre.configure(fg_color='transparent')
        if month == 'Octubre':
            if self.check_existing_data('Octubre') == False:

                self.octubre.configure(fg_color=BUTTOM_HOVER)
                self.user_entry.title_label.configure(text='Presupuesto Octubre')
                self._date='Octubre'
            else:
                mag = CTkMessagebox(title="?",message="Existen datos en el mes seleccionado desea reescribirlos?",icon="question", option_1="Cancel", option_2="No", option_3="Yes")
                response = mag.get()
                if response == 'Yes':
                    self.delete_row('Octubre')
                    self.octubre.configure(fg_color=BUTTOM_HOVER)
                    self.user_entry.title_label.configure(text='Presupuesto Octubre')
                    self._date='Octubre'
                else:
                    self._date=None
                    self.octubre.configure(fg_color='transparent')
            
        else:
            self.octubre.configure(fg_color='transparent')
        if month == 'Noviembre':
            if self.check_existing_data('Noviembre') == False:

                self.noviembre.configure(fg_color=BUTTOM_HOVER)
                self.user_entry.title_label.configure(text='Presupuesto Noviembre')
                self._date='Noviembre'
            else:
                mag = CTkMessagebox(title="?",message="Existen datos en el mes seleccionado desea reescribirlos?",icon="question", option_1="Cancel", option_2="No", option_3="Yes")
                response = mag.get()
                if response == 'Yes':
                    self.delete_row('Noviembre')
                    self.noviembre.configure(fg_color=BUTTOM_HOVER)
                    self.user_entry.title_label.configure(text='Presupuesto Noviembre')
                    self._date='Noviembre'
                else:
                    self._date=None
                    self.noviembre.configure(fg_color='transparent')
            
        else:
            self.noviembre.configure(fg_color='transparent')
        if month == 'Diciembre':
            if self.check_existing_data('Diciembre') == False:

                self.diciembre.configure(fg_color=BUTTOM_HOVER)
                self.user_entry.title_label.configure(text='Presupuesto Diciembre')
                self._date='Diciembre'
            else:
                mag = CTkMessagebox(title="?",message="Existen datos en el mes seleccionado desea reescribirlos?",icon="question", option_1="Cancel", option_2="No", option_3="Yes")
                response = mag.get()
                if response == 'Yes':
                    self.delete_row('Diciembre')
                    self.diciembre.configure(fg_color=BUTTOM_HOVER)
                    self.user_entry.title_label.configure(text='Presupuesto Diciembre')
                    self._date='Diciembre'
                else:
                    self._date=None
                    self.diciembre.configure(fg_color='transparent')

        else:
            self.diciembre.configure(fg_color='transparent')
    def event_guardar(self):
        """Aqui se debe verificar las entradas del usuario y escribirlas en la base de datos
        """
        data =self.user_entry.get_data()
        data.insert(0,self._date)
        newdata = tuple(data)
        print(newdata)
        if self._date == None:
            CTkMessagebox(title="Error", message='Debe elegir una fecha',icon='cancel')
            raise ExceptionSystem("Error en la escritura")
        if data != None and self._date != None:
            self.write_data(newdata)
            self._date=None
            self.user_entry.title_label.configure(text="Presupuesto")
            self.user_entry.clean_entry()
        else:
            CTkMessagebox(title="Error", message="Error al escribir en la base de datos",icon='cancel')

    def write_data(self,data):
        """Funcion para escribir en la base de datos

        :param data: tuple con los valores de las entradas de categoria de presupuesto
        :type data: tuple de floats
        """
        escribir_valores = '''
        INSERT INTO presupuesto (mes, Domicilio,Higiene , Transporte,Entretenimiento,Deudas,Seguros,Vestimenta,Servicios,Otros)
        VALUES (?, ?, ?, ?, ?, ?,?,?,?,?)
        '''
        current_data_base = f'{config.currentuser}.db'
        self.conn = sqlite3.connect(current_data_base)
        self.conn.execute(escribir_valores, data)
        self.conn.commit()
        self.conn.close()
        CTkMessagebox(title="info",message='Datos ingresados exitosamente')
    def check_existing_data(self,month):
        """Función para verificar si ya existen datos para un mes dado.

        :param date: Mes para el cual se quiere verificar la existencia de datos.
        :type date: str
        :return: True si existen datos, False si no.
        :rtype: bool
        """
        query = "SELECT COUNT(*) FROM presupuesto WHERE mes = ?"
        current_data_base = f'{config.currentuser}.db'

        conn = sqlite3.connect(current_data_base)
        date = month
        cursor = conn.cursor()
        cursor.execute(query, (date,))
        count = cursor.fetchone()[0]
        conn.close

        return count > 0
    def delete_row(self,month):
        current_data_base = f'{config.currentuser}.db'

        conn = sqlite3.connect(current_data_base)
        date = month
        cursor = conn.cursor()
        query = "DELETE FROM presupuesto WHERE mes = ?;"
        cursor.execute(query, (date,))
        conn.commit()
        conn.close()
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
        self.grid_rowconfigure(11,weight=1)
        self.title_frame=customtkinter.CTkFrame(self,fg_color=FG_COLOR)
        self.title_frame.grid(row=0,column=3,sticky='nsew')
        self.title_label = customtkinter.CTkLabel(self.title_frame,text="Presupuesto",
                                                 text_color=TEXT_COLOR,
                                                 font=set_font('Cascadia Mono SemiBold',15))
        self.title_label.pack(side=tk.TOP,fill=tk.BOTH,expand=True)
        economy_atr=['Domicilio','Higiene','Transporte','Entretenimiento','Deudas','Seguros','Vestimenta','Servicios','Otros']
        for index,atr in enumerate(economy_atr):
            customtkinter.CTkLabel(self,text=atr,text_color=TEXT_COLOR,
                                                 font=set_font('Cascadia Mono')).grid(row = 1+ index, column=1,pady=5,padx=5)
            
        #Casillas para la entrada de datos
        self.domicilio_var = customtkinter.StringVar(value='0')
        self.domicilio_entry = customtkinter.CTkEntry(self,
                                                 text_color=TEXT_COLOR,placeholder_text="descripcion", 
                                                 font=set_font('Cascadia Mono'),
                                                 textvariable=self.domicilio_var)
        self.domicilio_entry.grid(row=1, column=4,pady=5)
    
        self.higiene_var = customtkinter.StringVar(value='0')
        self.higiene_entry = customtkinter.CTkEntry(self,
                                                 text_color=TEXT_COLOR,placeholder_text="descripcion", 
                                                 font=set_font('Cascadia Mono'),
                                                 textvariable=self.higiene_var)
        self.higiene_entry.grid(row=2, column=4,pady=5)

        
        self.transporte_var = customtkinter.StringVar(value='0')
        self.transporte_entry = customtkinter.CTkEntry(self,
                                                 text_color=TEXT_COLOR,placeholder_text="descripcion", 
                                                 font=set_font('Cascadia Mono'),
                                                 textvariable=self.transporte_var)
        self.transporte_entry.grid(row=3, column=4,pady=5)

        
        self.entretenimiento_var = customtkinter.StringVar(value='0')
        self.entretenimiento_entry = customtkinter.CTkEntry(self,
                                                 text_color=TEXT_COLOR,placeholder_text="descripcion", 
                                                 font=set_font('Cascadia Mono'),
                                                 textvariable=self.entretenimiento_var)
        self.entretenimiento_entry.grid(row=4, column=4,pady=5)
        
        
        self.deudas_var = customtkinter.StringVar(value='0')
        self.deudas_entry = customtkinter.CTkEntry(self,
                                                 text_color=TEXT_COLOR,placeholder_text="descripcion", 
                                                 font=set_font('Cascadia Mono'),
                                                 textvariable=self.deudas_var)
        self.deudas_entry.grid(row=5, column=4,pady=5)

        
        self.seguros_var = customtkinter.StringVar(value='0')
        self.seguros_entry = customtkinter.CTkEntry(self,
                                                 text_color=TEXT_COLOR,placeholder_text="descripcion", 
                                                 font=set_font('Cascadia Mono'),
                                                 textvariable=self.seguros_var)
        self.seguros_entry.grid(row=6, column=4,pady=5)
        self.vestimenta_var = customtkinter.StringVar(value='0')
        self.vestimenta_entry = customtkinter.CTkEntry(self,
                                                 text_color=TEXT_COLOR,placeholder_text="descripcion", 
                                                 font=set_font('Cascadia Mono'),
                                                 textvariable=self.vestimenta_var)
        self.vestimenta_entry.grid(row=7, column=4,pady=5)

        
        self.servicios_var = customtkinter.StringVar(value='0')
        self.servicios_entry = customtkinter.CTkEntry(self,
                                                 text_color=TEXT_COLOR,placeholder_text="descripcion", 
                                                 font=set_font('Cascadia Mono'),
                                                 textvariable=self.servicios_var)
        self.servicios_entry.grid(row=8, column=4,pady=5)

        
        self.otros_var = customtkinter.StringVar(value='0')
        self.otros_entry = customtkinter.CTkEntry(self,
                                                 text_color=TEXT_COLOR,placeholder_text="descripcion", 
                                                 font=set_font('Cascadia Mono'),
                                                 textvariable=self.otros_var)
        self.otros_entry.grid(row=9, column=4,pady=5)
        self.money_frame=customtkinter.CTkFrame(self,fg_color=FG_COLOR)
        self.money_frame.grid(row=10,column=3,sticky='nsew')
        self.coin_label = customtkinter.CTkLabel(self.money_frame,
                                                text='Tipo de cambio',
                                                font=set_font(), 
                                                text_color=TEXT_COLOR)
        self.coin_label.pack(side= tk.TOP, fill = 'both',expand=True)
        self.coin_var=customtkinter.StringVar(value="Dolar")
        self.coin_entry = customtkinter.CTkSegmentedButton(self.money_frame, values=["Dólar", "Colón", "Euro"],
                                                     font=set_font('Shanti'),
                                                     variable=self.coin_var)
        self.coin_entry.pack(side= tk.BOTTOM, fill = 'both',expand=True)
    def get_data(self):
        """Funcion para recopilar los datos de las entradas, toma los datos y los pasa por la funcion que los convierte en float
        Todavia da error, necesita que se la revise
        ....
        :return: lista con los valores convertidos a colones
        :rtype: lista de floats
        """
        tuple_data = (self.domicilio_var.get(),self.higiene_var.get(),self.transporte_var.get(),self.entretenimiento_var.get(),self.deudas_var.get(),self.seguros_var.get(),self.vestimenta_var.get(),self.servicios_var.get(),self.otros_var.get())
        check_tuple = []
        money_type = self.coin_var.get()
        check_tuple = list(map(lambda x : valid_amount(x,money_type),tuple_data))
        """for item in check_tuple:
            if item == False:
                CTkMessagebox(title="Error",message='Valor invalido')
                self.clean_entry()
                raise ExceptionSystem('Error en la entrada de datos')"""
        return check_tuple
    def clean_entry(self):
        """Funcion para limpiar las entradas una vez se guardan los datos
        """
        self.domicilio_entry.delete(0,'end')
        self.domicilio_entry.insert(0,'0')
        self.domicilio_var = customtkinter.StringVar(value='0')
        self.higiene_entry.delete(0,'end')
        self.higiene_entry.insert(0,'0')
        self.higiene_var = customtkinter.StringVar(value='0')
        self.transporte_entry.delete(0,'end')
        self.transporte_entry.insert(0,'0')
        self.transporte_var = customtkinter.StringVar(value='0')
        self.entretenimiento_entry.delete(0,'end')
        self.entretenimiento_entry.insert(0,'0')
        self.entretenimiento_var = customtkinter.StringVar(value='0')
        self.deudas_entry.delete(0,'end')
        self.deudas_entry.insert(0,'0')
        self.deudas_var = customtkinter.StringVar(value='0')
        self.seguros_entry.delete(0,'end')
        self.seguros_entry.insert(0,'0')
        self.seguros_var = customtkinter.StringVar(value='0')
        self.vestimenta_entry.delete(0,'end')
        self.vestimenta_entry.insert(0,'0')
        self.vestimenta_var = customtkinter.StringVar(value='0')
        self.servicios_entry.delete(0,'end')
        self.servicios_entry.insert(0,'0')
        self.servicios_var  = customtkinter.StringVar(value='0')
        self.otros_entry.delete(0,'end')
        self.otros_entry.insert(0,'0')
        self.otros_var = customtkinter.StringVar(value='0')
    

        

