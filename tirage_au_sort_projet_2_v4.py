# -*- coding: utf-8 -*-
"""Tirage_au_sort_projet_2_v4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VJk-DYUDmhoHrCjos2e5TxdQz_Ai4Eah
"""

# Tirage au sort pour le projet 2 de 14 personnes dont 4 têtes de séries #
# Ce tirage prend en compte les précédents groupes du projet 1 #
# Le résultat voulu : 2 groupes de 4 personnes et 2 groupes de 3 personnes #
# Contrainte : Aucun des participants ne doit avoir travaillé ensemble avant #
# Période conception : octobre 2023 #

!pip install faker
!pip install iteration_utilities

import random  # Import bibliothèque random
from faker import Faker  # Pour créer des faux noms
from iteration_utilities import duplicates
from iteration_utilities import unique_everseen

# Groupes projet 1
# groupe a = jacques, noemie, anne, laurent
# groupe b = laure, lucien, georges, joachim
# groupe c = louis, amelie, etienne
# groupe d = felix, jose, patrick

def group_number():  # Choix du nombre groupe
    group_nb = len(heads.items())
    return group_nb

def list_group_name():  # Création de la liste des noms de groupe(s)
    group_nber = group_number()
    l_group_name = []
    fake = Faker()
    for i in range(group_nber):
        l_group_name.append(fake.name())
    return l_group_name

def heads_draw():  # Tirage au sort des têtes de séries + Ajout dans chaque liste dans un dictionnaire
    li_group_name = list_group_name()
    group_name = dict()
    new_heads = dict()
    for i in range(len(li_group_name)):
        group_name[li_group_name[i]] = list()
        choice_heads_keys = random.choice(list(heads.keys()))
        choice_heads_values_0 = heads[choice_heads_keys]
        group_name[li_group_name[i]].append(choice_heads_keys)
        new_heads[choice_heads_keys] = choice_heads_values_0
        del heads[choice_heads_keys]
    return group_name, new_heads

def others_draw():  # Tirage au sort du reste des prticipants + Ajout dans chaque liste dans un dictionnaire
    tuple_heads_draw = heads_draw()[0:2]
    group_name_dict = tuple_heads_draw[0]
    group_name_dict_length = len(group_name_dict.items())
    new_heads_dict = tuple_heads_draw[1]
    # Déterminer la taille minimum des groupes et le restant à répartir
    total_length = len(new_heads_dict.items()) + len(others.items())
    repartition_nb = 0
    rest_0 = (total_length - repartition_nb) % (len(new_heads_dict.items()))
    while rest_0 != 0:
        repartition_nb += 1
        rest_0 = (total_length - repartition_nb) % (len(new_heads_dict.items()))
    nb_min_per_group = int(total_length - repartition_nb) / (len(new_heads_dict.items()))
    # Attribution des participants aux groupes
    for key_group_name, value_group_name in group_name_dict.items():
        i = 1
        for key_heads, value_heads in new_heads_dict.items():
            if i < nb_min_per_group and repartition_nb != 0:
                choice_others_keys = random.choice(list(others.keys()))
                choice_others_values = others[choice_others_keys]
                group_name_dict[key_group_name].append(choice_others_keys)
                del others[choice_others_keys]
                repartition_nb -= 1
                i += 1
            else:
                if i < nb_min_per_group:
                    choice_others_keys = random.choice(list(others.keys()))
                    choice_others_values = others[choice_others_keys]
                    group_name_dict[key_group_name].append(choice_others_keys)
                    del others[choice_others_keys]
                    i += 1
                else:
                    if len(others.items()) < len(new_heads_dict.items()):
                        break
                    else:
                        choice_others_keys = random.choice(list(others.keys()))
                        choice_others_values = others[choice_others_keys]
                        group_name_dict[key_group_name].append(choice_others_keys)
                        del others[choice_others_keys]
                        break
    return group_name_dict

def verify():  # Vérification doublons
    validation = 0
    final_group = others_draw()
    for keys_final_group, values_final_group in final_group.items():
        i = 0
        comparison = []
        for i in range(len(final_group[keys_final_group])):
            for keys_full_list, values_full_list in full_list.items():
                if final_group[keys_final_group][i] == keys_full_list:
                    comparison.append(values_full_list)
        # Vérification si doublon par rapport au 1er projet dans les groupes
        list_duplicate = {x for x in comparison if comparison.count(x) > 1}
        if len(list_duplicate) == 0:
            validation += 1
        else:
            validation = 0
    return validation, final_group.keys(), final_group.values()


# Programme de sélection
validation = 0
while validation != 4:
    heads = {"Jacques" : "a", "Laure" : "b", "Noemie" : "a", "Felix" : "d"}
    others = {"Louis" : "c", "Jose" : "d", "Amelie" : "c", "Patrick" : "d", "Lucien" : "b", "Georges" : "b", "Anne" : "a", "Etienne" : "c", "Joachim" : "b", "Laurent" : "a"}
    full_list = {"Jacques" : "a", "Laure" : "b", "Noemie" : "a", "Felix" : "d", "Louis" : "c", "Jose" : "d", "Amelie" : "c", "Patrick" : "d", "Lucien" : "b", "Georges" : "b", "Anne" : "a", "Etienne" : "c", "Joachim" : "b", "Laurent" : "a"}
    verify_return = list(verify()[0:3])
    validation = verify_return[0]
# Affichage des résultats
final_group_keys = list(verify_return[1])
final_group_values = list(verify_return[2])
for i in range(len(final_group_keys)):
    print(final_group_keys[i] + " :")
    print(final_group_values[i])

exit()
