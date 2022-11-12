GRANT ALL PRIVILEGES ON DATABASE productdb TO docker;

-- Creation of product table
CREATE TABLE IF NOT EXISTS product (
  product_id INT NOT NULL,
  brand varchar(25) NOT NULL,
  ram_gb INT NOT NULL,
  hdd_gb INT NOT NULL, 
  ghz NUMERIC NOT NULL,
  price INT NOT NULL
  --PRIMARY KEY (product_id)
);