# Generated by Django 2.2.1 on 2019-05-16 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aliment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140, unique=True)),
                ('nutrition_group', models.CharField(max_length=2, verbose_name='Groupe nutritionnel')),
                ('nova_group', models.CharField(max_length=2)),
                ('shop', models.CharField(max_length=80, verbose_name="Boutique d'achat")),
                ('link', models.CharField(max_length=140, verbose_name='Lien internet')),
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
                ('substitute', models.IntegerField()),
                ('aliment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Aliment')),
            ],
            options={
                'verbose_name': 'favoris',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=45, verbose_name="Nom d'utilisateur")),
                ('first_name', models.CharField(max_length=45, verbose_name="Prénom d'utilisateur")),
                ('pseudo', models.CharField(max_length=45, unique=True)),
                ('email', models.EmailField(max_length=80)),
                ('password', models.CharField(max_length=88)),
                ('favoris_save', models.ManyToManyField(through='search.Favoris', to='search.Aliment')),
            ],
            options={
                'verbose_name': 'utilisateur',
            },
        ),
        migrations.AddField(
            model_name='favoris',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.User'),
        ),
        migrations.AddField(
            model_name='aliment',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Categorie'),
        ),
    ]