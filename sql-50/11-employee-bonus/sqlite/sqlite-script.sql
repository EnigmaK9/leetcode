-- Crear la tabla Employee
create table employee (
    empid integer primary key,
    name text,
    supervisor integer,
    salary integer
);

-- Crear la tabla Bonus
create table bonus (
    empid integer primary key,
    bonus integer,
    foreign key (empid) references employee(empid)
);

-- Insertar datos en la tabla Employee
insert into employee (empid, name, supervisor, salary) values (3, 'Brad', null, 4000);
insert into employee (empid, name, supervisor, salary) values (1, 'John', 3, 1000);
insert into employee (empid, name, supervisor, salary) values (2, 'Dan', 3, 2000);
insert into employee (empid, name, supervisor, salary) values (4, 'Thomas', 3, 4000);

-- Agregar más datos a la tabla Employee
insert into employee (empid, name, supervisor, salary) values (5, 'Alice', 3, 3500);
insert into employee (empid, name, supervisor, salary) values (6, 'Bob', 2, 2800);
insert into employee (empid, name, supervisor, salary) values (7, 'Carol', 1, 3000);
insert into employee (empid, name, supervisor, salary) values (8, 'David', 4, 4500);
insert into employee (empid, name, supervisor, salary) values (9, 'Eve', 2, 3200);
insert into employee (empid, name, supervisor, salary) values (10, 'Frank', 5, 3700);

-- Insertar datos en la tabla Bonus
insert into bonus (empid, bonus) values (2, 500);
insert into bonus (empid, bonus) values (4, 2000);

-- Agregar más datos a la tabla Bonus
insert into bonus (empid, bonus) values (5, 800);
insert into bonus (empid, bonus) values (6, 700);
insert into bonus (empid, bonus) values (7, 900);
insert into bonus (empid, bonus) values (9, 600);
insert into bonus (empid, bonus) values (10, 1500);

-- Ejecutar la consulta para obtener los resultados deseados
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

