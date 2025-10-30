CREATE TABLE 
if NOT EXISTS Salesman
(
Salesman_id TEXT PRIMARY KEY,
name TEXT, 
city TEXT,
commision REAL

);

INSERT INTO Salesman
(Salesman_id, name,city,commision)
VALUES

('46','JOHN','LONDON',0.14),
('87','NANCY','DELHI',0.44),
('56','NICK','LONDON',0.23),
('54','JAS','PARIS',0.14),
('44','NINA','LONDON',0.65); 
SELECT*
 FROM Salesman;
 CREATE TABLE 
if NOT EXISTS Orders
(
order_no TEXT PRIMARY KEY,
purch_amt REAL, 
ord_date TEXT,
customer_id TEXT,
salesman_id TEXT

);
INSERT INTO Orders
(order_no,purch_amt,ord_date,customer_id,salesman_id)
VALUES
('455',122.5,'8.02.25','114443','4665'),
('445',187.5,'10.02.25','114442','4665'),
('451',1456.5,'18.02.25','114444','4665'),
('454',1278.5,'14.02.25','114445','4665'),

SELECT*
 FROM Orders;
Select name,commision
From Salesman;