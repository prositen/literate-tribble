from app import app

__author__ = 'Anna Holmgren'

app.run(host=app.config['TRIBBLE_HOST'],
        port=app.config['TRIBBLE_PORT'], debug=app.config['DEBUG'])
