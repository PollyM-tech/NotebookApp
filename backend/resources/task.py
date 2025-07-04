from flask_restful import Resource
from models import db

class TaskResource(Resource):
    def get(self, tasks_id=None):
        if tasks_id == None:
            return {}
        else:
            return {}