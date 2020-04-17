from flask import Flask   #imports Flask
from noteapp.views.index import bp as index_bp #imports the blueprint
from noteapp.views.createnote import bp as createnote_bp

app = Flask(__name__)    #titel, name of this file

app.register_blueprint(index_bp) #registers the application
app.register_blueprint(createnote_bp)
