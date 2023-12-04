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

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Comenzar
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

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Instalación

Primero, se debe clonar localmente el repositorio remoto que se encuentra en GitHub:

```sh
git clone https://github.com/Msolis314/ProyectoFinal.git
```

Una vez clonado, se puede ingresar a la carpeta del proyecto y efectuar la configuración de las dependencias según lo detallado en la sección precedente.

Es recomendable, de ser posible, utilizar un entorno virtual para establecer la configuración de dependencias y requerimientos del proyecto. Para esto, se puede utilizar herramientas como Anaconda o alternativas equivalentes.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Uso

```sh
python3 ./main.py
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Funcionamiento


<p align="right">(<a href="#readme-top">back to top</a>)</p>
