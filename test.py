import unittest
from app import app, Database


class Testing(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_home(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_add(self):
        response = self.app.get('/add', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_check(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertTrue(b'It uses Bootstrap, python Flask and SQLAlchemy.' in response.data)

    def test_check_add(self):
        response = self.app.get('/add', follow_redirects=True)
        self.assertTrue(b'Submit' in response.data)

    def test_columns(self):
        columns = ['id', 'firstname', 'surname', 'country', 'group_num']
        self.assertEqual(Database.__table__.columns.keys(), columns)

    def test_table_name(self):
        name = 'database'
        self.assertEqual(Database.__table__.name, name)


if __name__ == '__main__':
    unittest.main()
