-- Видалення та створення бази даних
DROP DATABASE IF EXISTS lab_4;
CREATE DATABASE lab_4;
USE lab_4;

-- Видалення таблиць, якщо вони існують
DROP TABLE IF EXISTS User_Preferences, Reservations, Property_Amenities, Property_Features, Photos, Payments, Reviews, Bookings, Properties, Users;

-- Створення таблиці Users (Користувачі)
CREATE TABLE Users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    user_type ENUM('renter', 'owner') NOT NULL,
    account_balance DECIMAL(10, 2) DEFAULT 0.00,
    registration_date DATE NOT NULL
) ENGINE = INNODB;

-- Створення таблиці Properties (Нерухомість)
CREATE TABLE Properties (
    property_id INT PRIMARY KEY AUTO_INCREMENT,
    owner_id INT NOT NULL,
    address VARCHAR(255) NOT NULL,
    description TEXT,
    rooms INT NOT NULL,
    price_per_night DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (owner_id) REFERENCES Users(user_id) ON DELETE CASCADE
) ENGINE = INNODB;

-- Створення таблиці Bookings (Бронювання)
CREATE TABLE Bookings (
    booking_id INT PRIMARY KEY AUTO_INCREMENT,
    property_id INT NOT NULL,
    renter_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    status ENUM('pending', 'confirmed', 'cancelled') NOT NULL,
    FOREIGN KEY (property_id) REFERENCES Properties(property_id) ON DELETE CASCADE,
    FOREIGN KEY (renter_id) REFERENCES Users(user_id) ON DELETE CASCADE
) ENGINE = INNODB;

CREATE TABLE Authors (
    author_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    bio TEXT
);

CREATE TABLE Books (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    author_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    published_year INT,
    genre VARCHAR(50),
    FOREIGN KEY (author_id) REFERENCES Authors(author_id) ON DELETE CASCADE
);

INSERT INTO Users (name, email, password, user_type, account_balance, registration_date) VALUES
('John Doe', 'john.doe@example.com', 'password123', 'renter', 150.00, '2023-01-10'),
('Jane Smith', 'jane.smith@example.com', 'password456', 'owner', 500.00, '2023-02-15'),
('Alice Johnson', 'alice.johnson@example.com', 'password789', 'renter', 80.00, '2023-03-20'),
('Bob Brown', 'bob.brown@example.com', 'password987', 'owner', 700.00, '2023-04-05'),
('Charlie Wilson', 'charlie.wilson@example.com', 'password654', 'renter', 120.00, '2023-05-12'),
('David Miller', 'david.miller@example.com', 'password321', 'renter', 200.00, '2023-06-15'),
('Emily Clark', 'emily.clark@example.com', 'password111', 'owner', 1000.00, '2023-07-10'),
('Frank Wright', 'frank.wright@example.com', 'password222', 'renter', 90.00, '2023-08-01'),
('Grace Lee', 'grace.lee@example.com', 'password333', 'owner', 550.00, '2023-09-20'),
('Henry Thompson', 'henry.thompson@example.com', 'password444', 'renter', 300.00, '2023-10-05');


INSERT INTO Properties (owner_id, address, description, rooms, price_per_night) VALUES
(2, '123 Main St, Cityville', 'Spacious 2-bedroom apartment in the city center', 2, 75.00),
(4, '456 Oak St, Townsville', 'Cozy cottage with a garden', 3, 50.00),
(2, '789 Pine St, Suburbia', 'Modern apartment with great views', 1, 100.00),
(4, '321 Elm St, Lakeside', 'Lakefront cabin with private dock', 4, 120.00),
(2, '654 Maple St, Villagetown', 'Charming studio apartment', 1, 40.00),
(6, '987 Birch St, Mountainville', 'Mountain cabin near hiking trails', 3, 150.00),
(8, '432 Spruce St, Cityville', 'Compact apartment near downtown', 1, 60.00),
(9, '876 Cedar St, Lakeside', 'Lakeside villa with private garden', 5, 200.00),
(2, '567 Palm St, Beachville', 'Beachfront condo with ocean view', 2, 180.00),
(10, '768 Oak St, Townsville', 'Cozy studio near the park', 1, 55.00);



INSERT INTO Bookings (property_id, renter_id, start_date, end_date, status) VALUES
(1, 1, '2023-06-01', '2023-06-07', 'confirmed'),
(2, 3, '2023-06-10', '2023-06-12', 'confirmed'),
(3, 1, '2023-07-01', '2023-07-05', 'pending'),
(4, 5, '2023-07-15', '2023-07-18', 'cancelled'),
(5, 1, '2023-08-01', '2023-08-03', 'confirmed'),
(6, 6, '2023-09-01', '2023-09-05', 'confirmed'),
(7, 8, '2023-09-15', '2023-09-20', 'pending'),
(8, 9, '2023-10-01', '2023-10-05', 'cancelled'),
(9, 1, '2023-10-10', '2023-10-12', 'confirmed'),
(10, 5, '2023-10-20', '2023-10-25', 'confirmed');

INSERT INTO Authors (name, bio) VALUES
('George Orwell', 'English novelist and essayist, known for "1984" and "Animal Farm".'),
('Jane Austen', 'English novelist known for her romantic fiction, like "Pride and Prejudice".'),
('Mark Twain', 'American writer known for "Adventures of Huckleberry Finn" and "Tom Sawyer".'),
('J.K. Rowling', 'British author, famous for the "Harry Potter" series.'),
('F. Scott Fitzgerald', 'American novelist known for "The Great Gatsby".'),
('Agatha Christie', 'English writer, known as the Queen of Mystery for her detective novels.'),
('Ernest Hemingway', 'American novelist known for his succinct style and "The Old Man and the Sea".'),
('Charles Dickens', 'English writer known for novels like "Great Expectations" and "Oliver Twist".'),
('Leo Tolstoy', 'Russian author, known for "War and Peace" and "Anna Karenina".'),
('Gabriel Garcia Marquez', 'Colombian novelist known for "One Hundred Years of Solitude".');

INSERT INTO Books (author_id, title, published_year, genre) VALUES
(1, '1984', 1949, 'Dystopian'),
(1, 'Animal Farm', 1945, 'Political Satire'),
(2, 'Pride and Prejudice', 1813, 'Romance'),
(2, 'Sense and Sensibility', 1811, 'Romance'),
(3, 'Adventures of Huckleberry Finn', 1884, 'Adventure'),
(3, 'The Adventures of Tom Sawyer', 1876, 'Adventure'),
(4, 'Harry Potter and the Sorcerer\'s Stone', 1997, 'Fantasy'),
(4, 'Harry Potter and the Chamber of Secrets', 1998, 'Fantasy'),
(5, 'The Great Gatsby', 1925, 'Tragedy'),
(6, 'Murder on the Orient Express', 1934, 'Mystery');



-- Додавання індексів

--  Це дозволить швидше фільтрувати користувачів за типом
CREATE INDEX idx_user_type ON Users(user_type);

-- Це допоможе швидко отримувати бронювання за датою початку.
CREATE INDEX idx_booking_start_date ON Bookings(start_date);

-- Це допоможе швидко шукати нерухомість за адресою.
CREATE INDEX idx_property_address ON Properties(address);
