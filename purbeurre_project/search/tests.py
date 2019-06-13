from django.test import TestCase, Client
from .models import Categorie, Aliment

    
class SatusCodePageTestCase(TestCase):
    def setUp(self):
        self.cli = Client()
        cat = Categorie()
        cat.name = 'boisson'
        cat.save()
        alim = Aliment()
        alim.name = 'Ice Tea'
        alim.nutrition_group = 'a'
        alim.nova_group = 1
        alim.shop = 'Hyper U'
        alim.link = 'https://link.shop.com'
        alim.nutriments = "{'succre pour 100g': 12}"
        alim.categorie = cat
        alim.save()

    def test_page_index(self):
        rep = self.cli.get('/')
        self.assertEqual(rep.status_code, 200)

    def test_page_result(self):
        rep = self.cli.get('/result')
        self.assertEqual(rep.status_code, 200)

    def test_page_food_detail(self):
        rep = self.cli.get('/food_detail/1')
        self.assertEqual(rep.status_code, 200)