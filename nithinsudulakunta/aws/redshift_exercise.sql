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



CREATE TABLE supplier_nithin
(
  s_suppkey   INTEGER NOT NULL,
  s_name      VARCHAR(25) NOT NULL,
  s_address   VARCHAR(25) NOT NULL,
  s_city      VARCHAR(10) NOT NULL,
  s_nation    VARCHAR(15) NOT NULL,
  s_region    VARCHAR(12) NOT NULL,
  s_phone     VARCHAR(15) NOT NULL
);



COPY dev.public.supplier_nithin FROM 's3://awssampledbuswest2/ssbgz/supplier.tbl'
CREDENTIALS 'aws_iam_role=arn:aws:iam::475184346033:role/service-role/AmazonRedshift-CommandsAccessRole-20230802T180608'
DELIMITER '|'
gzip
REGION 'us-west-2';

select * from supplier_nithin limit 5;


COPY dev.public.customer_nithin FROM 's3://bkt-03aug-mujahed/load/customer-fw-manifest'
CREDENTIALS 'aws_iam_role=arn:aws:iam::475184346033:role/service-role/AmazonRedshift-CommandsAccessRole-20230802T180608'
fixedwidth 'c_custkey:10,c_name:25,c_address:25,c_city:10,c_nation:15,c_region:12,c_phone:15,c_mktsegment:10'
maxerror 10
acceptinvchars as '^'
manifest;



CREATE TABLE customer_nithin
(
  c_custkey      INTEGER NOT NULL, 
  c_name         VARCHAR(25) NOT NULL,
  c_address      VARCHAR(25) NOT NULL,
  c_city         VARCHAR(10) NOT NULL,
  c_nation       VARCHAR(15) NOT NULL,
  c_region       VARCHAR(12) NOT NULL,
  c_phone        VARCHAR(15) NOT NULL,
  c_mktsegment   VARCHAR(10) NOT NULL
);

SELECT 
	QUERY,
	SUBSTRING(FILENAME,22,25) AS FileName,
	LINE_NUMBER as line,
	SUBSTRING(RAW_FIELD_VALUE,0,45) AS Field_Text,
	SUBSTRING(err_reason,0,45) as err_reason	
FROM STL_LOAD_ERRORS
ORDER BY QUERY DESC, FileName
limit 7;

select * from supplier_customer limit 5;


CREATE TABLE dev.public.dwdate_nithin
(
  d_datekey            INTEGER NOT NULL,
  d_date               VARCHAR(19) NOT NULL,
  d_dayofweek          VARCHAR(10) NOT NULL,
  d_month              VARCHAR(10) NOT NULL,
  d_year               INTEGER NOT NULL,
  d_yearmonthnum       INTEGER NOT NULL,
  d_yearmonth          VARCHAR(8) NOT NULL,
  d_daynuminweek       INTEGER NOT NULL,
  d_daynuminmonth      INTEGER NOT NULL,
  d_daynuminyear       INTEGER NOT NULL,
  d_monthnuminyear     INTEGER NOT NULL,
  d_weeknuminyear      INTEGER NOT NULL,
  d_sellingseason      VARCHAR(13) NOT NULL,
  d_lastdayinweekfl    VARCHAR(1) NOT NULL,
  d_lastdayinmonthfl   VARCHAR(1) NOT NULL,
  d_holidayfl          VARCHAR(1) NOT NULL,
  d_weekdayfl          VARCHAR(1) NOT NULL
);

COPY dev.public.dwdate_nithin FROM  's3://bkt-03aug-mujahed/load/dwdate-tab.tbl'
CREDENTIALS 'aws_iam_role=arn:aws:iam::475184346033:role/service-role/AmazonRedshift-CommandsAccessRole-20230802T180608' 
DELIMITER '\t'
dateformat 'auto';

select * from dwdate_nithin limit 5;

COPY  lineorder_nithin
FROM 's3://awssampledb/load/lo/lineorder-single.tbl' 
CREDENTIALS 'aws_iam_role=arn:aws:iam::475184346033:role/service-role/AmazonRedshift-CommandsAccessRole-20230802T180608' 
GZIP
COMPUPDATE OFF
REGION 'us-east-1';

CREATE TABLE lineorder_nithin
(
  lo_orderkey          INTEGER NOT NULL,
  lo_linenumber        INTEGER NOT NULL,
  lo_custkey           INTEGER NOT NULL,
  lo_partkey           INTEGER NOT NULL,
  lo_suppkey           INTEGER NOT NULL,
  lo_orderdate         INTEGER NOT NULL,
  lo_orderpriority     VARCHAR(15) NOT NULL,
  lo_shippriority      VARCHAR(1) NOT NULL,
  lo_quantity          INTEGER NOT NULL,
  lo_extendedprice     INTEGER NOT NULL,
  lo_ordertotalprice   INTEGER NOT NULL,
  lo_discount          INTEGER NOT NULL,
  lo_revenue           INTEGER NOT NULL,
  lo_supplycost        INTEGER NOT NULL,
  lo_tax               INTEGER NOT NULL,
  lo_commitdate        INTEGER NOT NULL,
  lo_shipmode          VARCHAR(10) NOT NULL
);

select * from lineorder_nithin limit 2;


select * from svv_table_info order by 1;

vacuum;
analyze;





UNLOAD ('select * from customer_nithin')
TO 's3://bkt-nithin-0308/customers/'
iam_role 'arn:aws:iam::475184346033:role/service-role/AmazonRedshift-CommandsAccessRole-20230802T180608'

UNLOAD ('select * from dwdate_nithin')
TO 's3://bkt-nithin-0308/dwdate/'
iam_role 'arn:aws:iam::475184346033:role/service-role/AmazonRedshift-CommandsAccessRole-20230802T180608'
PARALLEL OFF
maxfilesize 100 mb;


UNLOAD ('select * from lineorder_nithin')
TO 's3://bkt-nithin-0308/lineorder/'
iam_role 'arn:aws:iam::475184346033:role/service-role/AmazonRedshift-CommandsAccessRole-20230802T180608'
PARALLEL OFF
maxfilesize 100 mb;


UNLOAD ('select * from supplier_nithin')
TO 's3://bkt-nithin-0308/supplier-manifest/'
IAM_ROLE 'arn:aws:iam::475184346033:role/service-role/AmazonRedshift-CommandsAccessRole-20230802T180608'
MANIFEST;

select * from stl_unload_log where path like '%nithin%';

select query, substring(path,0,40) as path from stl_unload_log where query = 5752 order by path;



CREATE TABLE region_nations_noshred_nithin (rdata SUPER);

COPY region_nations_noshred_nithin FROM 's3://redshift-downloads/semistructured/tpch-nested/data/json/region_nation'
REGION 'us-east-1' IAM_ROLE 'arn:aws:iam::475184346033:role/service-role/AmazonRedshift-CommandsAccessRole-20230802T180608'
FORMAT JSON 'noshred';


select * from region_nations_noshred_nithin


CREATE TABLE region_nations_nithin
(
 r_regionkey smallint
 ,r_name varchar
 ,r_comment varchar
 ,r_nations super
 );




COPY region_nations_nithin FROM 's3://redshift-downloads/semistructured/tpch-nested/data/json/region_nation'
REGION 'us-east-1' IAM_ROLE 'arn:aws:iam::475184346033:role/service-role/AmazonRedshift-CommandsAccessRole-20230802T180608'
FORMAT JSON 'auto';


select * from region_nations_nithin;
