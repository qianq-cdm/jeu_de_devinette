"""
TP1 - Jeu de devinette
Par: Qian Qian
Groupe: 407
Ce programme est un jeu de devinette et le joueur peut choisir des bornes en premier
"""

import random


def choisir_borne():
    """
    fonction pour le choix des bornes
    """
    global borne_minimale, borne_maximale
    # entrer borne minimal (défaut 0)
    borne_minimale = int(input("Entrez le borne minimale que vous voulez... ") or 0)
    # entrer borne maximale (défaut 100)
    borne_maximale = int(input("Entrez le borne maximale que vous voulez... ") or 100)


# boucle de si on joue
while True:
    # demander à joueur de choisir les bornes
    choisir_borne()

    # générer un nombre aléatoire
    random_number = random.randint(borne_minimale, borne_maximale)
    print(f"J'ai choisi un nombre au hasard entre {borne_minimale} et {borne_maximale}.\nÀ vous de le deviner...")

    # compteur de nombre d'essai
    nombre_essai = 0

    # boucle d'entrer les essais
    while True:
        # demander le joueur de essayer
        essai = int(input("Entrez votre essai :"))
        # ajouter le nombre d'essai
        nombre_essai += 1
        if random_number < essai:
            # c'est trop petit
            print(f"Mauvais choix, le nombre est plus petit que {essai}")
            # essayer à nouveau
            continue
        elif random_number > essai:
            # c'est ttop grand
            print(f"Mauvaise réponse, le nombre est plus grand que {essai}")
            # essayer à nouveau
            continue
        else:
            # bonne réponse
            print(f"Bravo! Bonne réponse\nVous avez réussi en : {nombre_essai} essai(s).")
            # arrêter les essaies
            break

    # demander si le joueur veut encore jouer
    nouvelle_partie = input("Voulez-vous faire une autre partie (o/n)?")
    if not (nouvelle_partie.lower() == "o"):
        # réponse n'est pas "oui", on arrête
        break

print("Merci et au revoir…")
