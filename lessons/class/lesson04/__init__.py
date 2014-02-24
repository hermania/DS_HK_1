-- What customers are from the London
SELECT * FROM Customers WHERE city = 'London';  

-- What is the name of the customer who has the most orders?
SELECT Customers.CustomerName FROM Orders
JOIN Customers on (Orders.CustomerID = Customers.CustomerID)
GROUP BY Orders.CustomerID
ORDER BY COUNT(Orders.CustomerID) DESC
LIMIT 1

-- What supplier has the highest average product price?
SELECT Suppliers.*, AVG (Products.Price)  FROM Products
JOIN Suppliers on (Suppliers.SupplierID = Products.SupplierID)
GROUP BY Products.SupplierID
ORDER BY AVG(Products.Price) DESC
Limit 3;


-- Which category has the most orders?
SELECT Categories.CategoryName, COUNT (OrderDetails.ProductID) 
FROM OrderDetails JOIN Products ON (Products.ProductID  = OrderDetails.ProductID) JOIN Categories ON (Categories.CategoryID = Products.CategoryID) 
GROUP BY OrderDetails.ProductID
ORDER BY COUNT (OrderDetails.ProductID) DESC;


-- Which employee made the most sales (by number of sales)?

SELECT Employees.*, COUNT(Orders.EmployeeID) FROM Orders 
JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
GROUP BY Orders.EmployeeID
ORDER BY COUNT(Orders.EmployeeID)  DESC
LIMIT 1;

-- Which employee made the most sales (by value of sales)?

SELECT Employees.*, SUM(Products.Price * OrderDetails.Quantity) AS SalesValue
FROM OrderDetails
 JOIN Orders ON OrderDetails.OrderID = Orders.OrderID
  JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
  JOIN Products ON OrderDetails.ProductID = Products.ProductID
GROUP BY Employees.EmployeeID
ORDER BY SalesValue DESC
LIMIT 1

-- which employees have BS degrees? 
SELECT * FROM Employees WHERE Notes LIKE '%BS%';

-- What supplier has the highest average product price assuming they have at least 2 products

SELECT Suppliers.*, AVG(Products.Price)
FROM Products
  JOIN Suppliers ON Products.SupplierID = Suppliers.SupplierID
GROUP BY Products.SupplierID
HAVING COUNT(Products.SupplierID) > 1
ORDER BY AVG(Products.Price) DESC
LIMIT 1