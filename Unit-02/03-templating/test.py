from app import app
import unittest

class TestTemplateRoutes(unittest.TestCase):

    def test_welcome(self):
        tester = app.test_client(self)
        response = tester.get('/person/bob/20', content_type='html/text')
        self.assertIn(b'bob 20', response.data)
        self.assertEqual(response.status_code, 200)

        response = tester.get('/person/bob', content_type='html/text')
        self.assertEqual(response.status_code, 404)

        response = tester.get('/person', content_type='html/text')
        self.assertEqual(response.status_code, 404)

    def test_calculate(self):
        tester = app.test_client(self)
        response = tester.get('/calculate', content_type='html/text')
        self.assertIn(b'add subtract multply divide', response.data)
        self.assertEqual(response.status_code, 200)

    def test_math(self):
        tester = app.test_client(self)
        response = tester.get('/math?num1=10&num2=20?calculation=add', content_type='html/text')
        self.assertIn(b'30', response.data)
        self.assertEqual(response.status_code, 200)

        response = tester.get('/math?num1=10&num2=20?calculation=subtract', content_type='html/text')
        self.assertIn(b'-10', response.data)
        self.assertEqual(response.status_code, 200)

        response = tester.get('/math?num1=10&num2=120?calculation=multiply', content_type='html/text')
        self.assertIn(b'1200', response.data)
        self.assertEqual(response.status_code, 200)

        response = tester.get('/math?num1=20&num2=20?calculation=divide', content_type='html/text')
        self.assertIn(b'1', response.data)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()