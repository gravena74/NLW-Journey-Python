import pytest
import uuid 
from .participants_repository import ParticipantsRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="interacao com o banco")
def test_registry_participant():
    conn = db_connection_handler.get_connection()
    participant_respository = ParticipantsRepository(conn)

    participant_trip_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "emails_to_invite_id": "gravena@email.com",
        "name": "joao Gravena"
    }

    participant_respository.registry_participant(participant_trip_infos)


@pytest.mark.skip(reason="interacao com o banco")
def test_find_participants_from_trip():
    conn = db_connection_handler.get_connection()
    participant_respository = ParticipantsRepository(conn)

    participant = participant_respository.find_participants_from_trip(trip_id)
    

@pytest.mark.skip(reason="interacao com o banco")
def test_update_participant_status():
    conn = db_connection_handler.get_connection()
    participant_repository = ParticipantsRepository(conn)

    participant = participant_repository.update_participant_status(trip_id)
    