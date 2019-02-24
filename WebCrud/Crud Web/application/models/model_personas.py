import config as config

db = config.db

'''
Metodo para seleccionar todos los registros de la tabla personas consulta todos los registros de las personas
'''
def select_persona():
    try:
        return db.select('personas') #Selecciona todos los registros de la tabla clientes
    except Exception as e:
        print "Model select_personas Error {}",format(e.args)
        print "Model select_personas Message {}",format(e.message)
        return None
'''
Metodo para seleccionar un registro en especifico de la persona deseada, dandole como parametro el nombre
'''
def select_nombre(nombre):
    try:
        return db.select('personas', where='nombre = $nombre', vars=locals())[0] #Selecciona los registros que coincidan con el nombre
    except Exception as e:
        print "Model select_nombre Error {}",format(e.args)
        print "Model select_nombre Message {}",format(e.message)
        return None
'''
Metodo para insertar un nuevo registro, aqui se le pediran 5 parametros (nombre, apellido paterno, apellido materno, email y edad)
Como Excepcion se tendra que si no se llenan los registros completamente o se llenan incorrectos mandara un mensaje de error
'''
def insert_personas(nombre, apellido_pat, apellido_mat, email, edad):
    try:
        return db.insert('personas', 
        nombre=nombre, 
        apellido_pat=apellido_pat, 
        apellido_mat=apellido_mat,
        email=email,
        edad=edad) #Inserta un registro 
    except Exception as e:
        print "Model insert_personas Error {}",format(e.args)
        print "Model insert_personas Message {}",format(e.message)
        return None
'''
Metodo para eliminar Registros, dandole como parametro el nombre para que realice la busqueda
Como excepcion se tendra que si no se da un nombre que coincida con la base de datos se arrojara un mensaje de error
'''
def delete_personas(nombre):
    try:
        return db.delete('personas', where='nombre=$nombre', vars=locals())#Elimina el registro de la base de datos si coincide con el nombre
    except Exception as e:
        print "Model delete_personas Error {}",format(e.args)
        print "Model delete_personas Message {}",format(e.message)
        return None
'''
Metodo para actualizar los registros, aqui se dara como parametro el nombre para poder actualizar (apellido paterno, apellido materno, email y edad)
Como excepcion se tendra que si el nombre no coincide se mandara un mensaje de error y no se actualizara el registro
'''
def update_cliente(nombre, apellido_pat, apellido_mat, email, edad):
    try:
        return db.update('personas',
            apellido_pat=apellido_pat,
            apellido_mat=apellido_mat,
            email=email,
            edad=edad,
            where='nombre=$nombre',
            vars=locals())#Actualiza el registro con los nuevos valores
    except Exception as e:
        print "Model update_personas Error {}",format(e.args)
        print "Model update_personas Message {}",format(e.message)
        return None
