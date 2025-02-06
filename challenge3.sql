CREATE DATABASE IF NOT EXISTS Challenge3;
USE Challenge3;

DROP TABLE IF EXISTS courses;

CREATE TABLE IF NOT EXISTS courses (
    id int AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    Course_Title VARCHAR(255) NOT NULL,
    Course_Number VARCHAR(255) NOT NULL,
    Department_Name VARCHAR(255) NOT NULL,
    Instructor VARCHAR(255) NOT NULL,
    Quarter VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS course_schedule (
    schedule INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    course VARCHAR(255) NOT NULL,
    role VARCHAR(255) NOT NULL,
    week_day VARCHAR(255) NOT NULL
);

DESC courses;

INSERT INTO courses(name, Course_Title, Course_Number, Department_Name, Instructor, Quarter) 
VALUES
('Design', 'Introduction to Analog Design', 'ECE35', 'ECE', 'Schurgers', 'Fall2024');