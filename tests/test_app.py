from unittest import TestCase

from app import app


class TestApp(TestCase):

    def setUp(self) -> None:
        app.testing = True

    def test_index(self):
        with app.test_client() as client:
            res = client.get('/')
            self.assertEqual(200, res.status_code)
            self.assertIn(b'<h1>flipdot Transparenzberichte</h1>', res.data)
