

use db;



select * from information_schema.tables;

-- Create Book table
CREATE TABLE Book (
    ISBN VARCHAR(20) primary key,
    Title VARCHAR(100) NOT NULL,
    Genre VARCHAR(50),
    Price DECIMAL(10, 2) NOT NULL,
    PublishDate DATE,
    QuantityInStock INT
);

-- Create Author table
CREATE TABLE Author (
    AuthorID INT IDENTITY(1, 1) primary key,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100)
);

-- Create Customer table
CREATE TABLE Customer (
    CustomerID INT IDENTITY(1, 1) primary key,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100),
    Address VARCHAR(200)
);

-- Create Order table
CREATE TABLE orders (
    OrderID INT IDENTITY(1, 1) primary key,
    CustomerID INT ,
    OrderDate DATE,
    TotalAmount DECIMAL(10, 2),
    foreign key (customerID) references Customer(CustomerID)
);

-- Create OrderDetails table
CREATE TABLE OrderDetails (
    OrderID INT ,
    ISBN VARCHAR(20) ,
    Quantity INT,
    foreign key (orderID) references Orders(OrderID),
    foreign key (ISBN) references Book(ISBN)
    
);



-- Insert sample data
INSERT INTO Book (ISBN, Title, Genre, Price, PublishDate, QuantityInStock)
VALUES
    ('ISBN-123', 'Sample Book 1', 'Fiction', 29.99, '2023-01-01', 100),
    ('ISBN-456', 'Sample Book 2', 'Mystery', 19.99, '2023-02-15', 50);

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
    
select * from book;

select * from orders;

select * from author;

select * from OrderDetails ;



exec sp_columns book;

-- query 3

select sum(totalamount) as 'Total Revenue' from orders;

-- query 2

select c.firstname,c.email, b.title,od.quantity from 
customer c inner join Orders o on
c.customerid = o.customerid inner join
OrderDetails od on o.orderid = od.orderid inner join 
book b on b.isbn = od.isbn;










