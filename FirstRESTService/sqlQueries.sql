CREATE TABLE laptops (laptop_id INT AUTO_INCREMENT PRIMARY KEY, brandname VARCHAR(20), prcessor VARCHAR(5), RAM VARCHAR(5), screen_size VARCHAR(10));

ALTER TABLE laptops AUTO_INCREMENT=100;

INSERT INTO laptops (brandname, prcessor, RAM, screen_size) VALUES ('Acer', 'i7', '8 GB', '14 in');
INSERT INTO laptops (brandname, prcessor, RAM, screen_size) VALUES ('Dell', 'i5', '8 GB', '15 in');
INSERT INTO laptops (brandname, prcessor, RAM, screen_size) VALUES ('Asus', 'i5', '16 GB', '15.5 in');

DELETE FROM laptops WHERE brandname='HP';
