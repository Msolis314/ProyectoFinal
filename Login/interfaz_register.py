import customtkinter
import ttkbootstrap as tk
import os
from CTkMessagebox import CTkMessagebox
from tools.Usos import reader_image
from tools.Usos import center
from tools.Usos import set_font 
from tablesetting.users_mem import Usuario_mem
from tablesetting.tablelogin import Usuario
import tools.crypto as cr
from system_vars.Vars import TEXT_COLOR, HOVER_COLOR,BUTTOM_HOVER,TEXT_COLOR2

global path_image
path_image=os.path.join(os.path.dirname(os.path.realpath("Documents")),r"./Imagenes")
print(path_image)
class Register(customtkinter.CTkToplevel):
    """Clase para el registro de usuario"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Sign in")
        self.resizable(False,False)
        center(self,800,500)
        self.usuario_mem= Usuario_mem()

        self.regi_image = reader_image(path_image,"2968290.jpg",(350,350))
        #Frames.
        self.frame_image= customtkinter.CTkFrame(self,border_width=0,width=300,fg_color='#FFFFFF')
        self.frame_image.pack(
                         side="left",
                         expand=tk.NO,
                         fill=tk.BOTH,
                         )
        self.label_image=customtkinter.CTkLabel(self.frame_image,
                                           image=self.regi_image, 
                                           text="")
        self.label_image.place(x=0,y=0,relwidth=1,relheight=1)

        #Frame de login
        self.login_frame= customtkinter.CTkFrame(self, border_width=0)
        self.login_frame.pack(side='right',expand=tk.YES,fill=tk.BOTH)
        #Frame para el titulo de Sign up
        self.upper_title_frame= customtkinter.CTkFrame(self.login_frame,height=40,border_width=0,fg_color='transparent')
        self.upper_title_frame.pack(side='top',fill=tk.X)
        self.label_title=customtkinter.CTkLabel(self.upper_title_frame,text="Sign up",
                                                font=set_font('Cascadia Mono SemiBold',25),
                                                text_color=TEXT_COLOR2,pady=50)
        self.label_title.pack(expand=tk.YES,fill=tk.BOTH)

        #Frame para la entrada el usuario
        self.user_entry_frame=customtkinter.CTkFrame(self.login_frame, border_width=0,fg_color='#E1E1E1')
        self.user_entry_frame.pack(side='bottom',expand=tk.YES,fill=tk.BOTH)
        #Widgets de entrada 
        self.user_label= customtkinter.CTkLabel(self.user_entry_frame,text='User',
                                                font=set_font('Cascadia Mono',13),
                                                text_color=TEXT_COLOR2,
                                                anchor='w')
        self.user_label.pack(fill=tk.X,padx=20,pady=6)
        self.User=customtkinter.CTkEntry(self.user_entry_frame,
                                         font=set_font('Cascadia Mono',13))
        self.User.pack(fill=tk.X,
                       padx=20,
                       pady=6
                       )
        self.password_label=customtkinter.CTkLabel(self.user_entry_frame,text='Password',
                                                font=set_font('Cascadia Mono',13),
                                                text_color=TEXT_COLOR2,
                                                anchor='w')
        self.password_label.pack(fill=tk.X,
                       padx=20,
                       pady=6)
        self.password=customtkinter.CTkEntry(self.user_entry_frame,
                                             font=set_font('Cascadia Mono',13))
        self.password.pack(fill=tk.X,
                       padx=20,
                       pady=6
                       )
        self.password.configure(show="*")
        self.password_confirm_label=customtkinter.CTkLabel(self.user_entry_frame,text='Confirm Password',
                                                font=set_font('Cascadia Mono',13),
                                                text_color=TEXT_COLOR2,
                                                anchor='w')
        self.password_confirm_label.pack(fill=tk.X,
                       padx=20,
                       pady=6)
        self.password_confirm=customtkinter.CTkEntry(self.user_entry_frame,
                                             font=set_font('Cascadia Mono',13))
        self.password_confirm.pack(fill=tk.X,
                       padx=20,
                       pady=6
                       )
        self.password_confirm.configure(show="*")
        self.regi_buttom=customtkinter.CTkButton(self.user_entry_frame,
                                                  text='Sing up',
                                                  font=set_font('Cascadia Mono',13),
                                                  border_width=2,
                                                  hover_color=BUTTOM_HOVER,
                                                  fg_color='#FF535F',
                                                  command=self.completeregister)
        self.regi_buttom.pack(fill=tk.X,padx=20,pady=40)
        self.regi_buttom.bind("<Return>",(lambda event: self.completeregister()))
    def User_not_in(self, usuario ):
        """Funcion para verificar que el usuario no esta en la base de datos"""
        check = True
        if (usuario !=None):
            check = False
            CTkMessagebox(title="Error",message='Usuario Registrado',icon='cancel')
            self.User.delete(0,tk.END)
        return check


    def valid_pass(self):
        """Funcion para verificar si la entrada del password es igual a la verificacion"""
        check = True
        #Si las contras no son iguales da un mensaje de error, igual si es una contra vacia
        if not (self.password.get().strip()):
            check=False
            CTkMessagebox(title="Error",message='Digite un contraseña',icon='cancel')
            self.password.delete(0,tk.END)
            self.password_confirm.delete(0,tk.END)
        if (self.password.get() != self.password_confirm.get()):
            check = False
            CTkMessagebox(title="Error",message='Contraseñas no iguales',icon='cancel')
            self.password.delete(0,tk.END)
            self.password_confirm.delete(0,tk.END)
        return check

    def completeregister(self):
        if (self.valid_pass()):
            #Creo una instancia de la tabla
            usuario = Usuario()
            usuario.username = self.User.get()
            #Busco la entrada del usuario en la base de datos, retorna none en caso de que no exista
            search_user : Usuario  = self.usuario_mem.get_user(self.User.get())
            # Si no existe significa que se puede seguir con el registro
            if  (self.User_not_in(search_user)):
                usuario.password = cr.crypting_pass(self.password.get())
                self.usuario_mem.new_user(usuario)
                CTkMessagebox(title='Message',message='Registro completado')
                self.destroy()

                

            



    
