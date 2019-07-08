from django.test import TestCase, Client
from django.contrib.auth.models import User
from .forms import SignupForm, LoginForm
from .views import sign_in, sign_out, sign_up, account


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


class UserAuthenticateTestCase(TestCase):
    def setUp(self):
        self.cli = Client()
        user_test = User.objects.create_user(
            username='testUser',
            email='testuser@founisseur.com',
            password='test'
        )
        user_test.first_name = 'Tester'
        user_test.last_name = 'FooTest'
        user_test.save()

    def test_user_sign_in(self):
        rep = self.cli.get('/user/signin')
        self.assertEqual(rep.status_code, 200)

    def test_user_redirect_after_sign_in(self):
        rep = self.cli.post('/user/signin',
            {'user': 'testUser', 'password': 'test'}
        )
        self.assertEqual(rep.status_code, 302)

    def test_user_is_authenticated(self):
        rep = self.cli.login(username='testUser', password='test')
        self.assertTrue(rep)

        rep2 = self.cli.get('/user/signin')
        self.assertEqual(rep2.context['user'].get_username(), 'testUser')

    def test_user_is_not_authenticated(self):
        rep = self.cli.login(username='notUser', password='notPwd')
        self.assertFalse(rep)
    
    def test_signup(self):
        user_test2 = User.objects.create_user(
            username='testUser2',
            email='testuser@founisseur.com',
            password='test'
        )
        user_test2.first_name = 'Tester'
        user_test2.last_name = 'FooTest'
        user_test2.save()
        rep = User.objects.get(username__contains='testUser2')
        self.assertEqual(rep.username, 'testUser2')


class FormTestCase(TestCase):
    def test_form_sign_up(self):
        form_data = {
            'pseudo': 'testUser',
            'last_name': 'FooTest',
            'first_name': 'Tester',
            'email': 'testuser@founisseur.com',
            'password': 'longpasswordtest'
        }
        form = SignupForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_sign_in(self):
        form_data = {
            'user': 'testUser',
            'password': 'longpasswordtest',
        }
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())


class TemplateRenderTestCase(TestCase):
    def setUp(self):
        self.cli = Client()

    def test_template_page_sign_in(self):
        rep = self.cli.get('/sign_in')
        self.assertTemplateUsed('/user/login.html')

    def test_template_page_sign_up(self):
        rep = self.cli.get('/sign_up')
        self.assertTemplateUsed('/user/sign_up.html')

    def test_template_page_sign_out(self):
        rep = self.cli.get('/sign_out')
        self.assertTemplateUsed('/user/sign_out.html')

    def test_template_page_account(self):
        rep = self.cli.get('/account')
        self.assertTemplateUsed('/user/account.html')


class ViewsUsedTestCase(TestCase):
    def setUp(self):
        self.cli = Client()

    def test_views_page_sing_in(self):
        rep = self.cli.get('/user/signin')
        self.assertEqual(rep.resolver_match.func, sign_in)

    def test_views_page_sing_up(self):
        rep = self.cli.get('/user/signup')
        self.assertEqual(rep.resolver_match.func, sign_up)

    def test_views_page_sing_out(self):
        rep = self.cli.get('/user/signout')
        self.assertEqual(rep.resolver_match.func, sign_out)

    def test_views_page_account(self):
        rep = self.cli.get('/user/account')
        self.assertEqual(rep.resolver_match.func, account)