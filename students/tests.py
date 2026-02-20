from django.test import TestCase
from .models import Student

class StudentTest(TestCase):

    def test_student_creation(self):
        student = Student.objects.create(name="Aditya", roll_number=101)
        self.assertEqual(student.name, "Aditya")