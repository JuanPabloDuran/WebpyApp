import web
import config as config

class Insert:
    def __init__(self):
        pass
    
    def GET(self):
        return config.render.insert() #renderiza la pagina insert.html

    def POST(self):
        formulario = web.input() #almacena los datos del formulario
        nombre = formulario['nombre'] #almacena el nombre escrito en el input
        apellido_pat = formulario['apellido_pat']
        apellido_mat = formulario['apellido_mat']
        email = formulario['email']
        edad = formulario['edad']
        config.model_personas.insert_personas(nombre,apellido_pat,apellido_mat,email,edad)
        raise web.seeother('/personas') #redirecciona al index.html
