-- Create Book table

CREATE TABLE Book (

    ISBN VARCHAR(20) PRIMARY KEY,

    Title VARCHAR(100) NOT NULL,

    Genre VARCHAR(50),

    Price DECIMAL(10, 2) NOT NULL,

    PublishDate DATE,

    QuantityInStock INT

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

 

-- Create Orders table (Renamed to avoid conflict with SQL keyword ORDER)

CREATE TABLE Orders (

    OrderID INT IDENTITY(1, 1) PRIMARY KEY,

    CustomerID INT,

    OrderDate DATE,

    TotalAmount DECIMAL(10, 2),

    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)

);

 

-- Create OrderDetails table

CREATE TABLE OrderDetails (

    OrderID INT,

    ISBN VARCHAR(20),

    Quantity INT,

    PRIMARY KEY (OrderID, ISBN),

    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),

    FOREIGN KEY (ISBN) REFERENCES Book(ISBN)

);

 

-- Insert sample data

INSERT INTO Book (ISBN, Title, Genre, Price, PublishDate, QuantityInStock) VALUES

    ('ISBN-123', 'Sample Book 1', 'Fiction', 29.99, '2023-01-01', 100),

    ('ISBN-456', 'Sample Book 2', 'Mystery', 19.99, '2023-02-15', 50);

 

INSERT INTO Author (FirstName, LastName, Email) VALUES

    ('John', 'Doe', 'john.doe@example.com'),

    ('Jane', 'Smith', 'jane.smith@example.com');

 

INSERT INTO Customer (FirstName, LastName, Email, Address) VALUES

    ('Alice', 'Johnson', 'alice.johnson@example.com', '123 Main St'),

    ('Bob', 'Smith', 'bob.smith@example.com', '456 Oak Ave');

 

INSERT INTO Orders (CustomerID, OrderDate, TotalAmount) VALUES

    (1, '2023-07-31', 49.98),

    (2, '2023-08-01', 39.98);

 

INSERT INTO OrderDetails (OrderID, ISBN, Quantity) VALUES

    (1, 'ISBN-123', 2),

    (2, 'ISBN-456', 1);

-- Retrieve all books written by a specific author
SELECT b.*
FROM Book b
JOIN OrderDetails od ON b.ISBN = od.ISBN
JOIN Orders o ON od.OrderID = o.OrderID
JOIN Customer c ON o.CustomerID = c.CustomerID
JOIN Author a ON c.CustomerID = a.AuthorID
WHERE a.FirstName = 'John';


--all orders with the customer details (name, email) and the books ordered (title, quantity)
select c.FirstName, c.email, b.title, od.quantity
from customer c
join orders o on c.customerID=o.customerID
join orderdetails od on o.orderID=od.orderID
join book b on od.ISBN=b.ISBN;

-- Total revenue generated from all sales
select 	sum(TotalAmount)
from Orders;
