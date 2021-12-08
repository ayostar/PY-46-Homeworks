create table if not exists singer (
id serial primary key,
name varchar(40) not null unique
);

create table if not exists album (
id serial primary key,
name varchar(40) not null,
singer integer references singer(id),
year date not null
);

create table if not exists track(
id serial primary key,
album integer references album(id),
name varchar(40),
length numeric(4,2) CHECK (length > 0)
);