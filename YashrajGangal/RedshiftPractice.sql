SELECT default_iam_role();

SELECT * from pg_tables;
SELECT * from pg_user;
SELECT * from pg_roles;
SELECT current_schema();

SELECT
    usename as USERNAME,
    current_schema() as SCHEMANAME,
    has_schema_privilege( USERNAME, SCHEMANAME,  'USECREATEDB' )
FROM
    pg_user;

SELECT *
  FROM public.role_table_grants 
 WHERE grantee = 'IAM:data3';

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
    AND s.schemaname = 'public';

SELECT * from stl_query;
select query, trim(querytxt) as sqlquery
from stl_query
order by query desc limit 5;


GRANT ALL PRIVILEGES ON ALL TABLES TO "admin";
GRANT ALL PRIVILEGES ON DATABASE dev TO "admin";

select * from pg_database;
select * from information_schema.schemata;

SELECT * from pg_tables;
SELECT * FROM pg_default_acl;

-- Task 3
SELECT 
    querytxt,
    count(*) as number_of_runs
FROM
    stl_query
GROUP BY querytxt
ORDER BY number_of_runs DESC
LIMIT 10;

-- Task 4
SELECT 
    querytxt,
    datediff(milliseconds, starttime, endtime) AS runtime
FROM
    stl_query;
ORDER BY runtime;
