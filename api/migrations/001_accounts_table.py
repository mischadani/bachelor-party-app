steps = [
    [
        # CREATE TABLE
        """
        CREATE TABLE accounts (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(200) UNIQUE NOT NULL,
            hashed_password TEXT NOT NULL,
            phone_number VARCHAR(15) NOT NULL,
            picture_url VARCHAR(200),
            about_me TEXT
        );
        """,
        # DROP TABLE
        """
        DROP TABLE accounts;
        """
    ]
]
