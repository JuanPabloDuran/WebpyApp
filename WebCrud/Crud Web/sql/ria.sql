create database ria_iniciales;
use ria_iniciales;
create table personas(
    id  int(20) not null primary key,
    nombre  varchar(30) not null,
    apellidos   varchar(40) not null,
    email   varchar(20) not null,
    edad    int(3)  not null
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

insert into personas (id, nombre, apellidos, email, edad) values
(1, "Alex", "Haz Hunter", "123@gmail.com", 23),
(2, "Dante", "Alcho Kelpo", "JJJ@gmail.com", 32),
(3, "Leon", "Perez Keneddy", "Leo@gmail.com", 28),
(4, "Clare", "Patoja Burton", "Cla@hotmail.com", 25);

create table productos(
    id_prod  int(20) not null primary key,
    nombre  varchar(30) not null,
    marca   varchar(40) not null,
    descripcion   varchar(20) not null,
    cantidad    int(3)  not null
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

insert into personas (id_prod, nombre, marca, descripcion, cantidad) values
(1, "Axe", "AXE", "desodorante", 23),
(2, "Danonino", "Danette", "yoghurt", 12),
(3, "Ruffles", "Sabritas", "Comida chatarra", 20),
(4, "Mortadela", "FUD", "Embutido", 23);

show tables;

select * from personas;

describe personas;

CREATE USER 'ria'@'localhost' IDENTIFIED BY 'ria.2019';
GRANT ALL PRIVILEGES ON ria_iniciales.* TO 'ria'@'localhost';
FLUSH PRIVILEGES;
