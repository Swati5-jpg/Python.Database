import unittest
from unittest.mock import patch
from student_management import Student, StudentManagement

class TestAddStudent(unittest.TestCase):
    
    def setUp(self):
        """Initialize a fresh StudentManagement instance before each test."""
        self.sm = StudentManagement()
        self.sm.students = []  # Ensure we start with an empty list of students

    @patch("builtins.input", side_effect=["201", "Anvita Mishra", "20", "A", "Math, Science"])
    def test_add_student_success(self, mock_input):
        """Test adding a new student successfully."""
        # Call the method to add a student
        self.sm.add_student()

        # Check if the student was added
        self.assertEqual(len(self.sm.students), 1)
        student = self.sm.students[0]
        self.assertEqual(student.student_id, 201)
        self.assertEqual(student.name, "Anvita Mishra")
        self.assertEqual(student.age, 20)
        self.assertEqual(student.grade, "A")
        self.assertEqual(student.subjects, ["Math", "Science"])

    @patch("builtins.input", side_effect=["201", "Anvita Mishra", "twenty", "A", "Math, Science"])
    def test_add_student_invalid_age(self, mock_input):
        """Test adding a student with an invalid age."""
        self.sm.add_student()
        self.assertEqual(len(self.sm.students), 0)

    @patch("builtins.input", side_effect=["201", "Anvita Mishra", "20", "A", ""])
    def test_add_student_empty_subjects(self, mock_input):
        """Test adding a student with no subjects provided."""
        self.sm.add_student()
        self.assertEqual(len(self.sm.students), 0)

    @patch("builtins.input", side_effect=["201", "Anvita Mishra", "20", "A", "Math, Science"])
    def test_add_student_duplicate_id(self, mock_input):
        """Test adding a student with a duplicate student ID."""
        # First, add a student with ID 201
        self.sm.add_student()

        # Try adding another student with the same ID
        self.sm.add_student()

        # Check if the second student was not added due to duplicate ID
        self.assertEqual(len(self.sm.students), 1)

if __name__ == "__main__":
    unittest.main()
