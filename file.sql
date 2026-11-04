USE student_db;
CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT,
    course VARCHAR(100)
);
INSERT INTO students (name, age, course)
VALUES ('Rahul', 21, 'Python');
SELECT * FROM students;