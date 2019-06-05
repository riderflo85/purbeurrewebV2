from django.test import TestCase, Client

    
class SatusCodePageTestCase(TestCase):
    def setUp(self):
        self.cli = Client()

    def test_page_index(self):
        rep = self.cli.get('/')
        self.assertEqual(rep.status_code, 200)

    def test_page_result(self):
        rep = self.cli.get('/result')
        self.assertEqual(rep.status_code, 404)