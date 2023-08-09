steps = [
    [
        # CREATE TABLE
        """
        CREATE TABLE events (
            id SERIAL PRIMARY KEY NOT NULL,
            event_name VARCHAR(100) NOT NULL,
            description TEXT,
            location VARCHAR(200) NOT NULL,
            event_date DATE NOT NULL,
            start_time TIME NOT NULL,
            end_time TIME NOT NULL,
            picture_url VARCHAR(200),
            bach_party INTEGER NOT NULL REFERENCES bach_parties(id) ON DELETE RESTRICT
        );
        """,
        # DROP TABLE
        """
        DROP TABLE events;
        """
    ]
]
