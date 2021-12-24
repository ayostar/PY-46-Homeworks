insert into singer (name)
values ('AB');

insert into singer (name)
values ('C D');

insert into singer (name)
values ('E F');

insert into singer (name)
values ('G H');

insert into singer (name)
values ('I J');

insert into singer (name)
values ('K L');

insert into singer (name)
values ('M N');

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
values ('One', 2001);

insert into album(name, year)
values ('Two', 2002);

insert into album(name, year)
values ('Three', 2003);

insert into album(name, year)
values ('Four', 2004);

insert into album(name, year)
values ('Five', 2005);

insert into album(name, year)
values ('Six', 2006);

insert into album(name, year)
values ('Seven', 2007);

insert into album(name, year)
values ('Eighteen', 2018);

insert into track(album, name, length)
values (1, 'Track1', 1.11);

insert into track(album, name, length)
values (2, 'Track2', 2.22);

insert into track(album, name, length)
values (3, 'Track3', 3.33);

insert into track(album, name, length)
values (4, 'Track4', 4.44);

insert into track(album, name, length)
values (5, 'Track5', 5.55);

insert into track(album, name, length)
values (6, 'Track6', 6.59);

insert into track(album, name, length)
values (7, 'Track7', 7.59);

insert into track(album, name, length)
values (8, 'Track8', 8.59);

insert into track(album, name, length)
values (8, 'Track9', 9.59);

insert into track(album, name, length)
values (8, 'My Track10', 10.59);

insert into track(album, name, length)
values (8, 'Track11', 11.59);

insert into track(album, name, length)
values (8, 'My Track12', 12.59);

insert into track(album, name, length)
values (8, 'Track13', 13.59);

insert into track(album, name, length)
values (8, 'My Track14', 14.59);

insert into track(album, name, length)
values (8, 'Track15', 15.59);

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
values (2, 5);

insert into track_collection(track_id, collection_id)
values (1, 6);

insert into track_collection(track_id, collection_id)
values (2, 6);

insert into track_collection(track_id, collection_id)
values (1, 6);

insert into track_collection(track_id, collection_id)
values (2, 6);

insert into track_collection(track_id, collection_id)
values (3, 6);

insert into track_collection(track_id, collection_id)
values (11, 6);

insert into track_collection(track_id, collection_id)
values (12, 6);

insert into track_collection(track_id, collection_id)
values (8, 6);