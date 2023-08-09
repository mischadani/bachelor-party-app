from pydantic import BaseModel
from queries.pool import pool
from typing import List, Union, Optional
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
    bach_party: str


class BachPartyEventOut(BachPartyEventIn):
    id: str


class BachPartyEventQueries:

    def get_bach_party_event(self, id: str) -> BachPartyEventOut:
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

    def get_all_bach_party_events(self)
