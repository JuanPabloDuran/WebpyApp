import web
import config as config

class Delete_produ:
    def __init__(self):
        pass
    
    def GET(self, codigo):
        producto = config.model_productos.select_producto(id_prod) #Selecciona el registro que coinicida con el codigo
        return config.render.delete_p(producto)

    def POST(self, codigo):
        formulario = web.input()

        id_prod = formulario['id_prod']
        nombre = formulario['nombre']
        marca = formulario['marca']
        descripcion = formulario['descripcion']
        cantidad = formulario['cantidad']

        config.model_productos.delete_producto(codigo)
        raise web.seeother('/productos')
