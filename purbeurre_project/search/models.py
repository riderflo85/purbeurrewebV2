from django.db import models

class Aliment(models.Model):
    name = models.CharField(max_length=220, null=False, unique=True)
    nutrition_group = models.CharField(max_length=1, verbose_name="Groupe nutritionnel")
    nova_group = models.IntegerField()
    shop = models.CharField(max_length=500, verbose_name="Boutique d'achat")
    image = models.CharField(max_length=300)
    link = models.CharField(max_length=300, verbose_name="Lien internet")
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)

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

class User(models.Model):
    last_name = models.CharField(max_length=45, null=False, verbose_name="Nom d'utilisateur")
    first_name = models.CharField(max_length=45, null=False, verbose_name="Prénom d'utilisateur")
    pseudo = models.CharField(max_length=45, null=False, unique=True)
    email = models.EmailField(max_length=80, null=False)
    password = models.CharField(max_length=88, null=False)
    favoris_save = models.ManyToManyField(Aliment, through='Favoris', through_fields=('user', 'substitute'))

    class Meta:
        verbose_name = "utilisateur"

    def __str__(self):
        return "{} {}".format(self.last_name, self.first_name)

class Favoris(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    aliment = models.ForeignKey(Aliment, on_delete=models.CASCADE)
    substitute = models.ForeignKey(Aliment, on_delete=models.CASCADE, related_name="substitu")
    # substitute = models.IntegerField()

    class Meta:
        verbose_name = "favoris"

    def __str__(self):
        return self.user
