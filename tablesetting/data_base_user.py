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
        tipo TEXT,
        monto TEXT,
        notas TEXT,
        mes TEXT
    )
    '''
    tabla_presupuesto= '''
    CREATE TABLE IF NOT EXISTS presupuesto (
        Domicilio TEXT,
        Higiene TEXT,
        Transporte TEXT,
        Entretenimiento TEXT,
        Deudas TEXT,
        Seguros TEXT,
        Servicios TEXT,
        Otros TEXT,
        mes TEXT
    )
    '''
    c.execute(tabla_ingresos)
    c.execute(tabla_gastos)
    c.execute(tabla_presupuesto)
    conn.commit()
    conn.close()

