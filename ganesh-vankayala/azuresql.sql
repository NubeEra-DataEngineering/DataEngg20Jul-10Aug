--6 (a)

SELECT b.*

FROM Book b

JOIN OrderDetails od ON b.ISBN = od.ISBN

JOIN Orders o ON od.OrderID = o.OrderID

JOIN Customer c ON o.CustomerID = c.CustomerID

JOIN Author a ON c.CustomerID = a.AuthorID

WHERE a.FirstName = 'John'
-- 6 (b)

 

SELECT c.FirstName AS CustomerFirstName,

       c.LastName AS CustomerLastName,

       c.Email AS CustomerEmail,

       b.Title AS BookTitle,

       od.Quantity AS QuantityOrdered

FROM Customer c

JOIN Orders o ON c.CustomerID = o.CustomerID

JOIN OrderDetails od ON o.OrderID = od.OrderID

JOIN Book b ON od.ISBN = b.ISBN;

-- 6 (c)

select sum(totalamount) as Revenue from [dbo].[Orders]
