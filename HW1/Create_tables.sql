CREATE TABLE trips (
       medallion varchar(50),
       hack_license varchar(50),
       vendor_id VARCHAR(3),
       rate_code SMALLINT,
       store_and_fwd_flag VARCHAR(3),
       pickup_datetime TIMESTAMP,
       dropoff_datetime TIMESTAMP,
       passenger_count SMALLINT,
       trip_time_in_secs INT,
       trip_distance DECIMAL(12,5),
       pickup_longitude DECIMAL(15,10),
       pickup_latitude DECIMAL(15,10),
       dropoff_longitude DECIMAL(15,10),
       dropoff_latitude DECIMAL(15,10)
);
CREATE TABLE fares (
       medallion varchar(50),
       hack_license varchar(50),
       vendor_id VARCHAR(3),
       pickup_datetime TIMESTAMP,
       payment_type VARCHAR(3),
       fare_amount DECIMAL(15,10),
       surcharge DECIMAL(15,10),
       mta_tax DECIMAL(15,10),
       tip_amount DECIMAL(15,10),
       tolls_amount DECIMAL(15,10),
       total_amount DECIMAL(15,10)
);

CREATE TABLE medallions (
       medallion varchar(50),
       name varchar(50),
       type varchar(30),
       current_status varchar(10),
       DMV_license_plate varchar(10),
       vehicle_VIN_number varchar(20),
       vehicle_type varchar(10),
       model_year DECIMAL(4),
       medallion_type varchar(30),
       agent_number INTEGER,
       agent_name varchar(30),
       agent_telephone_number varchar(15),
       agent_website varchar(50),
       agent_address varchar(50),
       last_updated_date DATE,
       last_updated_time TIME
);