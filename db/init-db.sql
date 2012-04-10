drop table if exists users;
create table users (id integer primary key,
       username text not null unique,
       email text not null unique,
       password text not null);

drop table if exists sessions;
create table sessions (
       session_id text not null unique,
       user_id integer not null,
       foreign key (user_id) references users (id));

