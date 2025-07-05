from flask_restful import Resource
from models import db

class CategoryResource(Resource):
    def get(self, id=None):
        if id == None:
            categories = category.query.all()
            print (categories)
            return categories
        else:
            category = categories.query.filter_by(id=id).first()
            print(category)
            return category

    def post(self):
        return {"message": "Category created successfully"}

    def patch(self, categories_id):
        return {"message": f"Category with ID {categories_id} updated successfully"}

    def delete(self, categories_id):
        return {"message": f"Category with ID {categories_id} deleted successfully"}
