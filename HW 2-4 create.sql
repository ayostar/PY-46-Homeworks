create table if not exists singer (
id serial primary key,
name varchar(40) not null unique
);

create table if not exists album (
id serial primary key,
name varchar(40) not null,
year integer not null
);

create table if not exists track (
id serial primary key,
album integer references album(id),
name varchar(40),
length numeric(4,2) CHECK (length > 0)
);

create table if not exists style (
id serial primary key,
name varchar(40) not null unique
);


create table if not exists collection (
id serial primary key,
name varchar(40),
year integer not null
);

create table if not exists singer_style (
id serial primary key,    
singer_id integer references singer(id),
style_id integer references style(id)
);

create table if not exists singer_album (
id serial primary key,
singer_id integer references singer(id),
album_id integer references album(id)
);

create table if not exists track_collection (
id serial primary key,
track_id integer references track(id),
collection_id integer references collection(id)
);
