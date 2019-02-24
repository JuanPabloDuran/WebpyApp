import web 

urls= (
    '/', 'application.controllers.personas.main.Main',
    '/personas', 'application.controllers.personas.index.Index',
    '/insert', 'application.controllers.personas.insert.Insert',
    '/update/(.*)', 'application.controllers.personas.update.Update',
    '/delete/(.*)', 'application.controllers.personas.delete.Delete',
    '/view/(.*)', 'application.controllers.personas.view.View',
    '/productos', 'application.controllers.productos.index.Index_produ',
    '/insert_p', 'application.controllers.productos.insert.Insert_produ',
    '/update_p/(.*)', 'application.controllers.productos.update.Update_produ',
    '/delete_p/(.*)', 'application.controllers.productos.delete.Delete_produ',
    '/view_p/(.*)', 'application.controllers.productos.view.View_produ'
)

if __name__ == '__main__':
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()
    
