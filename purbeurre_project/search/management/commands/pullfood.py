from django.core.management.base import BaseCommand, CommandError
from search.complete_db import category_table, food_table, main

class Command(BaseCommand):
    help = "Pull food database"

    def add_arguments(self, parser):
        """ add an argument to the command """

        parser.add_argument('table', nargs='+', type=str)

    def handle(self, *args, **options):
        """ execute an action according to the command """

        cat = [
            "boissons", "cereales-et-derives", "desserts", "fruits",
            "legumes-et-derives", "poissons", "produits-laitiers", "viandes"
        ]

        # If the argument is 'categorie' then complete the category table
        if options['table'][0] == 'category':
            result = category_table(cat)

            if result:
                self.stdout.write(self.style.SUCCESS(
                    'La table catégorie à bien été remplie.'
                    ))

            else:
                self.stdout.write(self.style.ERROR(
                    "Une erreur est survenu au niveau de la base de données."
                    ))

        # If the argument is 'food' then complete the food table
        elif options['table'][0] == 'food':
            food = main()
            result = food_table(cat, food)

            if result:
                self.stdout.write(self.style.SUCCESS(
                    'La table aliment à bien été remplie.'
                    ))

            else:
                self.stdout.write(self.style.ERROR(
                    "Une erreur est survenu au niveau de la base de données."
                ))
