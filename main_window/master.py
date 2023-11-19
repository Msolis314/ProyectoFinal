import customtkinter
import os
from PIL import Image

from tools.Usos import reader_image
from tools.Usos import center


global path_image
path_image=os.path.join(os.path.dirname(os.path.realpath("Documents")),r"./Imagenes")
class Panel(customtkinter.CTk):
    """Panel principal, hereda de CTk"""
    def __init__(self):
        super().__init__()
        self.title("Sistema de Login")
        w,h= self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w,h))
        self.resizable(False,False)
        
        self.welcomeimage = reader_image(path_image,"login.png",(1000,1000))
        self.label1= customtkinter.CTkLabel(self,text=' ', image=self.welcomeimage,bg_color='transparent')
        self.label1.place(x=0,y=0,relwidth=1,relheight=1)
        self.mainloop()

