DROP TABLE IF EXISTS DEPARTMENT;

CREATE TABLE IF NOT EXISTS DEPARTMENT(
  EMPLOYEE_ID TEXT, 
  NAME TEXT,
  DEPARTMENT_ID TEXT, 
  MANAGER_ID TEXT, 
  SALARY REAL
);

INSERT INTO DEPARTMENT(EMPLOYEE_ID, NAME, DEPARTMENT_ID, MANAGER_ID, SALARY) VALUES
('14666','ZZ','80254','444455',15000),
('14667','XX','45775','455533',1500),
('14668','YY','80254','445522',25000),
('14669','JJ','78546','444455',10000),
('14670','QQ','78554','444455',30000),
('14671','LL','80254','445588',59000),
('14672','MM','46354','444455',10000);

SELECT EMPLOYEE_ID, NAME, DEPARTMENT_ID, MANAGER_ID, SALARY
FROM DEPARTMENT;
SELECT 
  department_id AS 'Department Code',
  COUNT(*) AS 'No. of Employees'
FROM DEPARTMENT
GROUP BY department_id;

SELECT 
  department_id AS 'Department Code',
  SUM(Salary) AS 'Total Salary'
FROM DEPARTMENT
GROUP BY department_id;

SELECT 
  department_id AS 'Department Code',
  COUNT(*) AS 'No. of Employees',
  SUM(Salary) AS 'Total Salary'
FROM DEPARTMENT
GROUP BY department_id;

SELECT 
  department_id AS 'Department Code',
  SUM(Salary) AS 'Total Salary'
FROM DEPARTMENT
WHERE MANAGER_ID = '444455'
GROUP BY department_id;

SELECT 
  department_id AS 'Department Code',
  COUNT(*) AS 'No. of Employees'
FROM DEPARTMENT
GROUP BY department_id
HAVING COUNT(*) > 2;
