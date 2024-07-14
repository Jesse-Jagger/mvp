# tests/test_forms.py

import unittest
from app import create_app
from app.forms import RegistrationForm
from config import Config

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/test_database'
    WTF_CSRF_ENABLED = False

class FormTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_registration_form_valid(self):
        form = RegistrationForm(data={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password',
            'confirm_password': 'password',
            'first_name': 'Test',
            'last_name': 'User',
            'bio': 'This is a test user.',
            'profile_picture': 'path/to/picture'
        })
        self.assertTrue(form.validate())

    def test_registration_form_invalid(self):
        form = RegistrationForm(data={
            'username': '',
            'email': 'not-an-email',
            'password': 'password',
            'confirm_password': 'differentpassword',
            'first_name': '',
            'last_name': '',
            'bio': '',
            'profile_picture': ''
        })
        self.assertFalse(form.validate())

if __name__ == '__main__':
    unittest.main()