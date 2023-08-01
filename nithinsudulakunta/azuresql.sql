CREATE TABLE Book (
  ISBN VARCHAR(20) PRIMARY KEY,
  Title VARCHAR(100) NOT NULL,
  Genre VARCHAR(50),
  Price DECIMAL(10, 2) NOT NULL,
  PublishDate DATE,
  QuantityInStock INT
);


CREATE TABLE Author (
  AuthorID INT IDENTITY(1, 1) PRIMARY KEY,
  FirstName VARCHAR(50) NOT NULL,
  LastName VARCHAR(50) NOT NULL,
  Email VARCHAR(100)
);


CREATE TABLE Customer (
  CustomerID INT IDENTITY(1, 1) PRIMARY KEY,
  FirstName VARCHAR(50) NOT NULL,
  LastName VARCHAR(50) NOT NULL,
  Email VARCHAR(100),
  Address VARCHAR(200)
);


CREATE TABLE [Order] (
  OrderID INT IDENTITY(1, 1) PRIMARY KEY,
  CustomerID INT,
  OrderDate DATE,
  TotalAmount DECIMAL(10, 2),
  FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);


CREATE TABLE OrderDetails (
  OrderID INT,
  ISBN VARCHAR(20),
  Quantity INT,
  PRIMARY KEY (OrderID, ISBN),
  FOREIGN KEY (OrderID) REFERENCES [Order](OrderID),
  FOREIGN KEY (ISBN) REFERENCES Book(ISBN)
);



INSERT INTO Book (ISBN, Title, Genre, Price, PublishDate, QuantityInStock) VALUES
  ('ISBN-123', 'Sample Book 1', 'Fiction', 29.99, '2023-01-01', 100),
  ('ISBN-456', 'Sample Book 2', 'Mystery', 19.99, '2023-02-15', 50);

INSERT INTO Author (FirstName, LastName, Email) VALUES
  ('John', 'Doe', 'john.doe@example.com'),
  ('Jane', 'Smith', 'jane.smith@example.com');

INSERT INTO Customer (FirstName, LastName, Email, Address) VALUES
  ('Alice', 'Johnson', 'alice.johnson@example.com', '123 Main St'),
  ('Bob', 'Smith', 'bob.smith@example.com', '456 Oak Ave');

INSERT INTO [Order] (CustomerID, OrderDate, TotalAmount) VALUES
  (1, '2023-07-31', 49.98),
  (2, '2023-08-01', 39.98);

INSERT INTO OrderDetails (OrderID, ISBN, Quantity) VALUES
  (1, 'ISBN-123', 2),
  (2, 'ISBN-456', 1);


select * from OrderDetails;



 -- List all orders with the customer details (name, email) and the books ordered (title, quantity).


SELECT c.FirstName, c.email, b.title, od.quantity
FROM Book b
JOIN OrderDetails od ON b.ISBN = od.ISBN
JOIN [Order] o ON o.OrderID = od.OrderID
JOIN Customer c ON c.CustomerID = o.CustomerID;


-- c. Calculate the total revenue generated from book sales by each order.

SELECT o.orderid, b.title, (od.quantity*o.TotalAmount) as total
FROM Book b
JOIN OrderDetails od ON b.ISBN = od.ISBN
join [order] o on o.orderID = od.orderID
