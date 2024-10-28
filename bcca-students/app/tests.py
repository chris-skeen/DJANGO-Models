from django.test import TestCase
from app import models

# Create your tests here.

class TestStudent(TestCase):
    def test_can_create_student(self):
        student = models.create_student(
            "Chris",
            "2025",
            "cskeen25@example.com",
            True,
        )

        self.assertEqual(student.name, "Chris")
        self.assertEqual(student.class_of, "2025")
        self.assertEqual(student.email, "cskeen25@example.com")
        self.assertTrue(student.enrolled, True)

    def test_can_view_all_students_at_once(self):
        students_data = [
            {
                 "name": "Chris",
                 "class_of": "2025",
                 "email" : "cskeen25@example.com",
                 "enrolled": True
            },
            {
                 "name": "Goat",
                 "class_of": "2034",
                 "email" : "goatskeen25@example.com",
                 "enrolled": False
            },
            {
                 "name": "OptimusPrime",
                 "class_of": "1999",
                 "email" : "optimusprime@example.com",
                 "enrolled": True
            },
        ]

        for student_data in students_data:
            models.create_student(
                student_data["name"],
                student_data["class_of"],
                student_data["email"],
                student_data["enrolled"],
            )

        students = models.all_students()

        self.assertEqual(len(students), len(students_data))

        students_data = sorted(students_data, key=lambda c: c["name"])
        students = sorted(students, key=lambda c: c.name)

        for data, student in zip(students_data, students):
            self.assertEqual(data["name"], student.name)
            self.assertEqual(data["class_of"], student.class_of)
            self.assertEqual(data["email"], student.email)
            self.assertEqual(data["enrolled"], student.enrolled)

    def test_can_search_by_name(self):
        students_data = [
            {
              "name": "Chris",
              "class_of": "2025",
              "email" : "cskeen25@example.com",
              "enrolled": True
            },
            {
              "name": "Goat",
              "class_of": "2034",
              "email" : "goatskeen25@example.com",
              "enrolled": False
            },
            {
              "name": "OptimusPrime",
              "class_of": "1999",
              "email" : "optimusprime@example.com",
              "enrolled": True
            },
        ]

        for student_data in students_data:
            models.create_student(
                student_data["name"],
                student_data["class_of"],
                student_data["email"],
                student_data["enrolled"],
            )

        self.assertIsNone(models.find_student_by_name("aousnth"))

        student = models.find_student_by_name("Chris")

        self.assertIsNotNone(student)
        self.assertEqual(student.email, "cskeen25@example.com")


    def test_can_view_enrolled_students(self):
        students_data = [
            {
              "name": "Chris",
              "class_of": "2025",
              "email" : "cskeen25@example.com",
              "enrolled": True
            },
            {
              "name": "Goat",
              "class_of": "2034",
              "email" : "goatskeen25@example.com",
              "enrolled": False
            },
            {
              "name": "OptimusPrime",
              "class_of": "1999",
              "email" : "optimusprime@example.com",
              "enrolled": False
            },
        ]

        for student_data in students_data:
            models.create_student(
            student_data["name"],
            student_data["class_of"],
            student_data["email"],
            student_data["enrolled"],
            )

            self.assertEqual(len(models.enrolled_students()), 1)

    def test_can_update_students_email(self):
        students_data = [
            {
              "name": "Chris",
              "class_of": "2025",
              "email" : "cskeen25@example.com",
              "enrolled": True
            },
            {
              "name": "Goat",
              "class_of": "2034",
              "email" : "goatskeen25@example.com",
              "enrolled": False
            },
            {
              "name": "OptimusPrime",
              "class_of": "1999",
              "email" : "optimusprime@example.com",
              "enrolled": False
            },
        ]

        for student_data in students_data:
            models.create_student(
                student_data["name"],
                student_data["class_of"],
                student_data["email"],
                student_data["enrolled"],
            )

        models.update_student_email("Chris", "crish@example.com")

        self.assertEqual(
            models.find_student_by_name("Chris").email, "crish@example.com"
        )

    def test_can_delete_student(self):
        students_data = [
            {
              "name": "Chris",
              "class_of": "2025",
              "email" : "cskeen25@example.com",
              "enrolled": True
            },
            {
              "name": "Goat",
              "class_of": "2034",
              "email" : "goatskeen25@example.com",
              "enrolled": False
            },
            {
              "name": "OptimusPrime",
              "class_of": "1999",
              "email" : "optimusprime@example.com",
              "enrolled": False
            },
        ]

        for student_data in students_data:
            models.create_student(
                student_data["name"],
                student_data["class_of"],
                student_data["email"],
                student_data["enrolled"],
            )

        models.delete_student("OptimusPrime")

        self.assertEqual(len(models.all_students()), 2)
