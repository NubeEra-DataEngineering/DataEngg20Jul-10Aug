-- Create the Book table
CREATE TABLE Book (
    ISBN VARCHAR(20) PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Genre VARCHAR(100),
    Price DECIMAL(10, 2) NOT NULL,
    PublishDate DATE,
    QuantityInStock INT
);

-- Create the Author table
CREATE TABLE Author (
    AuthorID INT PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255)
);

-- Create the Customer table
CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255),
    Address VARCHAR(255)
);

-- Create the Order table
CREATE TABLE Order1 (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    TotalAmount DECIMAL(10, 2),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

-- Create the OrderDetails table (Association Table)
CREATE TABLE OrderDetails (
    OrderID INT,
    ISBN VARCHAR(20),
    Quantity INT,
    PRIMARY KEY (OrderID, ISBN),
    FOREIGN KEY (OrderID) REFERENCES Order(OrderID),
    FOREIGN KEY (ISBN) REFERENCES Book(ISBN)
);

-- Insert sample data into the Book table

INSERT INTO Book (ISBN, Title, Genre, Price, PublishDate, QuantityInStock) VALUES
  ('ISBN-123', 'Sample Book 1', 'Fiction', 29.99, '2023-01-01', 100),
  ('ISBN-456', 'Sample Book 2', 'Mystery', 19.99, '2023-02-15', 50);
-- Insert sample data into the Author table
INSERT INTO Author (FirstName, LastName, Email) VALUES
  ('John', 'Doe', 'john.doe@example.com'),
  ('Jane', 'Smith', 'jane.smith@example.com');

  -- Insert sample data into the customer table

INSERT INTO Customer (FirstName, LastName, Email, Address) VALUES
  ('Alice', 'Johnson', 'alice.johnson@example.com', '123 Main St'),
  ('Bob', 'Smith', 'bob.smith@example.com', '456 Oak Ave');

  -- Insert sample data into the order table

INSERT INTO order1 (CustomerID, OrderDate, TotalAmount) VALUES
  (1, '2023-07-31', 49.98),
  (2, '2023-08-01', 39.98);

-- Insert sample data into the order details table

INSERT INTO OrderDetails (OrderID, ISBN, Quantity) VALUES
  (1, 'ISBN-123', 2),
  (2, 'ISBN-456', 1);


  --Queries 
  --a. Retrieve all books written by a specific author.

SELECT b.*
FROM Book b
JOIN OrderDetails od ON b.ISBN = od.ISBN
JOIN order1 o ON od.OrderID = o.OrderID
JOIN Customer c ON o.CustomerID = c.CustomerID
JOIN Author a ON b.AuthorID = a.AuthorID
WHERE a.FirstName = 'John' AND a.LastName = 'Doe';

--b List all orders with the customer details (name, email) and the books ordered (title, quantity).

SELECT o.OrderID, c.FirstName, c.LastName, c.Email, b.Title, od.Quantity
FROM Order1 o
JOIN Customer c ON o.CustomerID = c.CustomerID
JOIN OrderDetails od ON o.OrderID = od.OrderID
JOIN Book b ON od.ISBN = b.ISBN;

--c Calculate the total revenue generated from book sales.

SELECT SUM(b.Price * od.Quantity) AS TotalRevenue
FROM Book b
JOIN OrderDetails od ON b.ISBN = od.ISBN;


