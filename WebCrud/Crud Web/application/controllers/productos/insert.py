import web
import config as config

class Insert_produ:
    def __init__(self):
        pass
    
    def GET(self):
        return config.render.insert_p() #renderiza la pagina insert.html

    def POST(self):
        formulario = web.input() #almacena los datos del formulario
        
        id_prod = formulario['id_prod'] 
        nombre = formulario['nombre']
        marca = formulario['marca']
        descripcion = formulario['descripcion']
        cantidad = formulario['cantidad']
        
        config.model_productos.insert_producto(codigo, nombre, marca, descripcion, cantidad)
        raise web.seeother('/productos') #redirecciona al index.html
