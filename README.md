<a name="readme-top"></a>

<details>
  <summary>Contenidos</summary>
  <ol>
    <li><a href="#acerca-del-proyecto">Acerca del proyecto</a></li>
    <li>
      <a href="#comenzar">Comenzar</a>
      <ul>
        <li><a href="#dependencias">Dependencias</a></li>
        <li><a href="#instalación">Instalación</a></li>
      </ul>
    </li>
    <li><a href="#uso">Uso</a></li>
    <li><a href="#Funcionamiento">Funcionamiento</a></li>
  </ol>
</details>

## Acerca del proyecto

El proyecto consiste en una solución informática para el control del presupuesto personal por mes. Esto se efectúa por medio de una aplicación desarrollada en Python, la cual cuenta con una interfaz gráfica para la interacción con el usuario, el cual puede crear una cuenta personal para gestionar en su perfil información de las finanzas mensuales.

La aplicación permite el registro de ingresos para cada uno de los meses del año. Estos ingresos pueden ser clasificados en diferentes categorías predefinidas, a saber:

* Salario
* Ventas
* Comisiones
* Otros

Además, se pueden registrar gastos por categoría. Para cada mes, el usuario puede definir un presupuesto planificado; es decir, los gastos proyectados o deseados. En este último caso, las partidas del presupuesto corresponden a las mismas categorías de gasto, según se detalla a continuación:

* Vivienda
* Alimentación
* Transporte
* Cuidado personal
* Ropa
* Entretenimiento
* Deudas
* Servicios
* Seguros
* Ahorros
* Otros

El programa permite comparar los gastos que se generan en el mes con el presupuesto proyectado, con el propósito de que el usuario pueda administrar sus finanzas de forma más consciente y proactiva y así aumentar sus ahorros mensualmente.

Además, la aplicación genera gráficos con información relevante, como es la comparación entre gastos y presupuesto, mencionada anteriormente, así como la distribución de gastos y de ingresos por categoría en un mes dado.

Dentro de las principales limitaciones de la solución implementada, se encuentra que bien su funcionalidad cumple con el objetivo establecido en el alcance inicial del proyecto, en cuanto a llevar el presupuesto de manera mensual a lo largo del año, la aplicación en esta fase inicial no permite el aprovechamiento de información para diferentes años, de forma que se pueda analizar y comparar comportamientos y tendencias en periodos más amplios de tiempo. No obstante, esta funcionalidad puede ser agregada sin mayores complicaciones, debido al diseño modular del proyecto.

### Estructura

En Python, los paquetes son la forma de organizar y estructurar módulos relacionados en un directorio, el cual contiene un archivo `__init__.py`. Por su parte, un módulo se refiere a un archivo con extensión `.py` el cual contiene definiciones de funciones y clases que se pueden utilizar. Esta organización en módulos y paquetes permite mantener un orden el código de un proyecto de relativa complejidad y tamaño, así como facilitar la reutilización del código. Los módulos o sus funciones pueden ser utilizadas en otros archivos usando el comando `import`.

De esta forma, el diseño de la solución del proyecto incluye una estructura de directorios que facilita el manejo y la organización del código, dentro de los cuales destacan los siguientes:

* `entry_classes` es el paquete principal donde se encuentra todo el código necesario para interactuar con la interfaz para gestionar el ingreso de información por parte del usuario y la conexión con las bases de datos donde se almacena ésta. Contiene los siguientes módulos:
	* `template.py`, donde se crea la base de funcionalidad para los gastos y el presupuesto, esto es, la clase `Economy` que define los atributos que luego heredaran las clases `presupuesto` y `gasto`, los cuales determinan las categorías en las que el usuario podrá clasificar los gastos y las partidas presupuestarias.
	* `spend.py`, para configurar el panel de introducción de gastos del usuario, define la clase `GastosFrame` que hereda de `Economy` y maneja el layout de la interfaz para los gastos.
	* `budget.py`, para configurar la entrada del presupuesto, para esto, define la clase `PresupuestoFrame` que hereda de `Economy`. Posee las funciones `event_guardar` y `write_data` que permiten escribir los valores ingresados en la base de datos, verificando una posible sobreescritura por medio de la función `check_existing_data`.
	* `income.py`, para las características de la entrada de ingresos por medio de la interfaz y hacia la base de datos. Crea la clase `Income` como clase padre para el manejo de ingresos que gestiona los atributos y los métodos para validad y escribir en la base de datos. Además, crea la clase `IncomeFrame` que hereda de `Income`, la cual maneja el layout de la interfaz para los ingresos.
* `main_window`, paquete donde se encuentra el código de la interfaz principal del programa.
	*  Contiene el módulo `menu_panel.py` que tiene toda la estructura de la ventana principal del programa. Crea las clase s`MainWindow` y `BodyFrame`, que controlan y configuran la ventana principal, así como `UpperBar` para la barra superior y `MenuFrame` para el menú lateral.
*  `graph_classes`, paquete donde se maneja el módulo `graph_choyce.py` para desplegar las opciones de elección para el gráfico, por medio de la clase `GraphChoice`.
* El paquete `tablesetting` que contiene el módulo `base_to_excel.py` para pasar los datos de las bases de datos manejadas con `sqlite` a formato Excel por medio de la función `data_to_excel`, esto para la generación de los gráficos, la cual se implementó utilizando tablas en formato `xls`. También en este paquete se encuentran los módulos que contienen el código necesario para realizar operaciones para buscar en la base de datos y para crear las tablas de ingresos, gastos y presupuesto para el usuario.

<p align="right">(<a href="#readme-top">regresar</a>)</p>

### Diseño

Como se detalló en el apartado anterior, el proyecto posee una estructura organizada en módulos y paquetes con el fin de aprovechar las ventajas que brinda Python para trabajar de forma estructurada, utilizando al mismo tiempo un enfoque de programación orientada objetos, con fundamento en la aplicación de conceptos útiles en muchos ámbitos del desarrollo de software, como son abstracción, clases, herencia, encapsulamiento y polimorfismo.

La versión de Python utilizada es la 3.11.5.

#### GUI

Para la implementación de la interfaz gráfica se utilizó Tkinter,  una biblioteca estándar de Python que permite crear interfaces gráficas de usuario (GUI), por lo que únicamente requiere de incluir `import tkinter as tk` en el código. Esta biblioteca proporciona una variedad de widgets que se pueden utilizar para construir la interfaz gráfica, como por ejemplo recuadros para el ingreso de texto o números, botones para guardar datos o menús desplegables para seleccionar opciones. Sigue un modelo de programación basado en eventos, lo que permite asociar las funciones y los métodos a eventos específicos, como presionar una tecla o dar clic. Tkinter resulta una solución interesante para este proyecto, donde la interfaz es sencilla, y además debido a su amplia documentación y comunidad activa.

#### Bases de datos

Por su parte, para el manejo de las bases de datos se utilizó SQLite3, también una biblioteca ligera que se encuentra incorporada en la biblioteca estándar de Python, por lo cual únicamente es necesario importar el módulo `sqlite3` en el código del proyecto. Dentro de otras ventajas para seleccionar su uso en este proyecto se encuentra el que sea una base de datos que no requiere un servidor, su baja curva de aprendizaje y el buen rendimiento mostrado en un proyecto pequeño como este. La estructura de tabla proporcionada por este módulo permite una fácil manipulación de los datos para almacenamiento y consultas.

#### Gráficas

Además, para la implementación de las gráficas, se utilizó la biblioteca `Matplotlib`, la cual proporciona herramientas para la creación de distintos tipos de gráficos y cuenta con amplia comunidad y documentación. Para instalarla es necesario ejecutar `pip install matplotlib`. También, se utilizó la biblioteca `pandas`, que permite trabajar con estructuras de datos tabulares y series temporales, y es compatible con diferentes formatos de entrada y salida de datos, como por ejemplo Excel. Finalmente, se utilizó la biblioteca `openpyxl` para trabajar con archivos en formato `.xlsx`, dado que proporciona funciones para leer, escribir y manipular hojas de cálculo en Excel. 

Finalmente, fue necesario unir posteriormente la funcionalidad de generar las gráficas, la cual se encuentra implementada en formato Excel, con el manejo de información en las bases de datos realizada con `sqlite3` en la interacción con el usuario por medio de la interfaz gráfica.

#### Diagrama UML

El diagrama de clases muestra gráficamente la lógica de diseño del proyecto basada en programación orientada a objetos.

![diagrama_UML](https://raw.githubusercontent.com/mareyes1/Lab2/main/UML_proyecto_final.jpeg)
#### Objetivos y limitaciones

Los objetivos del proyecto fueron los siguientes:

1. Desarrollar una interfaz sencilla que permita al usuario ingresar sus gastos y llevar un presupuesto.
2. Comparar los gastos con el presupuesto y mostrar la información.
3. Graficar el porcentaje de gasto e ingreso según categorías.

Al respecto, todos los objetivos fueron cumplidos satisfactoriamente, considerando las oportunidades de mejora señaladas en este reporte.

En cuanto a las limitaciones, la aplicación no permite hacer un seguimiento multianual de la información. Si bien es un aspecto fuera del alcance del proyecto, esta funcionalidad podría ser implementada sin mayor dificultad debido al diseño modular de la solución desarrollada.

<p align="right">(<a href="#readme-top">regresar</a>)</p>

## Comenzar

En esta sección se detalla todo lo necesario ejecutar el proyecto.

### Dependencias

Lo primero que es necesario es tener instalado Python en el sistema. Esto se puede hacer de la siguiente forma desde la terminal de Linux (Ubuntu/Debian):

```sh
sudo apt install python3
```

Además, se requiere tener instalado `pip`, el sistema de gestión de paquetes de Python para instalar y administrar las bibliotecas requeridas. Esto se puede hacer con el siguiente comando:

```sh
sudo apt install python3-pip
```

Para ejecutar adecuadamente el proyecto se deben tener las siguientes dependencias instaladas y configuradas en el entorno de la siguiente forma:

```sh
criptography == 41.0.5
customtkinter == 5.2.1
ctkmessagebox == 2.5
sqlalchemy == 2.0.23
tkcalendar == 1.6.1
ttkbootstrap == 1.10.1
pillow == 10.1.0
openpyxl == 3.1.2
pandas == 2.1.3
sphinx == 6.2.1
matplotlib == 3.8.2
```

La configuración mostrada anteriormente está contenida en el archivo `requirements.txt` incluido en la raíz de la estructura de carpetas del proyecto. Para establecer los valores de las dependencias, se ejecuta el siguiente comando:

```sh
pip install -r requirements.txt
```

<p align="right">(<a href="#readme-top">regresar</a>)</p>

### Instalación

Primero, se debe clonar localmente el repositorio remoto que se encuentra en GitHub:

```sh
git clone https://github.com/Msolis314/ProyectoFinal.git
```

Una vez clonado, se puede ingresar a la carpeta del proyecto y efectuar la configuración de las dependencias según lo detallado en la sección precedente.

Es recomendable, de ser posible, utilizar un entorno virtual para establecer la configuración de dependencias y requerimientos del proyecto. Para esto, se puede utilizar herramientas como Anaconda o alternativas equivalentes.

<p align="right">(<a href="#readme-top">regresar</a>)</p>

## Uso

Una vez efectuada toda la configuración del entorno detallada en el apartado anterior, el programa se ejecuta de la siguiente forma:

```sh
python3 ./main.py
```

<p align="right">(<a href="#readme-top">regresar</a>)</p>

## Funcionamiento

En esta sección se muestra la apariencia del programa en funcionamiento.

### Interfaz gráfica principal

### Registro de usuario

### Ingreso de datos
### Gráficos

#### Gráfico de ingresos

![grafica_ingresos](https://raw.githubusercontent.com/mareyes1/Lab2/main/grafica_ingresos.jpeg)

#### Gráfico de gastos

![grafica_ingresos](https://raw.githubusercontent.com/mareyes1/Lab2/main/grafica_gastos.jpeg)
<p align="right">(<a href="#readme-top">regresar</a>)</p>
