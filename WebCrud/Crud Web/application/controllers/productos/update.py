import web
import config as config

class Update_produ:
    def __init__(self):
        pass

    def GET(self, codigo):
        producto = config.model_productos.select_producto(id_prod) #Selecciona el registro que coinicida con el nombre
        return config.render.update_p(producto) #Envia el registro y renderiza update.html

    def POST(self, id_prod):
        formulario = web.input()

        id_prod = formulario['id_prod'] #almacena el nombre escrito en el input
        nombre = formulario['nombre']
        marca = formulario['marca']
        descricpion = formulario['descricpion']
        cantidad = formulario['cantidad']

        config.model_productos.update_producto(id_prod, nombre, marca, descripcion, cantidad)
        raise web.seeother('/productos')
        
