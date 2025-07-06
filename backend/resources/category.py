from flask_restful import Resource, reqparse
from models import Category, db
from flask import request, jsonify

class CategoryResource(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument("name", required=True, help="Category name is required")
    # parse.add_argument("email", required=True, help="Email is required")
    # parse.add_argument("password", required=True, help="Password is required")
    def get(self, id=None):
        if id is None:
            categories = Category.query.all()
            return jsonify([category.to_dict() for category in categories])
        else:
            category = Category.query.filter_by(id=id).first()
            if category is None:
                return {"message": "Category not found"}, 404
            return jsonify(category.to_dict())

    def post(self):
        data = self.parse.parse_args()
        
        category = Category(**data)
        db.session.add(category)
        db.session.commit()
        return {"message": "Category created successfully"}, 201
    
    #only admins can update categories
    #for updating
    def patch(self, id):
        data = self.parse.parse_args()
        #retrieve the record by id
        category = Category.query.filter_by(id=id).first()
        
        if category is None:
            return {"message": "Category not found"}, 404
        #update instance with new value
        category.name = data["name"]
        #commit to db
        db.session.commit()
        return {"message": "Category updated successfully"}, 200
    
    #only admins can delete categories
    def delete(self, id):
        category = Category.query.filter_by(id=id).first()
        
        if category is None:
            return {"message": "Category not found"}, 404
        
        db.session.delete(category)
        db.session.commit()
        return {"message": "Category deleted successfully"}, 200