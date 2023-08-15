select default_iam_role();
select current_user;
select u.* from pg_user u;
select current_schema();
select * from pg_tables;

SELECT
    u.usename,
    s.schemaname,
    has_schema_privilege(u.usename,s.schemaname,'create') AS user_has_select_permission,
    has_schema_privilege(u.usename,s.schemaname,'usage') AS user_has_usage_permission
FROM
    pg_user u
CROSS JOIN
    (SELECT DISTINCT schemaname FROM pg_tables) s
WHERE
    u.usename = 'IAM:data11'
    AND s.schemaname = 'public'

-- check a list of schemas in the cluster
select distinct schemaname from pg_tables

-- check a list of tables in a specific schema
select tablename from pg_tables where schemaname='pg_catalog';

-- check a list of columns in a specific table
select * from information_schema.columns where table_name='table1';

-- task3
select query, starttime, endtime, datediff(milliseconds,starttime, endtime) 
as "Total_Exec_Time(in milliseconds)" 
from stl_query 
order by "Total_Exec_Time(in milliseconds)" desc;
