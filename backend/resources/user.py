from flask_restful import Resource
from models import db

class UserResource(Resource):
    def get(self, users_id = None):
        if users_id == None:
            return {"message": "List of users"}
        else:
            return {"message": f"User with ID {users_id} retrieved successfully"}
        
    def post(self):
        return {"messages": "User created successful"}
    
    def patch(self, users_id):
        return {"message": f"User with ID {users_id} updated successfully"}
    
    def delete(self, users_id):
        return {"message": f"User with ID {users_id} deleted successfully"}