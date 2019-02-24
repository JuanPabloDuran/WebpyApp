import web
import config as config

class View_produ:
    def __init__(self):
        pass

    def GET(self, id_produ):
        producto = config.model_productos.select_producto(id_produ) #Selecciona el registro que coinicida con el nombre
        return config.render.view_p(producto)
