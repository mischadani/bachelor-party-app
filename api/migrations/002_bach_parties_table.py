steps = [
    [
        # CREATE TABLE
        """
        CREATE TABLE bach_parties (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(100) NOT NULL,
            description TEXT,
            host INTEGER NOT NULL REFERENCES accounts(id) ON DELETE RESTRICT,
            picture_url VARCHAR(200),
            location VARCHAR(200) NOT NULL,
            start_date DATE NOT NULL,
            end_date DATE NOT NULL,
            host_notes TEXT,
            status VARCHAR(20) DEFAULT "Upcoming!"
        );
        """,
        # DROP TABLE
        """
        DROP TABLE bach_parties;
        """
    ]
]
