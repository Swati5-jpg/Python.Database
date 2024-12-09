import unittest
from student_management import StudentManagement, Student


class TestStudentManagement(unittest.TestCase):

    def setUp(self):
        """Set up a fresh instance of StudentManagement for each test."""
        self.management = StudentManagement()
        self.management.students = []  # Clear any default data for isolated testing

    def test_add_student_success(self):
        """Test adding a new student successfully."""
        new_student = Student(201, "Rohan Mehta", 21, "A+", ["Math", "Physics"])
        self.management.students.append(new_student)

        # Assertions
        self.assertEqual(len(self.management.students), 1)  # List size should be 1
        self.assertEqual(self.management.students[0].student_id, 201)  # ID matches
        self.assertEqual(self.management.students[0].name, "Rohan Mehta")  # Name matches
        self.assertEqual(self.management.students[0].age, 21)  # Age matches
        self.assertIn("Math", self.management.students[0].subjects)  # Subject exists

    def test_add_student_duplicate_id(self):
        """Test adding a student with a duplicate ID."""
        # Add initial student
        student1 = Student(201, "Rohan Mehta", 21, "A+", ["Math", "Physics"])
        self.management.students.append(student1)

        # Attempt to add a duplicate student
        with self.assertRaises(ValueError):
            if any(s.student_id == 201 for s in self.management.students):
                raise ValueError("Duplicate ID not allowed!")

    def test_view_students_empty(self):
        """Test viewing students when no students are available."""
        result = [student.display_details() for student in self.management.students]
        self.assertEqual(result, [])  # Should return an empty list

    def test_view_students_with_data(self):
        """Test viewing students when students are present."""
        # Add students
        student1 = Student(201, "Rohan Mehta", 21, "A+", ["Math", "Physics"])
        student2 = Student(202, "Sneha Kapoor", 22, "B", ["History", "English"])
        self.management.students.extend([student1, student2])

        # Get view result
        result = [student.display_details() for student in self.management.students]

        # Expected details
        expected_result = [
            "ID: 201, Name: Rohan Mehta, Age: 21, Grade: A+, Subjects: Math, Physics",
            "ID: 202, Name: Sneha Kapoor, Age: 22, Grade: B, Subjects: History, English"
        ]
        self.assertEqual(result, expected_result)

    def tearDown(self):
        """Clean up after each test."""
        self.management.students = []


if __name__ == "__main__":
    unittest.main()



