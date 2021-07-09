-- The JOIN Operation
-- Links across several tables as part of a select operation.
-- You must tell the JOIN how to use the keys that make the connection between the tables using an ON clause.
select Album.title, Artist.name from Album join Artist on Album.artist_id = Artist.id
--     ^ What we want to see ^   ^ the tables with data ^   ^ how tables are linked ^
-- the ON clause says that the rows will be connected when the Album's artist_id value = Artist's id value

-- Join a table of the track names and their genres.
select Track.title, Genre.name from Track join Genre on Track.genre_id = Genre.id

-- Without an ON Clause, you will get all possible combinations of Track.genre_id and Genre.id, even it not equal.
select Track.title, Genre.name from Track join Genre

-- Table with Track title, Artist name, Album title, Genre name. Use AND keyword to join on clauses
select Track.title, Artist.name, Album.title, Genre.name from Track join Artist join Album join Genre on Track.album_id = Album.id and Track.genre_id = Genre.id and Album.artist_id = Artist.id
