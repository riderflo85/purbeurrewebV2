from django.test import TestCase, Client
from django.contrib.auth.models import User

# Create your tests here.
class SignInTestCase(TestCase):
    def setUp(self):
        user_test = User.objects.create_user(username='testUser', email='testuser@founisseur.com', password='test')
        user_test.first_name = 'Tester'
        user_test.last_name = 'FooTest'
        user_test.save()
    
    