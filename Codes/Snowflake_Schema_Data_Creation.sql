

# Snowflake schema creation


# -- Create your warehouse (used to run SQL)
CREATE OR REPLACE WAREHOUSE compute_wh;

# -- Create your database to store tourism data
CREATE OR REPLACE DATABASE culture_tourism_db;

# -- Use that database and schema
USE DATABASE culture_tourism_db;
USE SCHEMA public;



-- create table by uploading csv

CREATE OR REPLACE TABLE heritage_sites (
    city_name STRING,
    state STRING,
    country STRING,
    zone_name STRING,
    name_of_heritage STRING,
    nature_of_heritage STRING,
    heritage_use STRING,
    age_of_heritage STRING
);

