create table person (
    id int primary key not null,
    first_name text,
    last_name text
);

insert into person (id, first_name, last_name) values (1, 'John', 'Adams');
insert into person (id, first_name, last_name) values (2, 'Richard', 'Recluse');
insert into person (id, first_name, last_name) values (3, 'Sara', 'Smith');

select first_name, last_name from person;


create table phone (
    id int primary key not null,
    person_id int not null,
    phone_number text,
    phone_type text
);

insert into phone (id, person_id, phone_number, phone_type) values (1, 1, '555-1234', 'home');
insert into phone (id, person_id, phone_number, phone_type) values (2, 1, '555-5555', 'cell');
insert into phone (id, person_id, phone_number, phone_type) values (3, 3, '555-9999', 'cell');

select person.first_name, person.last_name, phone.phone_number, phone.phone_type
from person inner join phone on person.id = phone.person_id;

select person.first_name, person.last_name, phone.phone_number, phone.phone_type
from person left outer join phone on person.id = phone.person_id;

select person.first_name, person.last_name, phone.phone_number, phone.phone_type
from person left outer join phone on person.id = phone.person_id
where person.last_name = 'Adams';
