from django.test import TestCase, Client
from django.contrib.auth.models import User

# Create your tests here.
class SignInTestCase(TestCase):
    def setUp(self):
        self.cli = Client()
        user_test = User.objects.create_user(username='testUser', email='testuser@founisseur.com', password='test')
        user_test.first_name = 'Tester'
        user_test.last_name = 'FooTest'
        user_test.save()
    
    def test_user_sign_in(self):
        rep = self.cli.post('/signin', {'user': 'testUser', 'password': 'test'})
        user = rep.context
        print(user)
        self.assertEqual(rep.status_code, 302)
    
class SatusCodePageTestCase(TestCase):
    def setUp(self):
        self.cli = Client()

    def test_page_index(self):
        rep = self.cli.get('/')
        self.assertEqual(rep.status_code, 200)
    
    def test_page_sign_in(self):
        rep = self.cli.get('/signin')
        self.assertEqual(rep.status_code, 200)
    
    def test_page_sign_up(self):
        rep = self.cli.get('/signup')
        self.assertEqual(rep.status_code, 200)
    
    def test_page_sing_out(self):
        rep = self.cli.get('/signout')
        self.assertEqual(rep.status_code, 200)
    
    def test_page_account(self):
        rep = self.cli.get('/account')
        self.assertEqual(rep.status_code, 200)

    def test_page_result(self):
        rep = self.cli.get('/result')
        self.assertEqual(rep.status_code, 404)