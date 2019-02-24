import web 
import application.models.model_personas as model_personas #importa el modelo personas

render = web.template.render('application/views/personas/', base='master') #Configura la ubicacion de las vistas

