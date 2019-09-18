from unittest import TestCase

from app import app


class TestApp(TestCase):

    def setUp(self) -> None:
        app.testing = True

    def test_index(self):
        with app.test_client() as client:
            res = client.get('/')
            self.assertEqual(200, res.status_code)
            self.assertIn(b'<h1>Hello world!</h1>', res.data)

    def test_about(self):
        with app.test_client() as client:
            res = client.get('/about/')
            self.assertEqual(200, res.status_code)
            self.assertIn(b'<h1>About</h1>', res.data)
