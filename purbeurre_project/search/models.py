from django.db import models

class Aliment(models.Model):
    name = models.CharField(max_length=140, null=False, unique=True)
    categorie = models.CharField(max_length=45, null=False, unique=True)
    nutrition_group = models.CharField(max_length=2, verbose_name="Groupe nutritionnel")
    nova_group = models.CharField(max_length=2)
    shop = models.CharField(max_length=80, verbose_name="Boutique d'achat")
    link = models.CharField(max_length=140, verbose_name="Lien internet")

    class Meta:
        verbose_name = "aliment"

    def __str__(self):
        return self.name

class Categorie(models.Model):
    name = models.CharField(max_length=45, null=False, unique=True, verbose_name="Nom de la catégorie")

    class Meta:
        verbose_name = "categorie"
    
    def __str__(self):
        return self.name

class Favoris(models.Model):
    id_user = models.IntegerField(null=False)
    favoris_aliment = models.IntegerField()
    substitute = models.IntegerField()

    class Meta:
        verbose_name = "favoris"
    
    def __str__(self):
        return self.id_user

class User(models.Model):
    last_name = models.CharField(max_length=45, null=False, verbose_name="Nom d'utilisateur")
    first_name = models.CharField(max_length=45, null=False, verbose_name="Prénom d'utilisateur")
    pseudo = models.CharField(max_length=45, null=False, unique=True)
    email = models.EmailField(max_length=80, null=False)
    password = models.CharField(max_length=88, null=False)
    favoris = models.IntegerField()

    class Meta:
        verbose_name = "utilisateur"
    
    def __str__(self):
        return self.last_name + " " + self.first_name