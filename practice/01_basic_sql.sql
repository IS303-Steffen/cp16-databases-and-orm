/*
IMPORTANT:
You WILL NOT be tested on your knowledge of SQL.

However, reviewing some of the basics of SQL will make working with
peewee ORM easier to understand.

*/

-- =====================
-- SELECTING ALL COLUMNS
-- =====================

-- Overview of SQL Commands

-- Selecting everything from a table
SELECT * FROM author;

-- Selecting specific columns from a table
SELECT name, birth_year FROM author;

-- Selecting with a WHERE clause
SELECT * FROM book WHERE year_published > 2000;

-- Ordering results
SELECT * FROM book ORDER BY pages DESC;

-- Joining two tables together
SELECT 
    author.name AS author_name, 
    book.title AS book_title, 
    book.year_published 
FROM author
JOIN book ON author.author_id = book.author_id;

-- Grouping by and aggregating data
-- Example: Number of books by each author
SELECT 
    author.name AS author_name, 
    COUNT(book.book_id) AS number_of_books 
FROM author
JOIN book ON author.author_id = book.author_id
GROUP BY author.author_id
ORDER BY number_of_books DESC;
