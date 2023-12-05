import sqlite3


def new_data(user):
    
    data_base_name = f'{user}.db'
    conn = sqlite3.connect(data_base_name)
    c = conn.cursor()
    tabla_ingresos = '''
    CREATE TABLE IF NOT EXISTS ingresos (
        nombre TEXT,
        salario REAL,
        comisiones REAL,
        ventas REAL,
        otros REAL,
        notas TEXT,
        mes TEXT
    )
    '''
    tabla_gastos= '''
    CREATE TABLE IF NOT EXISTS gastos (
        nombre TEXT,
        Domicilio TEXT,
        Higiene TEXT,
        Transporte TEXT,
        Entretenimiento TEXT,
        Deudas TEXT,
        Seguros TEXT,
        Vestimenta TEXT,
        Servicios TEXT,
        Otros TEXT,
        notas TEXT,
        mes TEXT
    )
    '''
    tabla_presupuesto= '''
    CREATE TABLE IF NOT EXISTS presupuesto (
        mes TEXT,
        Domicilio TEXT,
        Higiene TEXT,
        Transporte TEXT,
        Entretenimiento TEXT,
        Deudas TEXT,
        Vestimenta TEXT,
        Seguros TEXT,
        Servicios TEXT,
        Otros TEXT
    )
    '''
    c.execute(tabla_ingresos)
    c.execute(tabla_gastos)
    c.execute(tabla_presupuesto)
    c.execute('SELECT * FROM ingresos LIMIT 1')
    first_row = c.fetchone()

    if first_row == None:

        escribir_valores = '''
            INSERT INTO ingresos (nombre, salario, comisiones, ventas, otros , notas, mes)
            VALUES (?, ?, ?, ?, ?, ?,?)
            '''
        dataingresos = ("nombre","Salario","Comisiones","Ventas","Otros","notas","Months")
        conn.execute(escribir_valores, dataingresos)
        conn.commit()
    c.execute('SELECT * FROM gastos LIMIT 1')
    first_row = c.fetchone()
    if first_row == None:
        escribir_valores = '''
            INSERT INTO gastos (nombre, Domicilio,Higiene , Transporte,Vestimenta,Entretenimiento,Deudas,Seguros,Servicios,Otros, notas, mes)
            VALUES (?, ?, ?, ?, ?, ?,?,?,?,?,?,?)
            '''
        datagastos = ("nombre", "Domicilio","Higiene" , "Transporte","Vestimenta","Entretenimiento","Deudas","Seguros","Servicios","Otros", "notas", "Meses")
        conn.execute(escribir_valores, datagastos)
        conn.commit()
    c.execute('SELECT * FROM presupuesto LIMIT 1')
    first_row = c.fetchone()
    if first_row == None:
        datapresupuesto = ("Meses", "Domicilio","Higiene" , "Transporte","Vestimenta","Entretenimiento","Deudas","Seguros","Servicios","Otros")
        escribir_valores = '''
            INSERT INTO presupuesto (mes, Domicilio,Higiene , Transporte,Entretenimiento,Deudas,Seguros,Vestimenta,Servicios,Otros)
            VALUES (?, ?, ?, ?, ?, ?,?,?,?,?)
            '''
            
        conn.execute(escribir_valores, datapresupuesto)
        conn.commit()
       

    conn.close()

