create table if not exists Singer (
ID serial primary key,
Name varchar(40) not null unique
);

create table if not exists Album (
ID serial primary key,
Name varchar(40) not null unique,
Singer integer references singer(ID),
year date
);

create table if not exists Track(
ID serial primary key,
Album integer references album(ID),
Name varchar(40),
Length numeric(4,2)
);