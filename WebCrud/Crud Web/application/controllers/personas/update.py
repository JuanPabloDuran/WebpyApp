import web
import config as config

class Update:
    def __init__(self):
        pass

    def GET(self, nombre):
        persona = config.model_personas.select_nombre(nombre) #Selecciona el registro que coinicida con el nombre
        return config.render.update(persona) #Envia el registro y renderiza update.html

    def POST(self, email):
        formulario = web.input()

        nombre = formulario['nombre']
        apellido_pat = formulario['apellido_pat']
        apellido_mat = formulario['apellido_mat']
        email = formulario['email']
        edad = formulario['edad']

        config.model_personas.update_persona(nombre, apellido_pat, apellido_pat, email, edad)
        raise web.seeother('/personas')
        
