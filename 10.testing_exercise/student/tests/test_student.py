from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student('Ivet')

    def test_init_without_courses(self):
        self.assertEqual('Ivet', self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_init_with_courses(self):
        self.student.courses = {'Math': ['test note 1', 'test note 2']}
        self.assertEqual('Ivet', self.student.name)
        self.assertEqual({'Math': ['test note 1', 'test note 2']}, self.student.courses)

    def test_enroll_with_course_in_courses_and_append_notes(self):
        self.student.courses = {'Physics': ['test note 1']}
        result_str = self.student.enroll('Physics', ['test note 2', 'test note 3'])
        self.assertEqual({'Physics': ['test note 1', 'test note 2', 'test note 3']}, self.student.courses)
        self.assertEqual("Course already added. Notes have been updated.", result_str)

    def test_enroll_if_course_not_exist_and_add_course_is_Y(self):
        result = self.student.enroll('Math', ['test note 1'], 'Y')
        self.assertEqual({'Math': ['test note 1']}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_if_course_not_exist_and_add_course_is_empty_str(self):
        result = self.student.enroll('Math', ['test note 1'])
        self.assertEqual({'Math': ['test note 1']}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_the_course_with_no_notes(self):
        result = self.student.enroll('Math', 'test note 1', 'E')
        self.assertEqual({'Math': []}, self.student.courses)
        self.assertEqual("Course has been added.", result)

    def test_add_notes_but_course_does_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('Python', ['test note 1', 'test note 2'])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_with_existing_course(self):
        self.student.enroll('Math', [])
        result = self.student.add_notes('Math', 'test note 1')
        self.assertEqual({'Math': ['test note 1']}, self.student.courses)
        self.assertEqual("Notes have been updated", result)

    def test_leave_course_if_course_exist(self):
        self.student.enroll('Math', ['test note 1'])
        result = self.student.leave_course('Math')
        self.assertEqual({}, self.student.courses)
        self.assertEqual("Course has been removed", result)

    def test_leave_course_if_course_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('Physics')
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))
