
import mysql.connector

# 1. Connect Python to MySQL
con = mysql.connector.connect(
    host="localhost",
    user="Username",
    password="Your_my_SQL_Password",
    database="student_db"
)

cur = con.cursor()


# 2. Add a student
def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter student course: ")

    query = """
    INSERT INTO students (name, age, course)
    VALUES (%s, %s, %s)
    """
    values = (name, age, course)

    cur.execute(query, values)
    con.commit()

    print("Student added successfully!")


# 3. View all students
def view_students():
    cur.execute("SELECT * FROM students")
    records = cur.fetchall()

    if not records:
        print("No students found.")
    else:
        print("\n--- Student Records ---")
        for student in records:
            print(
                f"ID: {student[0]}, "
                f"Name: {student[1]}, "
                f"Age: {student[2]}, "
                f"Course: {student[3]}"
            )


# 4. Update student details
def update_student():
    student_id = int(input("Enter student ID to update: "))
    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    course = input("Enter new course: ")

    query = """
    UPDATE students
    SET name = %s, age = %s, course = %s
    WHERE id = %s
    """
    values = (name, age, course, student_id)

    cur.execute(query, values)
    con.commit()

    if cur.rowcount > 0:
        print("Student updated successfully!")
    else:
        print("Student ID not found or no changes made.")


# 5. Delete a student
def delete_student():
    student_id = int(input("Enter student ID to delete: "))

    query = "DELETE FROM students WHERE id = %s"
    cur.execute(query, (student_id,))
    con.commit()

    if cur.rowcount > 0:
        print("Student deleted successfully!")
    else:
        print("Student ID not found.")


# 6. Main menu
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Thank you for using Student Management System!")
        break
    else:
        print("Invalid choice. Please try again.")


# 7. Close database connection
cur.close()
con.close()

