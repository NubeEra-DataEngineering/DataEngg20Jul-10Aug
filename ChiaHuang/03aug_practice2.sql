select "table", unsorted, vacuum_sort_benefit from svv_table_info order by 1;

vacuum;
analyze;
