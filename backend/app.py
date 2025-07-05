#import flask package
from flask import Flask
from flask_restful import Api,Resource
from flask_migrate import Migrate
from models import db

from resources.category import CategoryResource
from resources.entry import EntryResource
from resources.user import UserResource
#initialize our app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///recipe.db"
#allow sqlalchemy to display generate sql on the terminal
app.config["SQLALCHEMY_ECHO"] = True

api=Api(app)
migrate = Migrate(app, db)
db.init_app(app)

@app.route('/', methods= ['POST'])
def index():
    return {"message":"Welcome to my recipe app"}

# C.R.U.D

# CREATE -> POST -> /categories
# READ -> GET -> All categories -> /categories
# READ -> GET -> Single category -> /categories/<id> (UPDATE -> PATCH), (DELETE)

# We have refactored the category routes to use flask-restful

# Create a single category
# @app.post("/categories")
# def create_category():
#     return {"message": "Category created"}


# # Retrieves all categories
# @app.get("/categories")
# def get_categories():
#     return []

# # Retrieve a single catgory
# @app.get("/categories/<id>")
# def get_category(id):
#     return {}

# # Update a single catgory
# @app.patch("/categories/<id>")
# def update_category(id):
#     return {"message": "Category updated"}


# # Retrieve a single catgory
# @app.delete("/categories/<id>")
# def delete_category(id):
#     return {"message": "Category deleted"}

class Login(Resource):
    def post(self):
        return {"message": "Login successful"}

api.add_resource(EntryResource, '/entries', '/entries/<entry_id>')
api.add_resource(UserResource, '/users', '/users/<user_id>')
api.add_resource(CategoryResource, '/categories', '/categories/<int:id>')
api.add_resource(Login, '/signin')





    
