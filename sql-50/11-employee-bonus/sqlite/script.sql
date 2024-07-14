-- Create table employee
create table employee (
    empid integer primary key,
    name text,
    supervisor integer,
    salary integer
);

-- Create table bonus
create table bonus (
    empid integer primary key,
    bonus integer,
    foreign key (empid) references employee(empid)
);

-- insert data in employee table
insert into employee (empid, name, supervisor, salary) values (3, 'Brad', null, 4000);
insert into employee (empid, name, supervisor, salary) values (1, 'John', 3, 1000);
insert into employee (empid, name, supervisor, salary) values (2, 'Dan', 3, 2000);
insert into employee (empid, name, supervisor, salary) values (4, 'Thomas', 3, 4000);

-- insert data in bonus table
insert into bonus (empid, bonus) values (2, 500);
insert into bonus (empid, bonus) values (4, 2000);

-- execute query to obtain desired results
select
    e.name,
    b.bonus
from
    employee e
left join
    bonus b
on
    e.empid = b.empid
where
    b.bonus < 1000 or b.bonus is null;

