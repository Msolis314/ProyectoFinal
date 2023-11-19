import customtkinter
import ttkbootstrap as tk
import os
from tools.Usos import reader_image
from tools.Usos import center
from tools.Usos import set_font 
from system_vars.Vars import COLOR_BG
from system_vars.Vars import TEXT_COLOR, HOVER_COLOR,BUTTOM_HOVER

global path_image
path_image=os.path.join(os.path.dirname(os.path.realpath("Documents")),r"./Imagenes")
class AbstractLogin(customtkinter.CTk):
    """Clase abstracta con el frame del login"""
    def __init__(self):
        super().__init__()
        self.title("Sign in")
        self.geometry('800x500')
        self.resizable(False,False)
        center(self,800,500)

        self.login_image = reader_image(path_image,"login.png",(350,350))
        #Frames
        self.frame_image= customtkinter.CTkFrame(self,border_width=0,width=300,fg_color=COLOR_BG,)
        self.frame_image.pack(
                         side="left",
                         expand=tk.NO,
                         fill=tk.BOTH,
                         )
        self.label_image=customtkinter.CTkLabel(self.frame_image,
                                           image=self.login_image, 
                                           text="")
        self.label_image.place(x=0,y=0,relwidth=1,relheight=1)

        #Frame de login
        self.login_frame= customtkinter.CTkFrame(self, border_width=0)
        self.login_frame.pack(side='right',expand=tk.YES,fill=tk.BOTH)
        #Frame para el titulo de Sign up
        self.upper_title_frame= customtkinter.CTkFrame(self.login_frame,height=40,border_width=0,fg_color='transparent')
        self.upper_title_frame.pack(side='top',fill=tk.X)
        self.label_title=customtkinter.CTkLabel(self.upper_title_frame,text="Sign in",
                                                font=set_font('Cascadia Mono SemiBold',25),
                                                text_color=TEXT_COLOR,pady=50)
        self.label_title.pack(expand=tk.YES,fill=tk.BOTH)

        #Frame para la entrada el usuario
        self.user_entry_frame=customtkinter.CTkFrame(self.login_frame, border_width=0,fg_color='transparent')
        self.user_entry_frame.pack(side='bottom',expand=tk.YES,fill=tk.BOTH)
        #Widgets de entrada 
        self.user_label= customtkinter.CTkLabel(self.user_entry_frame,text='User',
                                                font=set_font('Cascadia Mono',13),
                                                text_color=TEXT_COLOR,
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
                                                text_color=TEXT_COLOR,
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
        self.login_buttom=customtkinter.CTkButton(self.user_entry_frame,
                                                  text='Login',
                                                  font=set_font('Cascadia Mono',13),
                                                  border_width=2,
                                                  hover_color=BUTTOM_HOVER,
                                                  command=self.checkpass)
        self.login_buttom.pack(fill=tk.X,padx=20,pady=40)
        self.login_buttom.bind("<Return>",(lambda event: self.checkpass()))
        self.regi_buttom=customtkinter.CTkButton(self.user_entry_frame,
                                                  text='Sing up',
                                                  font=set_font('Cascadia Mono',13),
                                                  border_width=2,
                                                  hover_color=BUTTOM_HOVER,
                                                  command=self.registration)
        self.regi_buttom.pack(fill=tk.X,padx=20,pady=40)
        self.regi_buttom.bind("<Return>",(lambda event: self.registration()))


        self.mainloop()
    
    def checkpass(self):
        pass
    def registration(self):
        pass



