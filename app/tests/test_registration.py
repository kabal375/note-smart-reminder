import unittest
from app import app, db, controllers

class TestRegistration(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()

        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_registration_success(self):
        with app.app_context():
            data = {'username': 'test_user', 'password': 'test_password'}
            result = controllers.register_user(data['username'], data['password'])
            self.assertEqual(result['status'], 'success')

    def test_registration_duplicate_username(self):
        with app.app_context():
            # Регистрируем пользователя
            data = {'username': 'test_user', 'password': 'test_password'}
            result = controllers.register_user(data['username'], data['password'])
            self.assertEqual(result['status'], 'success')

            # Пытаемся зарегистрировать пользователя с тем же именем
            result_duplicate = controllers.register_user(data['username'], 'another_password')
            self.assertEqual(result_duplicate['status'], 'error')

if __name__ == '__main__':
    unittest.main()
