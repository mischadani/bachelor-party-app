from pydantic import BaseModel
from queries.pool import pool
from typing import List, Union
from datetime import time, date


class Error(BaseModel):
    message: str


class BachPartyEventIn(BaseModel):
    event_name: str
    description: str
    location: str
    event_date: date
    start_time: time
    end_time: time
    picture_url: str
    bach_party_id: int

class BachPartyEventOut(BachPartyEventIn):
    id: str


class BachPartyEventQueries:


    def get_bach_party_event(self, id: int) -> Union[Error, BachPartyEventOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id
                        , event_name
                        , description
                        , location
                        , event_date
                        , start_time
                        , end_time
                        , picture_url
                        , bach_party
                        FROM events
                        WHERE id = %s
                        """,
                        [id],
                    )
                    record = result.fetchone()
                    if record is None:
                        return None
                    return BachPartyEventOut(
                        id=record[0],
                        event_name=record[1],
                        description=record[2],
                        location=record[3],
                        event_date=record[4],
                        start_time=record[5],
                        end_time=record[6],
                        picture_url=record[7],
                        bach_party=record[8],
                    )
        except Exception:
            return {"message": "Could not get bach party event"}


    def get_all_bach_party_events(self, bach_party_id: int) -> Union[Error, List[BachPartyEventOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id
                        , event_name
                        , description
                        , location
                        , event_date
                        , start_time
                        , end_time
                        , picture_url
                        , bach_party
                        FROM events
                        WHERE bach_party = %s
                        ORDER BY start_date
                        """,
                        [bach_party_id],
                    )
                    bach_party_event_list = []
                    for record in result:
                        bach_party_event = BachPartyEventOut(
                            id=record[0],
                            event_name=record[1],
                            description=record[2],
                            location=record[3],
                            event_date=record[4],
                            start_time=record[5],
                            end_time=record[6],
                            picture_url=record[7],
                            bach_party=record[8]
                        )
                        bach_party_event_list.append(bach_party_event)
                    return bach_party_event_list
        except Exception:
            return {"message": "Could not get all bach party events"}


    def create_bach_party_event(self, bach_party_event: BachPartyEventIn) -> Union[Error, BachPartyEventOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO events
                            (
                                event_name
                                , description
                                , location
                                , event_date
                                , start_time
                                , end_time
                                , picture_url
                                , bach_party
                            )
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        RETURNING id;
                        """,
                        [
                            bach_party_event.event_name,
                            bach_party_event.description,
                            bach_party_event.location,
                            bach_party_event.event_date,
                            bach_party_event.start_time,
                            bach_party_event.end_time,
                            bach_party_event.picture_url,
                            bach_party_event.bach_party,
                        ]
                    )
                    id = result.fetchone()
                    old_data = bach_party_event.dict()
                    return BachPartyEventOut(
                        id=id,
                        **old_data
                    )
        except Exception:
            return {"message": "Could not create bach party event"}


    def update_bach_party_event(self, bach_party_event: BachPartyEventIn, id: int) -> Union[Error, BachPartyEventOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        UPDATE events
                        SET event_name = %s
                        , description = %s
                        , location = %s
                        , event_date = %s
                        , start_time = %s
                        , end_time = %s
                        , picture_url = %s
                        , bach_party = %s
                        WHERE id = %s
                        """,
                        [
                            bach_party_event.event_name,
                            bach_party_event.description,
                            bach_party_event.location,
                            bach_party_event.event_date,
                            bach_party_event.start_time,
                            bach_party_event.end_time,
                            bach_party_event.picture_url,
                            bach_party_event.bach_party,
                            id
                        ]
                    )
                    return self.record_bach_party_event_out(id, bach_party_event)

        except Exception:
            return {"message": "Could not update bach party event"}


    def delete_bach_party_event(self, id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.curson() as db:
                    db.execute(
                        """
                        DELETE FROM events
                        WHERE id = %s
                        """,
                        [id],
                    )
                    return True
        except Exception:
            return False


    def record_bach_party_event_out(self, record):
        return BachPartyEventOut(
        id=record[0],
        event_name=record[1],
        description=record[2],
        location=record[3],
        event_date=record[4],
        start_time=record[5],
        end_time=record[6],
        picture_url=record[7],
        bach_party=record[8],
    )
