-- Primary Key - A key that has one version for every row.
-- Foreign Key - Key that can't exist without a primary key in another table.
-- Logical Key - A way to look up a row in a table from the outside world (usually a title or name).

CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT
)

CREATE TABLE Genre (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT
)

CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
    UNIQUE,
    artist_id INTEGER,
    title TEXT
)

CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY
    AUTOINCREMENT UNIQUE,
    title TEXT,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
)
