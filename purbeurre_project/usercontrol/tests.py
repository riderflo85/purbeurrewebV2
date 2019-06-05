from django.test import TestCase, Client
from django.contrib.auth.models import User

class StatusCodePageTestCase(TestCase):
    def setUp(self):
        self.cli = Client()

    def test_page_sign_in(self):
        rep = self.cli.get('/user/signin')
        self.assertEqual(rep.status_code, 200)

    def test_page_sign_up(self):
        rep = self.cli.get('/user/signup')
        self.assertEqual(rep.status_code, 200)

    def test_page_sing_out(self):
        rep = self.cli.get('/user/signout')
        self.assertEqual(rep.status_code, 200)

    def test_page_account(self):
        rep = self.cli.get('/user/account')
        self.assertEqual(rep.status_code, 302)

class SignInTestCase(TestCase):
    def setUp(self):
        self.cli = Client()
        user_test = User.objects.create_user(username='testUser', email='testuser@founisseur.com', password='test')
        user_test.first_name = 'Tester'
        user_test.last_name = 'FooTest'
        user_test.save()

    def test_user_redirect_after_sign_in(self):
        rep = self.cli.post('/user/signin', {'user': 'testUser', 'password': 'test'})
        self.assertEqual(rep.status_code, 302)
    
    def test_user_sign_in(self):
        rep = self.cli.get('/user/signin')
        print(rep)
        self.assertEqual(rep.status_code, 200)