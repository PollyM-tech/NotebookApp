from flask_restful import Resource
from models import db

class EntryResource(Resource):
    #for category and category id
    def get(self, entry_id=None):
        if entry_id == None:
            return {}
        else:
            #get a single entry
            return{}
    #         entries = Entry.query.all()
    #         return [{
    #             "id": e.id,
    #             "note": e.note,
    #             "user_id": e.user_id,
    #             "created_at": e.created_at,
    #             "updated_at": e.updated_at,
    #             "deleted_at": e.deleted_at
    #         } for e in entries]

    #     entry = Entry.query.get(entry_id)
    #     if entry:
    #         return {
    #             "id": entry.id,
    #             "note": entry.note,
    #             "user_id": entry.user_id,
    #             "created_at": entry.created_at,
    #             "updated_at": entry.updated_at,
    #             "deleted_at": entry.deleted_at
    #         }
    #     return {"error": "Entry not found"}

    def post(self):
        return {"message": "Entry created successfully"}

    def patch(self, entry_id):
        return {"message": "Entry updated successfully"}

    def delete(self, entry_id):
        return {"message": "Entry deleted successfully"}
