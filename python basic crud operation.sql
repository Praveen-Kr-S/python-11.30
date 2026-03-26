create database stephen;
use stephen;
create table employee(id int,name varchar(50),dept varchar(50),age int);
insert into employee values(2,"stephen","ECE",3);
insert into employee values(3,"Kumar","CSE",4);
insert into employee values(4,"Vidya","IT",5);
SET SQL_SAFE_UPDATES=0;
update employee set Name = "RAM" where id=3;
delete from employee where Name = "Praveen";
#row read or row select
select * from employee where name="RAM";
#select table
select * from employee;
#select column
select name,age from employee;
#add column
alter table employee add column phone int;
#drop column
alter table employee drop column phone;

