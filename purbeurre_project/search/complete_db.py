import requests
import json
import os
import django

try:
    from .models import Aliment, Categorie
except ModuleNotFoundError:
    pass 


def pull_data(categ, page):
    """ Récupération des données de l'API d'OpenFoodFacts """

    api = "https://fr.openfoodfacts.org/categorie/{}/{}".format(categ, page)
    payload = {"json": 1}
    response = requests.get(url=api, params=payload)
    print(response.url)
    try:
        return response.json()
    except json.decoder.JSONDecodeError:
        pass

def category_table(categ):
    """ remplissage de la table catégorie de la BDD """

    try:
        for i in categ:
            new_cat = Categorie()
            new_cat.name = i
            new_cat.save()
        return True
    except:
        return False

def food_table(cat, dico_food):
    """ remplissage de la table aliment de la BDD """

    id_cat = 1
    try:
        for i in cat:
            for food in dico_food[i]:
                new_food = Aliment()
                new_food.name = food[0]
                new_food.nutrition_group = food[1]
                new_food.nova_group = food[2]
                new_food.shop = food[3]
                new_food.image = food[4]
                new_food.link = food[5]
                new_food.nutriments = food[6]
                new_food.categorie_id = id_cat
                new_food.save()
            id_cat += 1
        return True
    except:
        return False

def delete_duplicates(categorie, dico_not_sorted):
    """ Data Sorting Function. Removes duplicates from a json file """

    list_sort = []
    temp = []
    all_temp = []
    dico_sorted = {}

    # Route every categories of food
    for cat in categorie:

        for food_list in dico_not_sorted[cat]:
            # Each food in the category is added to the sort list
            list_sort.append(food_list)

        index = -1

        # Pathways the food list that may potentially contain duplicates
        for x in list_sort[:]:
            index += 1

            # If the current food is not on the temporary list it is added
            if x[0].lower() not in temp and x[0].lower() not in all_temp:
                temp.append(x[0].lower())
                all_temp.append(x[0].lower())

            # If the current food is already in the temporary list it
            # means that the current food is a duplicate, so we delete
            # it from its list thanks to its index
            else:
                del(list_sort[index])
                index -= 1

        # Add the name of the current category and all its foods sorted
        # in a dictionary
        dico_sorted[cat] = list_sort

        # Empty the contents of both lists to be able to repeat the same
        # operation for the next category
        list_sort = []
        temp = []

    all_temp = []

    return dico_sorted

def sorted_nutriment(nut):
    """ Get back only specific nutriments """

    nut_sorted = {}
    dic_nut_accepted = {
        'fat_100g': 'Matières grasses / Lipides',
        'sugars_100g': 'Sucres',
        'saturated-fat_100g': 'Acides gras saturés',
        'salt_100g': 'Sel'
    }

    for k, v in nut.items():
        for ke, va in dic_nut_accepted.items():
            if k == ke:
                nut_sorted[va] = v
            else:
                pass
    
    return nut_sorted

def main():
    cat = [
        "boissons", "cereales-et-derives", "desserts", "fruits",
        "legumes-et-derives", "poissons", "produits-laitiers", "viandes"
        ]

    dico = {}
    list_test = []

    for i in cat:
        page = 1

        while page <= 10:
            rep = pull_data(i, page)

            for x in rep['products']:
                try:
                    pn = x["product_name_fr"].replace("\n", " ")
                    ng = x["nutrition_grade_fr"]
                    nova = x["nova_groups"]
                    st = str(x["stores_tags"]).replace("[", "")
                    st = st.replace("]", "")
                    st = st.replace("'", "")
                    img = x["image_url"]
                    url = x["url"]
                    nutriments = sorted_nutriment(x["nutriments"])
                    if pn!="" and ng!="" and nova!="" and st!="" and img!="" and url!="":
                        list_test.append([pn, ng, nova, st, img, url, nutriments])
                        dico[i] = list_test

                except:
                    pass

            page += 1
        list_test = []

    sort = delete_duplicates(cat, dico)

    return sort
    # with open('result_test.json', 'w') as file:
    #     json.dump(sort, file, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    main()