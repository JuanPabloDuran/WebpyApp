import web
import config as config

class View:
    def __init__(self):
        pass

    def GET(self, nombre):
        persona = config.model_personas.select_nombre(nombre) #Selecciona el registro que coinicida con el nombre
        return config.render.view(persona)
