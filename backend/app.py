#import flask package
from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from models import db

from resources.category import CategoryResource
from resources.entry import EntryResource
from resources.task import TaskResource
from resources.user import UserResource
#initialize our app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///recipe.db"
app.config["SQLALCHEMY_ECHO"] = True


api=Api(app)
migrate = Migrate(app, db)
db.init_app(app)

@app.route('/', methods= ['POST'])
def index():
    return {"message":"Welcome to my recipe app"}

api.add_resource(EntryResource, '/entries', '/entries/<id>')
api.add_resource(UserResource, '/users', '/users/<id>')
api.add_resource(TaskResource, '/tasks', '/tasks/<id>')
api.add_resource(CategoryResource, '/categories', '/categories/<id>')





    
