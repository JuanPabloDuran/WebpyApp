import web
import config as config

class Index:
    def __init__(self):
        pass
    
    def GET(self):
        personas = config.model_personas.select_persona().list() #Selecciona los registros de personas 
        return config.render.index(personas) #Envia los registros y renderiza index 
