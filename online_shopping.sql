CREATE DATABASE online_shopping;

USE online_shopping;

ALTER TABLE Products ADD COLUMN stock_level INT NOT NULL DEFAULT 0;

ALTER TABLE Orders ADD COLUMN status VARCHAR(50) NOT NULL DEFAULT 'pending';