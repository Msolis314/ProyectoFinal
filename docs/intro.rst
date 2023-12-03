
Desarrollo Teórico
------------------
Para la construcción de la interfaz gráfica se utilizó la biblioteca 'tkinter', que viene por defecto en Python, y un derivado de esta llamado 'customtkinter', que permite crear aplicaciones con una apariencia más moderna. Para el desarrollo de la estructura de la aplicación, se hizo uso de la documentación de tkinter y customtkinter, así como de tutoriales. Según (Amos, 2022), el elemento base de una GUI es la ventana, y en ella se van incorporando otras estructuras conocidas como 'widgets'. La primera ventana de la aplicación es creada en el submódulo 'interfaz_login', heredando de la clase que proporciona la biblioteca 'customtkinter' para crear ventanas. Cabe señalar que la programación de toda la interfaz gráfica se realizó siguiendo el paradigma de programación orientada a objetos. Por ende, las clases son en la mayoría de los casos hijas de alguna de las clases predefinidas por 'customtkinter'::
  class AbstractLogin(customtkinter.CTk)
Después de crearse la ventana principal, se le pueden agregar otros elementos, cada uno definido por una clase particular. Algunos de los más utilizados en el presente trabajo son:



.. csv-table::
   :header: "Widget", "Tipo", "Descripcion" 
   :widths: 15, 10, 30 

   "Label", "CTkLabel", "Caja de texto"
   "Entry", "CTkEntry", "Entradas de texto"
   "Botón", "CTkButton", "Botón con alguna acción"
   
   
La biblioteca de 'customtkinter' permite modificar muchos de los atributos de estos elementos, como el color de fondo o el tipo de texto, para mejorar el diseño de la aplicación. Además, para posicionarlos en los diferentes frames (widgets especializados para dividir la ventana), existen 3 métodos según (Bansal, R. 2023):

 1. pack(), el cual va distribuyendo los widgets en bloques para luego posicionarlos en la ventana principal. El tamaño que ocupa cada bloque lo define el propio widget, además permite centrarlo con distintas opciones.
 2. grid(), organiza los widgets en una matriz definida por el programador.
 3. place(), posición en x y y del widget.
 
En la mayoría de los casos, se hizo uso de grid() por la flexibilidad para determinar el acomodo en filas y columnas; no obstante, también se utilizó pack() para apilar frames o posicionar widgets en lugares relativos. De hecho, según (Shipman, 2013), el método grid() soporta diferentes atributos para acomodar distancias relativas en la aplicación. Se hizo uso de las opciones pady y padx para configurar las distancias alrededor del objeto. Además, es importante notar que los distintos métodos de posicionamiento no se pueden combinar en un mismo frame.

Otro aspecto a considerar para la creación de una aplicación es el manejo de eventos. Por defecto, para ejecutar cualquier ventana en tkinter, se debe llamar al método mainloop(), el cual se encarga de crear un bucle infinito que responde cuando sucede algún evento. Un evento, como lo destaca (Amos, 2022), es cualquier acción que desencadene un efecto para la GUI, como presionar un botón o seleccionar una opción. Internamente, la biblioteca se encarga de la gestión de estos eventos manteniendo una lista de los eventos ocurridos y escribiendo cualquier nuevo evento que se necesite agregar. Es importante mencionar que se hace un gran uso de las funciones tipo callback. Por ejemplo, cuando se desea dar alguna funcionalidad a un botón, se le pasa por argumento a command la función deseada.

Por ende, para la creación de la interfaz, se utilizaron tres principios:

 1. Crear widgets para los componentes de la GUI.
 2. Posicionar los widgets siguiendo cierta geometría según el método.
 3. Dar funcionalidad por medio de eventos.

Cabe mencionar que, por motivos estéticos, se hizo uso de una librería derivada de tkinter creada por Tom Schimansky llamada 'customtkinter'. Esta librería permite crear widgets con un aspecto más moderno e interactivo y, además, se puede mezclar con otras funcionalidades de la librería tkinter. Otro módulo de terceros utilizado fue CTkmessagebox, el cual agrega la funcionalidad de proporcionar ventanas de mensajes a la interfaz, lo cual resulta muy útil para gestionar las interacciones con el usuario.

En lo referente a la interfaz, también se utilizó la biblioteca PILLOW para el procesamiento de las imágenes en conjunto con las funcionalidades propias de 'customtkinter'. Específicamente, se utilizó el comando Image en conjunto con la funcionalidad CTkimage para contener imágenes de la siguiente forma::

.. code-block:: python

	try:
        return customtkinter.CTkImage(Image.open(os.path.join(path,name)), size=tam)
    except FileNotFoundError as e:
        print(f"Error al cargar las imagenes: {e}")
        
Código que se encuentra en: 

.. function:: reader_image
   :module: tools.Usos
   
   función para leer imagenes

Instalación
-----------

Uso 
---

