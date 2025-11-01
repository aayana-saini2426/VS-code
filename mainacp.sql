CREATE TABLE IF NOT EXISTS DCX_Salesman
(
  Salesman_id TEXT PRIMARY KEY,
  name TEXT, 
  city TEXT,
  commission REAL DEFAULT 0,
  fraud_amount REAL
);

INSERT INTO DCX_Salesman
(Salesman_id, name, city, fraud_amount)
VALUES
('46','JOHN','LONDON',6600),
('87','NANCY','DELHI',0),
('56','NICK','LONDON',145),
('54','JAS','PARIS',0),
('44','NINA','LONDON',0);

SELECT name, city, fraud_amount
FROM DCX_Salesman;
