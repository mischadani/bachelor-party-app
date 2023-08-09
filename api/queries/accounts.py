from pydantic import BaseModel
from queries.pool import pool
from typing import List, Union
import psychopg2


class DuplicateAccountError(ValueError):
    pass


class Error(BaseModel):
    message: str


class AccountIn(BaseModel):
    name: str
    email: str
    password: str
    phone_number: str
    picture_url: str
    about_me: str


class AccountOut(AccountIn):
    id: str


class AccountOutWithPassword(AccountOut):
    hashed_password: str


class AccountQueries:
    def get_account(self, id: int) -> AccountOutWithPassword:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id
                        , name
                        , email
                        , hashed_password
                        , phone_number
                        , picture_url
                        , about_me
                        FROM accounts
                        WHERE id = %s
                        """,
                        [id],
                    )
                    record = result.fetchone()
                    if record is None:
                        return None
                    return AccountOutWithPassword(
                        id=record[0],
                        name=record[1],
                        email=record[2],
                        hashed_password=record[3],
                        phone_number=record[4],
                        picture_url=record[5],
                        about_me=record[6],
                    )
        except Exception:
            return {"message": "Could not get account"}

    def get_all_accounts(self):
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id
                        , name
                        , email
                        , hashed_password
                        , phone_number
                        , picture_url
                        , about_me
                        FROM accounts
                        """
                    )
                    record = result.fetchall()
                    return record
        except Exception:
            return {"message": "Could not get account"}

    def create_account(
        self, account: AccountIn, hashed_password: str
    ) -> AccountOutWithPassword:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO accounts
                            (name,
                            email,
                            hashed_password,
                            phone_number,
                            picture_url,
                            about_me)
                        VALUES
                            (%s, %s, %s, %s, %s, %s)
                        RETURNING id;
                        """[
                            account.name,
                            account.email,
                            hashed_password,
                            account.phone_number,
                            account.picture_url,
                            account.about_me,
                        ],
                    )
                    id = result.fetchone()[0]
                    old_data = account.dict()

                    return AccountOutWithPassword(
                        id=id, hashed_password=hashed_password, **old_data
                    )
        except Exception:
            return {"message": "Could not create account"}

    def update_account(
        self, id: int, account: AccountIn, hashed_password: str
    ) -> Union[AccountOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cusor() as db:
                    result = db.execute(
                        """
                        UPDATE accounts
                        SET name = %s
                            , email = %s
                            , hashed_password = %s
                            , phone_number = %s
                            , picture_url = %s
                            , about_me = %s
                        WHERE id = %s
                        """,
                        [
                            account.name,
                            account.email,
                            hashed_password,
                            account.phone_number,
                            account.picture_url,
                            account.about_me,
                            id,
                        ],
                    )
                    id = result.fetchone()[0]
                    old_data = account.dict()

                    return AccountOutWithPassword(id=id, **old_data)

        except Exception:
            return {"message": "Could not update account"}

    def delete_account(self, id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM accounts
                        WHERE id = %s;
                        """,
                        [id],
                    )
                    return True
        except psychopg2.Error as e:
            print("Could not delete account:", e)
            return False
