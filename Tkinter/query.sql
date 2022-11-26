create database agenda_telefonica;

use agenda_telefonica;

create table contactos(
id int not null auto_increment,
nombre varchar(50) not null,
numero varchar(50) not null,
primary key(id)
);

insert into contactos(nombre,numero)
values('Ricardo','73000000'),('Veronica','61000000');

select * from contactos;
