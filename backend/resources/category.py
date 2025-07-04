from flask_restful import Resource
from models import db

class CategoryResource(Resource):
    def get(self, categories_id=None):
        if categories_id is None:
            categories = db.session.get(category, id)
            return [{
                "id": categ.id,
                "name": categ.name,
                "created_at": categ.created_at
            } for categ in categories]
        
        
        category = db.session.get(categories, id)
        if category:
            return {
                "id": category.id,
                "name": category.name,
                "created_at": category.created_at
            }
        return {"error": "Category not found"}

    def post(self):
        return {"message": "Category created successfully"}

    def patch(self, categories_id):
        return {"message": f"Category with ID {categories_id} updated successfully"}

    def delete(self, categories_id):
        return {"message": f"Category with ID {categories_id} deleted successfully"}
