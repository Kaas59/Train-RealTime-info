---- 【drop】 ----
-- DROP TABLE IF EXISTS agency;
---- 【drop】 ----

---- 【Create】 ----
create table IF not exists train_log(
    id INT(11) AUTO_INCREMENT,
    train_id VARCHAR(255) ,
    odpt_type VARCHAR(255) ,
    dc_date VARCHAR(255) ,
    dct_valid VARCHAR(255) ,
    odpt_delay INT(11) ,
    odpt_railway VARCHAR(255) ,
    odpt_operator VARCHAR(255) ,
    odpt_train_number VARCHAR(255) ,
    odpt_train_type VARCHAR(255) ,
    odpt_to_station VARCHAR(255) ,
    odpt_from_station VARCHAR(255) ,
    odpt_rail_direction VARCHAR(255) ,
    odpt_car_composition VARCHAR(255),
    odpt_destination_station VARCHAR(255) ,
    created_at Datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at Datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
) DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
---- 【Create】 ----
