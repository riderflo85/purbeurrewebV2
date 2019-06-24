from django.test import TestCase, Client
from .models import Categorie, Aliment
from .complete_db import category_table, sorted_nutriment
from .substitute import substitute


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
        rep = self.cli.get('/food_detail/6')
        self.assertEqual(rep.status_code, 200)

    def test_page_legal_mention(self):
        rep = self.cli.get('/mention_legale')
        self.assertEqual(rep.status_code, 200)


class RenderTemplateTestCase(TestCase):
    def setUp(self):
        self.cli = Client()
        cat = Categorie()
        cat.name = 'Dessert'
        cat.save()
        alim = Aliment()
        alim.name = 'Cookie'
        alim.nutrition_group = 'a'
        alim.nova_group = 1
        alim.shop = 'Hyper U'
        alim.link = 'https://link.shop.com'
        alim.nutriments = "{'succre pour 100g': 12}"
        alim.categorie = cat
        alim.save()

    def test_template_page_index(self):
        rep = self.cli.get('/')
        self.assertTemplateUsed(rep, 'search/index.html')

    def test_template_page_result(self):
        rep = self.cli.get('/result')
        self.assertTemplateUsed(rep, 'search/no_search.html')

    def test_template_page_food_detail(self):
        rep = self.cli.get('/food_detail/3')
        self.assertTemplateUsed(rep, 'search/food_detail.html')

    def test_template_page_legal_mention(self):
        rep = self.cli.get('/mention_legale')
        self.assertTemplateUsed(rep, 'search/legal_mention.html')


class FunctionCompleteDbTestCase(TestCase):
    def setUp(self):
        self.food = {"fruits": [
            [
                "Figues moelleuses",
                "b",
                3,
                "lidl",
                "https://static.openfoodfacts.org/images/products/20534462/front_fr.9.400.jpg",
                "https://fr.openfoodfacts.org/produit/20534462/figues-moelleuses-alesto",
                {
                    "saturated-fat_value": 0.6,
                    "nutrition-score-uk_100g": 1,
                    "fat_serving": 0.375,
                    "salt_serving": 0.035,
                    "carbohydrates_serving": 12.2,
                    "sodium_serving": 0.0138,
                    "fiber_100g": 6.9,
                    "sodium": 0.0551181102362205,
                    "energy_value": 249,
                    "fruits-vegetables-nuts_value": 100,
                    "salt_unit": "g",
                    "fat": 1.5,
                    "nova-group": 3,
                    "fiber_serving": 1.73,
                    "salt_value": 0.14,
                    "proteins_unit": "g",
                    "proteins_value": 3.3,
                    "fiber_value": 6.9,
                    "sodium_value": 0.0551181102362205,
                    "carbohydrates_unit": "g",
                    "fiber_unit": "g",
                    "fat_value": 1.5,
                    "nutrition-score-uk": 1,
                    "sodium_100g": 0.0551181102362205,
                    "sugars": 48.6,
                    "saturated-fat_unit": "g",
                    "carbohydrates_100g": 48.6,
                    "energy_unit": "kcal",
                    "fruits-vegetables-nuts_serving": 100,
                    "fat_100g": 1.5,
                    "sugars_100g": 48.6,
                    "saturated-fat_100g": 0.6,
                    "fat_unit": "g",
                    "nova-group_serving": 3,
                    "proteins": 3.3,
                    "fiber": 6.9,
                    "fruits-vegetables-nuts_100g": 100,
                    "sodium_unit": "g",
                    "nutrition-score-fr": 1,
                    "fruits-vegetables-nuts_label": "0",
                    "sugars_value": 48.6,
                    "fruits-vegetables-nuts_unit": "g",
                    "saturated-fat": 0.6,
                    "carbohydrates_value": 48.6,
                    "salt_100g": 0.14,
                    "sugars_unit": "g",
                    "energy_serving": 260,
                    "saturated-fat_serving": 0.15,
                    "sugars_serving": 12.2,
                    "nutrition-score-fr_100g": 1,
                    "salt": 0.14,
                    "energy": 1042,
                    "proteins_100g": 3.3,
                    "proteins_serving": 0.825,
                    "energy_100g": 1042,
                    "carbohydrates": 48.6,
                    "nova-group_100g": 3,
                    "fruits-vegetables-nuts": 100
                }
            ]
        ]}
        self.food_nut = self.food['fruits'][0][6]
        self.category = ['fruits', 'légumes', 'viandes']

    def test_save_category_in_data_base(self):
        self.assertTrue(category_table(self.category))

    def test_sorted_nutriment(self):
        nut_sorted = sorted_nutriment(self.food_nut)
        result = {
            'Matières grasses / Lipides': 1.5,
            'Sucres': 48.6,
            'Acides gras saturés': 0.6,
            'Sel': 0.14
        }
        self.assertEqual(nut_sorted, result)


class FunctionSubstituteTestCase(TestCase):
    def setUp(self):
        cat = Categorie()
        cat.name = 'Fruit'
        cat.save()
        alim1 = Aliment()
        alim1.name = 'Pomme'
        alim1.nutrition_group = 'c'
        alim1.nova_group = 2
        alim1.shop = 'Hyper U'
        alim1.link = 'https://link.shop.com'
        alim1.nutriments = "{'succre pour 100g': 12}"
        alim1.categorie = cat
        alim1.save()
        alim2 = Aliment()
        alim2.name = 'Fraise'
        alim2.nutrition_group = 'a'
        alim2.nova_group = 1
        alim2.shop = 'Lidl'
        alim2.link = 'https://link.shop.com'
        alim2.nutriments = "{'succre pour 100g': 12}"
        alim2.categorie = cat
        alim2.save()
    
    def test_result_substitute(self):
        food = Aliment.objects.get(name='Pomme')
        sub = substitute(food)
        self.assertQuerysetEqual(sub, {'<Aliment: Fraise>': 1}, ordered=False)
        self.assertEqual(sub[0].name, 'Fraise')