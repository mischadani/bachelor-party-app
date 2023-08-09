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
    start_date: date
    end_date: date
    picture_url: Optional[str]
    host_notes: str
    status: str


class BachPartyOut(BachPartyIn):
    id: int


class BachPartyQueries:
    def create_bach_party(self, bach_party: BachPartyIn) -> BachPartyOut:
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
                            start_date,
                            end_date,
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
                            bach_party.start_date,
                            bach_party.end_date,
                            bach_party.picture_url,
                            bach_party.host_notes,
                            bach_party.status,
                        ],
                    )
                    id = result.fetchone()[0]
                    old_data = bach_party.dict()
                    return BachPartyOut(id=id, **old_data)
        except Exception:
            return {"message": "Could not create bachelor party"}

    def get_all_bach_parties(self) -> Union[Error, List[BachPartyOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        SELECT id,
                        name,
                        description,
                        host,
                        location,
                        start_date,
                        end_date,
                        picture_url,
                        host_notes,
                        status
                        FROM bach_parties
                        ORDER BY start_date;
                        """,
                    )
                    result = []
                    for record in db:
                        bach_party = BachPartyOut(
                            id=record[0],
                            name=record[1],
                            description=record[2],
                            host=record[3],
                            location=record[4],
                            start_date=record[5],
                            end_date=record[6],
                            picture_url=record[7],
                            host_notes=record[8],
                            status=record[9],
                        )
                        result.append(bach_party)
                    return result
        except Exception:
            return {"message": "Could not get all bach parties"}

    def get_bach_party(self, id: int) -> Optional[BachPartyOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        SELECT id,
                        name,
                        description,
                        host,
                        location,
                        start_date,
                        end_date,
                        picture_url,
                        host_notes,
                        status
                        FROM bach_parties
                        WHERE id = %s
                        """,
                        [id],
                    )
                    record = db.fetchone()
                    if record is None:
                        return None
                    return BachPartyOut(
                            id=record[0],
                            name=record[1],
                            description=record[2],
                            host=record[3],
                            location=record[4],
                            start_date=record[5],
                            end_date=record[6],
                            picture_url=record[7],
                            host_notes=record[8],
                            status=record[9],
                        )
        except Exception:
            return {"message": "Could not get bach party"}

    def update_bach_party(
        self, id: int, bach_party: BachPartyIn
    ) -> Union[BachPartyOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE bach_parties
                        SET name = %s,
                        description = %s,
                        host = %s,
                        location = %s,
                        start_date = %s,
                        end_date = %s,
                        picture_url = %s,
                        host_notes = %s,
                        status = %s
                        WHERE id = %s
                        """,
                        [
                            bach_party.name,
                            bach_party.description,
                            bach_party.host,
                            bach_party.location,
                            bach_party.start_date,
                            bach_party.end_date,
                            bach_party.picture_url,
                            bach_party.host_notes,
                            bach_party.status,
                            id
                        ],
                    )
                    record = db.fetchone()
                    if record is None:
                        return None 
                    return BachPartyOut(
                            id=record[0],
                            name=record[1],
                            description=record[2],
                            host=record[3],
                            location=record[4],
                            start_date=record[5],
                            end_date=record[6],
                            picture_url=record[7],
                            host_notes=record[8],
                            status=record[9],
                        )

        except Exception:
            return {"message": "Could not update bach party"}

    def delete_bach_party(self, id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.curson() as db:
                    db.execute(
                        """
                        DELETE FROM bach_parties
                        WHERE id = %s
                        """,
                        [id],
                    )
                    return True
        except Exception:
            return False
