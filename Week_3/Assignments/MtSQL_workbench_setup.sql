use books_schema;

-- -- INSERT
insert into books (title,num_of_pages,created_at,updated_at)
values ('The daily stoic',200,current_timestamp(),current_timestamp());

insert into books (title,num_of_pages,created_at,updated_at)
values ('The daily dad',500,current_timestamp(),current_timestamp());

insert into books (title,num_of_pages,created_at,updated_at)
values ('Courage is calling',700,current_timestamp(),current_timestamp());

insert into books (title,num_of_pages,created_at,updated_at)
values ('laws of human nature',290,current_timestamp(),current_timestamp());

-- UPDATE
update books
set title = 'The king'
where id = 2; 

-- DELETE
delete from books
where id = 1;

-- SELECT
select * 
from books;