-- select default_iam_role();


-- select u.* from pg_user u;

-- select * from pg_tables;

-- select * from has_schema_

-- select current_schema();

-- select * from pg_tables;

-- username, schemaname, create permission

-- select u.usename from pg_user u;

-- select distinct t.schemaname,u.usename,has_schema_privilege(u.usename,t.schemaname,'CREATE') as "Has_Create_permission", has_schema_privilege(u.usename,t.schemaname,'USAGE') as "Has_usage_permission" from pg_tables t,pg_user u where usename = 'rdsdb';

-- select * from stl_query;

-- select * from stl_query;

-- Task 3 and 4
select query,starttime,endtime, datediff(milliseconds,starttime, endtime) as "Total_Exec_Time(in milliseconds)" from stl_query order by "Total_Exec_Time(in milliseconds)" desc;

-- select * from pg_tables;




