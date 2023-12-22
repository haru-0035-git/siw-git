-- Active: 1696486038674@@127.0.0.1@3306@bmi_calculation
drop table if EXISTS users ;
CREATE table users(
    id              int               not NULL   auto_increment,
    name            VARCHAR(32)       not NULL,
    birthday        date              NOT NULL,
    height          DECIMAL(4,1)      NOT NULL,
    target_weight   DECIMAL(4,1)      NOT NULL,
    
    PRIMARY KEY (id)
) COMMENT = "ユーザ登録マスタ";

drop Table if EXISTS weight_records;
CREATE TABLE weight_records(
    id                      int                AUTO_INCREMENT ,
    user_name               VARCHAR(32)        NOT NULL,
    height                  DECIMAL(4,1)       NOT NULL,
    weight                  DECIMAL(4,1)       NOT NULL,
    datetime                DATE               NOT NULL,
    target_weight           DECIMAL(4,1)       NOt NULL,
    PRIMARY KEY (id)
) COMMENT = '体重登録マスタ';

ALTER Table users ADD 
  Foreign Key (user_name) REFERENCES users(name);

SELECT * from users;

SELECT * from weight_records;