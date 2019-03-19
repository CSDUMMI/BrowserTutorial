import unittest, Lessons

class TestLesson0(unittest.TestCase):

    def test_concateStrings(self):
        


lesson_0_suite = unittest.TestLoader().loadTestsFromTestCase(TestLesson0)

lesson_0 = Lessons.Lesson   (
                            mode = "code",
                            suite=lesson_0_suite
                            )
