# Generated by Django 2.2.2 on 2019-06-20 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aliment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220, unique=True)),
                ('nutrition_group', models.CharField(max_length=1, verbose_name='Groupe nutritionnel')),
                ('nova_group', models.IntegerField()),
                ('shop', models.CharField(max_length=500, verbose_name="Boutique d'achat")),
                ('image', models.CharField(max_length=300)),
                ('link', models.CharField(max_length=300, verbose_name='Lien internet')),
                ('nutriments', models.TextField()),
            ],
            options={
                'verbose_name': 'aliment',
            },
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True, verbose_name='Nom de la catégorie')),
            ],
            options={
                'verbose_name': 'categorie',
            },
        ),
        migrations.CreateModel(
            name='Favoris',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('substitute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='substitu', to='search.Aliment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'favoris',
            },
        ),
        migrations.AddField(
            model_name='aliment',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Categorie'),
        ),
    ]
