CREATE DATABASE oyoo;
use oyoo;

CREATE TABLE data(
    nama_pemesan VARCHAR (50),
    check_in VARCHAR (50),
    nomor_kamar INT PRIMARY KEY,
    tipe_kamar VARCHAR (50)
);