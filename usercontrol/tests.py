from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from .forms import SignupForm, LoginForm
from .views import sign_in, sign_out, sign_up, account, change_pwd, change_email


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
            password='longpasswordtest'
        )
        user_test.first_name = 'Tester'
        user_test.last_name = 'FooTest'
        user_test.save()
        self.user = user_test

    def test_user_not_sign_in_with_view(self):
        rep = self.cli.post('/user/signin',
            {'user': 'notUser', 'password': 'longpasswordtest'}
        )
        self.assertTrue(rep.context['error'])

    def test_user_sign_in(self):
        rep = self.cli.get('/user/signin')
        self.assertEqual(rep.status_code, 200)

    def test_user_redirect_after_sign_in(self):
        rep = self.cli.post('/user/signin',
            {'user': 'testUser', 'password': 'longpasswordtest'}
        )
        self.assertEqual(rep.status_code, 302)

    def test_user_is_authenticated(self):
        rep = self.cli.login(username='testUser', password='longpasswordtest')
        self.assertTrue(rep)

        rep2 = self.cli.get('/user/signin')
        self.assertEqual(rep2.context['user'].get_username(), 'testUser')

    def test_user_is_not_authenticated(self):
        rep = self.cli.login(username='notUser', password='notPwd')
        self.assertFalse(rep)
    
    def test_user_signup(self):
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

    def test_user_signup_with_view(self):
        rep = self.cli.post('/user/signup',
            {
                'pseudo': 'secondary_user',
                'last_name': 'secondary',
                'first_name': 'user',
                'email': 'secondary.user@test.com',
                'password': 'longpasswordtest'
            }
        )
        self.assertEqual(rep.context['new_user'].username, 'secondary_user')

    def test_user_sign_out(self):
        self.cli.login(username=self.user.username,
            password='longpasswordtest'
        )
        rep = self.cli.get('/user/signout')
        user_signout = rep.context['user'].is_anonymous
        self.assertTrue(user_signout)

    def test_informations_for_account_user_page(self):
        self.cli.login(username=self.user.username,
            password='longpasswordtest'
        )
        rep = self.cli.get('/user/account')
        self.assertEqual(rep.context['first_name'], self.user.first_name)
        self.assertEqual(rep.context['last_name'], self.user.last_name)
        self.assertEqual(rep.context['email'], self.user.email)


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
        user_test = User.objects.create_user(
            username='testUser',
            email='testuser@founisseur.com',
            password='test'
        )
        user_test.first_name = 'Tester'
        user_test.last_name = 'FooTest'
        user_test.save()
        self.cli.login(username=user_test.username, password='test')

    def test_template_page_sign_in(self):
        rep = self.cli.get('/user/signin')
        self.assertTemplateUsed(rep, 'usercontrol/login.html')

    def test_template_page_sign_up(self):
        rep = self.cli.get('/user/signup')
        self.assertTemplateUsed(rep, 'usercontrol/sign_up.html')

    def test_template_page_sign_out(self):
        rep = self.cli.get('/user/signout')
        self.assertTemplateUsed(rep, 'usercontrol/sign_out.html')

    def test_template_page_account(self):
        rep = self.cli.get('/user/account')
        self.assertTemplateUsed(rep, 'usercontrol/account.html')


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


class ChangeInfosUserTestCase(TestCase):
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
        self.cli.login(username=user_test.username, password='test')
        self.user = user_test

    def test_change_email(self):
        rep = self.cli.post('/user/change_email',
            {
                'old_email': self.user.email,
                'new_email': 'newemail@fournisseur.com'
            }
        )
        self.assertTrue(rep.json()['ServerResponse'])
        self.assertEqual(
            User.objects.get(username=self.user.username).email,
            'newemail@fournisseur.com'
        )

    def test_change_email_fail(self):
        rep = self.cli.post('/user/change_email',
            {
                'old_email': 'failemial@fail.com',
                'new_email': 'newemail@fournisseur.com'
            }
        )
        self.assertFalse(rep.json()['ServerResponse'])
        self.assertNotEqual(
            User.objects.get(username=self.user.username).email,
            'newemail@fournisseur.com'
        )

    def test_change_pwd(self):
        rep = self.cli.post('/user/change_pwd',
            {
               'old_pwd': 'test',
               'new_pwd': 'newpassword'
            }
        )
        user_new_pwd = User.objects.get(username=self.user.username).password
        check_pwd = check_password('newpassword', user_new_pwd)
        self.assertTrue(rep.json()['ServerResponse'])
        self.assertTrue(check_pwd)

    def test_change_pwd_fail(self):
        rep = self.cli.post('/user/change_pwd',
            {
               'old_pwd': 'failpwd',
               'new_pwd': 'newpassword'
            }
        )
        user_new_pwd = User.objects.get(username=self.user.username).password
        check_pwd = check_password('newpassword', user_new_pwd)
        self.assertFalse(rep.json()['ServerResponse'])
        self.assertFalse(check_pwd)
