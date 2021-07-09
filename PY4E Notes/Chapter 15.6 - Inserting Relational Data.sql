-- Insert the data OUTWARD IN, that way you will not get errors when testing the SQL --

insert into Artist (name) values ('Led Zepplin'); -- inserts 'Led Zepplin' as the name for the first row. Since AUTOINCREMENT is on, the id is automatically set to 1.
insert into Artist(name) values('AC/DC') -- value automatically becomes 2

insert into Genre (name) values ('Rock');
insert into Genre (name) values ('Metal') -- you can perform two commands (inserts) at the same time if you add a semi-colon (;) to the end of the each one.

insert into Album (title, artist_id) values ('Who Made Who', 2);
insert into Album (title, artist_id) values ('IV', 1) -- need to pass in the artist_id as the second value. need to cross check and remember that Led Zeppelin is 1 and AC/DC is 2.

insert into Track (title, rating, len, count, album_id, genre_id)
    values ('Black Dog', 5, 297, 0, 2, 1);
insert into Track (title, rating, len, count, album_id, genre_id)
    values ('Stairway', 5, 482, 0, 2, 1); -- it is okay to have replication since they are numbers
insert into Track (title, rating, len, count, album_id, genre_id)
    values ('About to Rock', 5, 313, 0, 1, 2);
insert into Track (title, rating, len, count, album_id, genre_id)
    values ('Who Made Who', 5, 207, 0, 1, 2) -- two foreign keys. important to cross check all numbers