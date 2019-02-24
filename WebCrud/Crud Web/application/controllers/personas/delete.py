import web '''Importa la libreria de Web.py para trabajar con las paginas en conjunto con html'''
import config as config'''Importa el archivo de configuracion de la misma carpeta y crea un nuevo objeto'''

class Delete:
    def __init__(self):'''Funcion que sirve para dar paso al siguente evento que es GET'''
        pass
    
    def GET(self, nombre):
        personas = config.model_personas.select_nombre(nombre) '''Selecciona el registro que coinicida con el nombre y regresa
                                                                  el valor que contenga la base de datos junto con sus atributos'''
        return config.render.delete(personas)

    def POST(self, nombre):
        formulario = web.input()
        nombre = formulario['nombre']
        config.model_personas.delete_persona(nombre)
        raise web.seeother('/personas')'''Aqui te dirige a la pagina de las personas una vez arrojado el resultado'''
        
