import customtkinter
import os
from PIL import Image
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
def reader_image(path,name, tam= (20,20)):
    """Funcion para leer imagenes

    :param path: directorio donde esta la imagen
    :type path: str
    :param name: nombre de la imagen
    :type name: string
    :param tam: size que se quiere de la imagen
    :type tam: int 
    .....

    :return: carga la imagen con la funcion customtkinter.CTkImage
    :rtype: CTkImage
    """
    try:
        return customtkinter.CTkImage(Image.open(os.path.join(path,name)), size=tam)
    except FileNotFoundError as e:
        print(f"Error al cargar las imagenes: {e}")
        
def center(screen, weight_app, height_app):
    """Funcion para colocar la ventana en el centro de la pantalla
    
    :param screen : objeto de pantalla
    :type screen: CTk
    :param weight_app:ancho ventana
    :type weight_app:int
    :param height_app:largo ventana
    :type height_app: int 
    
    ........
    :return:Geometria de ventana
    :rtype: instancia de CTk
    """
    screen_weight= screen.winfo_screenwidth()
    screen_height= screen.winfo_screenheight()
    # Calcular la posicion en x y y de la ventana
    """
    Tengo que obtener el offset por tanto 
    resto la mitad de lo valores de altura 
    de pantalla y ventana"""
    y = int((screen_height/2)-(height_app/2))
    x = int((screen_weight/2)- (weight_app/2))

    # Retorna lo debe ir en geometru
    return screen.geometry(f"{weight_app}x{height_app}+{x}+{y}")

def set_font(family='Cascadia mono',tam=12):
    ''' Funcion para setear una fuente'''
    try:
        return customtkinter.CTkFont(family=family, size=tam)
    except:
        return customtkinter.CTkFont(family='Cascadia mono', size=tam)
    
class ExceptionSystem(Exception):
    ''' Clase para el manejo de excepciones'''
    def __init__(self, mensaje="Error"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def convertir_moneda(amount:float, coin_type:str = 'Colón'):
    if coin_type == 'Dólar':
        return amount*532
    elif coin_type == 'Euro':
        return amount*580.44
    elif coin_type == 'Colón':
        return amount
    else: 
        return False