from typing import Dict, Tuple, List
from sqlite3 import Connection

class LinksToTripsRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_links(self, links: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO links
                    (id, trip_id, link, title)
                VALUES
                    (?, ?, ?, ?)
            ''', (
                links["id"],
                links["trip_id"],
                links["link"],
                links["title"],
            )
        )
        self.__conn.commit()

    def find_link(self, trip_id: str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''SELECT * FROM links WHERE id = ?''', (trip_id,)
        )
        links = cursor.fetchall()
        return links