import pytest
import uuid
from .links_to_trips_repository import LinksToTripsRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="interacao com o banco")
def test_registry_links():
    conn = db_connection_handler.get_connection()
    links_to_trips_repository = LinksToTripsRepository(conn)

    links_trips_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "link": "viagem.com.br",
        "title": "viagem para a agentina"
    }

    links_to_trips_repository.registry_links(links_trips_infos)

@pytest.mark.skip(reason="interacao com o banco")
def test_find_links_from_trip():
    conn = db_connection_handler.get_connection()
    links_to_trips_repository = LinksToTripsRepository(conn)

    links = links_to_trips_repository.find_link(trip_id)
    assert isinstance(links, list)
    assert isinstance(links[0], tuple)