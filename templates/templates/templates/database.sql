CREATE DATABASE internship_monitoring;

USE internship_monitoring;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(100)
);

CREATE TABLE faculty (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE daily_reports (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    report_text TEXT,
    report_date DATE,
    FOREIGN KEY (student_id) REFERENCES students(id)
);
