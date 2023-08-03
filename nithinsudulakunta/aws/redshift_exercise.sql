select default_iam_role();

select current_user;

select * from pg_user;

select current_schema();

select *  from pg_tables;

select distinct u.usename User_Name, t.schemaname Schema_Name, has_schema_privilege( u.usename, t.schemaname, 'create') Create_Permission, has_schema_privilege( u.usename, t.schemaname, 'usage') Usage_Permission from pg_user u cross join pg_tables t where user_name like 'IAM:data6';

select * from sys_load_error_detail;


select query, querytxt, starttime, endtime, datediff(milliseconds, starttime, endtime) as date_diff_in_milliseconds  from stl_query;


SELECT querytxt, COUNT(*) AS query_count, avg(datediff(milliseconds, starttime, endtime)) as avg_date_diff_in_milliseconds
FROM stl_query
GROUP BY querytxt
HAVING COUNT(*) > 1;


SELECT query, querytxt, starttime, endtime, datediff(milliseconds, starttime, endtime) as date_diff_in_milliseconds
FROM stl_query
WHERE querytxt = 'your_identity_query_text_here'
ORDER BY date_diff_in_milliseconds DESC;
