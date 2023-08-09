from pydantic import BaseModel
from queries.pool import pool
from typing import List, Union, Optional
from datetime import time, date


class Error(BaseModel):
    message: str


class BachPartyIn(BaseModel):
    name: str
    description: Optional[str]
    host: int
    location: Optional[str]
    date: date
    start_time: time
    end_time: time
    picture_url: Optional[str]
    host_notes: str
    status: str



class BachPartyOut(BachPartyIn):
    id: int


class BachPartyQueries:
    def create_bach_party(self, bach_party: BachPartyIn, id: int) -> BachPartyOut:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO bach_parties
                            (name,
                            description,
                            host,
                            location,
                            date,
                            start_time,
                            end_time,
                            picture_url,
                            host_notes,
                            status)
                        VALUES
                            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        RETURNING id;
                        """,
                        [
                            bach_party.name,
                            bach_party.description,
                            bach_party.host,
                            bach_party.location,
                            bach_party.date,
                            bach_party.start_time,
                            bach_party.end_time,
                            bach_party.picture_url,
                            bach_party.host_notes,
                            bach_party.status
                        ]
                    )
                    id = result.fetchone()[0]
                    old_data = bach_party.dict()
                    return BachPartyOut(id=id, **old_data)
        except Exception:
            return{"message": "Could not create bachelor party"}


    def get_all_bach_parties(self) -> Union[Error, List[BachPartyOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        """
                    )
