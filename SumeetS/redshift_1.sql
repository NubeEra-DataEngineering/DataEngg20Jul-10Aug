select default_iam_role();

select current_user;

select u.* from pg_user u;

select current_schema();

select * from pg_tables;

select * from pg_user; 

select
    u.usename,
    s.schemaname,
    has_schema_privilege(u.usename,s.schemaname,'create') AS create_permission,
    has_schema_privilege(u.usename,s.schemaname,'usage') AS usage_permission
from
    pg_user u
cross join
    (select distinct schemaname from pg_tables) s
WHERE
    u.usename LIKE '%data8%';

select * from stl_query;

select * from pg_table_def;

select * from pg_user;

SELECT * FROM pg_catalog.pg_attribute;

select current_schema();

select * from pg_tables;

select query,starttime,endtime, datediff(milliseconds,starttime, endtime) as "Total_Exec_Time(in milliseconds)" 
from stl_query 
order by "Total_Exec_Time(in milliseconds)" desc;
