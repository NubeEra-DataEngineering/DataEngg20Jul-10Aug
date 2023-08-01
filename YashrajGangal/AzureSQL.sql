-- Create Book table
CREATE TABLE Book(
    ISBN VARCHAR(20) PRIMARY KEY,
    Title VARCHAR(100) NOT NULL,
    Genre VARCHAR(50),
    Price DECIMAL(10, 2) NOT NULL,
    PublishDate DATE,
    QuantityInStock INT
);

CREATE TABLE Book_Author(
	ISBN VARCHAR(20) FOREIGN KEY REFERENCES Book(ISBN),
	AuthorID INT FOREIGN KEY REFERENCES Author(AuthorID),
	PRIMARY KEY(ISBN, AuthorID)
);

-- Create Author table
CREATE TABLE Author (
    AuthorID INT IDENTITY(1, 1) PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100)
);

-- Create Customer table
CREATE TABLE Customer (
    CustomerID INT IDENTITY(1, 1) PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100),
    Address VARCHAR(200)
);

-- Create Order table
CREATE TABLE Orders (
    OrderID INT IDENTITY(1, 1) PRIMARY KEY,
    CustomerID INT FOREIGN KEY REFERENCES Customer(CustomerID),
    OrderDate DATE,
    TotalAmount DECIMAL(10, 2)
);

-- Create OrderDetails table
DROP TABLE OrderDetails;
CREATE TABLE OrderDetails (
    OrderID INT FOREIGN KEY REFERENCES Orders(OrderID),
    ISBN VARCHAR(20) FOREIGN KEY REFERENCES Book(ISBN),
    Quantity INT
    PRIMARY KEY(OrderID, ISBN)
);
--Above all DDL Commands given
--Following are all DML Commands::

-- Insert sample data
INSERT INTO Book (ISBN, Title, Genre, Price, PublishDate, QuantityInStock)
VALUES
    ('ISBN-123', 'Sample Book 1', 'Fiction', 29.99, '2023-01-01', 100),
    ('ISBN-456', 'Sample Book 2', 'Mystery', 19.99, '2023-02-15', 50);

INSERT INTO Book_Author (ISBN, AuthorID)
VALUES
    ('ISBN-123', 1),
    ('ISBN-123', 2),
    ('ISBN-456', 2);
   
INSERT INTO Author (FirstName, LastName, Email)
VALUES
    ('John', 'Doe', 'john.doe@example.com'),
    ('Jane', 'Smith', 'jane.smith@example.com');

INSERT INTO Customer (FirstName, LastName, Email, Address)
VALUES
    ('Alice', 'Johnson', 'alice.johnson@example.com', '123 Main St'),
    ('Bob', 'Smith', 'bob.smith@example.com', '456 Oak Ave');

INSERT INTO Orders (CustomerID, OrderDate, TotalAmount)
VALUES
    (1, '2023-07-31', 49.98),
    (2, '2023-08-01', 39.98);

INSERT INTO OrderDetails (OrderID, ISBN, Quantity)
VALUES
    (1, 'ISBN-123', 2),
    (2, 'ISBN-456', 1);
    
 -- 1
SELECT * 
FROM 
	Book b 
	JOIN Book_Author ba ON b.ISBN = ba.ISBN
	JOIN Author a ON ba.AuthorID = a.AuthorID
WHERE
	a.FirstName like 'Jane' AND a.LastName LIKE 'Smith';
 
SELECT * FROM Author a ;

-- 2. List all orders with the customer details (name, email) and the books ordered (title, quantity)
SELECT c.FirstName, c.LastName, c.Email, b.Title, od.Quantity
FROM Book b 
	JOIN OrderDetails od ON b.ISBN = od.ISBN 
	JOIN Orders o ON o.OrderID = od.OrderID 
	JOIN Customer c ON c.CustomerID = o.CustomerID

-- 3. Calculate the total revenue generated from book sales
SELECT *, (rev.revenue - cost.total_cost) as profit
FROM 
(SELECT sum(o.TotalAmount) as revenue
FROM Orders o) rev,
(SELECT SUM(b.Price * od.Quantity) as total_cost
FROM Book b 
	JOIN OrderDetails od ON b.ISBN = od.ISBN ) cost;