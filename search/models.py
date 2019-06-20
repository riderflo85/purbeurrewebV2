from django.db import models
from django.contrib.auth.models import User

class Aliment(models.Model):
    name = models.CharField(max_length=220, null=False, unique=True)
    nutrition_group = models.CharField(max_length=1, verbose_name="Groupe nutritionnel")
    nova_group = models.IntegerField()
    shop = models.CharField(max_length=500, verbose_name="Boutique d'achat")
    image = models.CharField(max_length=300)
    link = models.CharField(max_length=300, verbose_name="Lien internet")
    nutriments = models.TextField()
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "aliment"

    def __str__(self):
        return self.name

    def get_img_url(self):
        return '/static/search/img/nut{}.png'.format(self.nutrition_group.upper())
    
    def get_nutriments(self):
        return dict(eval(self.nutriments))

class Categorie(models.Model):
    name = models.CharField(max_length=45, null=False, unique=True, verbose_name="Nom de la catégorie")

    class Meta:
        verbose_name = "categorie"

    def __str__(self):
        return self.name

class Favoris(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    substitute = models.ForeignKey(Aliment, on_delete=models.CASCADE, related_name="substitu")

    class Meta:
        verbose_name = "favoris"
