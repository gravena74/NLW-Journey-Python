import pytest
import uuid
from datetime import datetime
from .activities_repository import ActivitiesRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

def test_create_trip():
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)

    activities_info = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "title": "escalada no gelo",
        "occurs_at": datetime.strptime("02-01-2024", "%d-%m-%Y")
    }

    activities_repository.registry_activity(activities_info)

def test_find_activities_from_trip():
    conn = db_connection_handler.get_connection()
    activities_respository = ActivitiesRepository(conn)

    activities = activities_respository.find_activities_from_trip(trip_id)