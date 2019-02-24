import config as config

db = config.DB

'''
Metodo para seleccionar todos los registros de la tabla productos
'''
def select_productos():
    try:
        return db.select('productos') 
    except Exception as e:
        print "Model select_productos Error {}",format(e.args)
        print "Model select_productos Message {}",format(e.message)
        return None

def select_producto(id_prod):
    try:
        return db.select('productos', where='id_prod = $id_prod', vars=locals())[0] #Selecciona el primer registro que coincida con el nombre
    except Exception as e:
        print "Model select_codigo Error {}",format(e.args)
        print "Model select_codigo Message {}",format(e.message)
        return None

def insert_producto(id_prod, nombre, marca, descricpion, cantidad):
    try:
        return db.insert('productos', 
        id_prod=id_prod,
        nombre=nombre,
        marca=marca,
        descricpion=descricpion,
        cantidad=cantidad
        ) #Inserta un registro en la tabla productos
    except Exception as e:
        print "Model insert_producto Error {}",format(e.args)
        print "Model insert_producto Message {}",format(e.message)
        return None

def delete_producto(id_prod):
    try:
        return db.delete('productos', where='id_prod=$id_prod', vars=locals())
    except Exception as e:
        print "Model delete_producto Error {}",format(e.args)
        print "Model delete_producto Message {}",format(e.message)
        return None

def update_producto(id_prod, nombre, marca, descripcion, cantidad):
    try:
        return db.update('productos',
            id_prod=id_prod,
            nombre=nombre,
            marca=marca,
            descripcion=descripcion,
            cantidad=cantidad,
            where='id_prod=$id_prod',
            vars=locals())
    except Exception as e:
        print "Model update_producto Error {}",format(e.args)
        print "Model update_producto Message {}",format(e.message)
        return None
