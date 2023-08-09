steps = [
    [
        # CREATE TABLE
        """
        CREATE TABLE attendee_list (
            id SERIAL PRIMARY KEY NOT NULL,
            attendee INTEGER NOT NULL REFERENCES accounts(id) ON DELETE RESTRICT,
            bach_party INTEGER NOT NULL REFERENCES bach_parties(id) ON DELETE RESTRICT
        );
        """,
        # DROP TABLE
        """
        DROP TABLE attendee_list;
        """
    ]
]
