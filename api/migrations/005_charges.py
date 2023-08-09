steps = [
    [
        # CREATE TABLE
        """
        CREATE TABLE charges (
            id SERIAL PRIMARY KEY NOT NULL,
            title VARCHAR(100),
            bach_party INTEGER NOT NULL REFERENCES bach_parties(id) ON DELETE RESTRICT,
            amount DEMICAL(2),
            description TEXT,
            account INTEGER NOT NULL REFERENCES accounts(id) ON DELETE RESTRICT
        );
        """,
        # DROP TABLE
        """
        DROP TABLE attendee_list;
        """
    ]
]
