import uuid 
from typing import Dict 

class ActivityCreator:
    def __init__(self, activity_repository) -> None:
        self.__activity_repository = activity_repository

    def create(self, body, trip_id) -> Dict:
        try:
            id = str(uuid.uuid4())
            activity_infos = {
                "id": id, 
                "trip_id": trip_id,
                "title": body["title"],
                "occurs_at": body["occurs_at"]
            }
            self.__activity_repository.registry_activity(activity_infos)
            return {
                "body": {"activityId": id},
                "status_code": 201
            }
        except Exception as exception:
            return{
                "body": {"error": "Bad Request", "message": str(exception)},
                "status_code": 400
            }

