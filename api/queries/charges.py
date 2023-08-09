from pydantic import BaseModel
from queries.pool import pool
from typing import List, Union, Optional
from datetime import date


class Error(BaseModel):
    message: str


class ChargeIn(BaseModel):
    title: str
    bach_party: int
    amount: float
    description: Optional[str]
    account: int
    date: date


class ChargeOut(ChargeIn):
    id: int


class ChargeQueries:
    def create_charge(self, id: int, charge: ChargeIn) -> ChargeOut:
        try:
            with pool.connection as conn:
                with conn.cursor as db:
                    result = db.execute(
                        """
                        INSERT INTO charges
                            (title,
                            bach_party,
                            amount,
                            description,
                            account,
                            date
                            )
                        VALUES
                            (%s, %s, %s, %s, %s)
                        RETURNING id;
                        """
                        [
                            charge.title,
                            charge.bach_party,
                            charge.amount,
                            charge.description,
                            charge.account,
                            charge.date
                        ]
                    )
                    id = result.fetchone()[0]
                    old_data = charge.dict()
                    return ChargeOut(id=id, **old_data)
        except Exception:
            return({"message": "Could not create charge"})

    def get_all_charges(self) -> Union[Error, List[ChargeOut]]:
        try:
            with pool.connection as conn:
                with conn.cursor as db:
                    db.execute(
                        """
                        SELECT id,
                        title,
                        bach_party,
                        amount,
                        description,
                        account,
                        date
                        FROM charges
                        ORDER by date;
                        """
                    )
                    result = []
                    for record in db:
                        charge = ChargeOut(
                            id=record[0],
                            title=record[1],
                            bach_party=record[2],
                            amount=record[3],
                            description=record[4],
                            account=record[5],
                            date=record[6]
                        )

        except Exception:
            return({"message": "Could not create charge"})


    def get_one_charge(self, id: int) -> Optional[ChargeOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        SELECT id,
                        title,
                        bach_party,
                        amount,
                        date
                        FROM charges
                        WHERE id = %s
                        ORDER BY date DESC;
                        """
                        [id]
                    )
                    record = db.fetchone()
                    if record is None:
                        return None
                    return ChargeOut(
                            id=record[0],
                            title=record[1],
                            bach_party=record[2],
                            amount=record[3],
                            description=record[4],
                            account=record[5],
                            date=record[6]
                        )
        except Exception:
            return({"message": "Could not get charge"})
