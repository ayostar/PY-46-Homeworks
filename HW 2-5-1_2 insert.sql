insert into singer (name)
values ('Alex B');

insert into singer (name)
values ('Complex Downshift');

insert into singer (name)
values ('Emerson Louzy');

insert into singer (name)
values ('Ginger Hope');

insert into singer (name)
values ('Inside the mind');

insert into singer (name)
values ('Keychain Lubricant');

insert into singer (name)
values ('Mama Nanny');

insert into singer (name)
values ('OP');

insert into style (name)
values ('Classic');

insert into style (name)
values ('Rock-n-Roll');

insert into style (name)
values ('Pop');

insert into style (name)
values ('Rap');

insert into style (name)
values ('Country');

insert into album(name, year)
values ('Jan', 2005);

insert into album(name, year)
values ('Feb', 2010);

insert into album(name, year)
values ('Mar', 2012);

insert into album(name, year)
values ('Apr', 2015);

insert into album(name, year)
values ('May', 2019);

insert into album(name, year)
values ('Jun', 2019);

insert into album(name, year)
values ('Jul', 2020);

insert into album(name, year)
values ('Aug', 2021);

insert into track(album, name, length)
values (1, 'Track1', 2.22);

insert into track(album, name, length)
values (2, 'Track2', 2.22);

insert into track(album, name, length)
values (2, 'Track3', 3.22);

insert into track(album, name, length)
values (3, 'Track4', 5.55);

insert into track(album, name, length)
values (3, 'Track5', 3.33);

insert into track(album, name, length)
values (3, 'Track6', 2.22);

insert into track(album, name, length)
values (4, 'Track7', 4.44);

insert into track(album, name, length)
values (4, 'Track8', 4.44);

insert into track(album, name, length)
values (5, 'Track9', 5.55);

insert into track(album, name, length)
values (6, 'Track10', 6.59);

insert into track(album, name, length)
values (7, 'Track11', 7.59);

insert into track(album, name, length)
values (8, 'Track12', 8.59);

insert into track(album, name, length)
values (8, 'Track13', 9.59);

insert into track(album, name, length)
values (8, 'My Track14', 10.59);

insert into track(album, name, length)
values (8, 'Track15', 11.59);

insert into track(album, name, length)
values (8, 'My Track16', 12.59);

insert into track(album, name, length)
values (8, 'Track17', 13.59);

insert into track(album, name, length)
values (8, 'My Track18', 14.59);

insert into track(album, name, length)
values (8, 'Track19', 15.59);

insert into collection(name, year)
values ('Red', 2011);

insert into collection(name, year)
values ('Blue', 2013);

insert into collection(name, year)
values ('Green', 2015);

insert into collection(name, year)
values ('Yellow', 2017);

insert into collection(name, year)
values ('Green', 2018);

insert into collection(name, year)
values ('Orange', 2020);

insert into collection(name, year)
values ('Black', 2020);

insert into collection(name, year)
values ('White', 2020);

insert into singer_album(singer_id, album_id)
values (1, 8);

insert into singer_album(singer_id, album_id)
values (2, 7);

insert into singer_album(singer_id, album_id)
values (2, 6);

insert into singer_album(singer_id, album_id)
values (3, 6);

insert into singer_album(singer_id, album_id)
values (4, 5);

insert into singer_album(singer_id, album_id)
values (5, 4);

insert into singer_album(singer_id, album_id)
values (6, 3);

insert into singer_album(singer_id, album_id)
values (7, 2);

insert into singer_album(singer_id, album_id)
values (8, 1);

insert into singer_style(singer_id, style_id)
values (2, 5);

insert into singer_style(singer_id, style_id)
values (1, 4);

insert into singer_style(singer_id, style_id)
values (3, 3);

insert into singer_style(singer_id, style_id)
values (4, 1);

insert into singer_style(singer_id, style_id)
values (5, 2);

insert into singer_style(singer_id, style_id)
values (6, 3);

insert into singer_style(singer_id, style_id)
values (2, 3);

insert into singer_style(singer_id, style_id)
values (2, 1);

insert into track_collection(track_id, collection_id)
values (1, 6);

insert into track_collection(track_id, collection_id)
values (2, 6);

insert into track_collection(track_id, collection_id)
values (1, 1);

insert into track_collection(track_id, collection_id)
values (2, 2);

insert into track_collection(track_id, collection_id)
values (3, 6);

insert into track_collection(track_id, collection_id)
values (11, 6);

insert into track_collection(track_id, collection_id)
values (12, 5);

insert into track_collection(track_id, collection_id)
values (8, 6);