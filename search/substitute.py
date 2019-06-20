from .models import Aliment


def substitute(food_search):
    """ Propose a substitute for the search food """
    food_sub = Aliment.objects.filter(
        nutrition_group='a'
    ).filter(
        categorie=food_search.categorie.id
    )
    if food_sub:
        return food_sub
    else:
        return None
