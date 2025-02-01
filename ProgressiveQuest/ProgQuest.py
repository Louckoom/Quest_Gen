import random

# Paramètres de la difficulté
niveau_base = 2
facteur_croissance = 1.5
nombre_de_niveaux = 50

# Génération des niveaux de difficulté (dictionnaire pour un accès plus rapide)
niveaux_difficulte = {
    i: int(niveau_base * facteur_croissance**(i - 1))
    for i in range(1, nombre_de_niveaux + 1)
}

# Niveaux de monstres (dictionnaire pour une meilleure organisation)
niveaux_monstres = {
    "beginner": list(range(1, 7)),
    "intermediate": list(range(7, 21)),
    "advanced": list(range(21, 43)),
    "hard": list(range(43, 51)),
}

# Types d'ennemis (dictionnaire pour une meilleure organisation)
types_ennemis = {
    "beginner": ["Slimes", "Feu folets", "Guêpes"],
    "intermediate": ["Gobelins", "Loups", "Bandits", "Demon"],
    "advanced": ["Chef Gobelin", "Mega-Loup", "Tireur_Demon"],
    "hard": ["Roi Gobelin", "Maitre Loup", "Chef_Demon", "Dieu_Demon"],
}

def choisir_niveau_monstre(niveau_joueur):
    """Détermine le niveau de monstre en fonction du niveau du joueur."""
    if niveau_joueur <= 10:
        return "beginner"
    elif niveau_joueur <= 20:
        return "intermediate"
    elif niveau_joueur <= 30:
        return "advanced"
    else:
        return "hard"

def generer_objectif(niveau_joueur):
    """Génère un objectif de quête en fonction du niveau du joueur."""
    niveau_monstre = choisir_niveau_monstre(niveau_joueur)
    nombre_ennemis = random.randint(2, 10)  # Ajuster les plages si nécessaire
    level_mob = random.choice(niveaux_monstres[niveau_monstre])
    type_ennemi = random.choice(types_ennemis[niveau_monstre])
    return f"Éliminer {nombre_ennemis} {type_ennemi} de niveau {level_mob}."

def creer_html(objectif, niveau, reponse=""):
    """Crée le contenu HTML pour l'objectif et la réponse."""
    return f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>ProgQuest 1.0</title>
    </head>
    <body>
        <h1>ProgQuest 1.0</h1>
        <p>Niveau {niveau} : {objectif}</p>
        <p>Voulez-vous continuer ?</p>
        <p>Réponse précédente : {reponse}</p>
    </body>
    </html>
    """

def progression_circulaire(niveau_joueur_actuel, niveau_joueur_max):
    """Gère la progression circulaire des niveaux et l'interaction avec l'utilisateur."""
    reponse_precedente = "" # Initialisation de la réponse précédente
    while True:
        objectif = generer_objectif(niveau_joueur_actuel)
        html = creer_html(objectif, niveau_joueur_actuel, reponse_precedente)

        with open("ProgQuest.html", "w", encoding="utf-8") as f:
            f.write(html)
        
        reponse = input("Voulez-vous continuer? (oui/non): ")

        # Afficher la réponse dans le HTML avant de passer au niveau suivant
        html = creer_html(objectif, niveau_joueur_actuel, reponse)
        with open("ProgQuest.html", "w", encoding="utf-8") as f:
            f.write(html)
        
        if reponse.lower() != "oui":
            html_fin = """
            <!DOCTYPE html>
            <html lang="fr">
            <head>
                <meta charset="UTF-8">
                <title>ProgQuest 1.0</title>
            </head>
            <body>
                <h1>ProgQuest 1.0</h1>
                <p>Vous avez décidé de ne plus accepter de quêtes. Relancez le programme pour recommencer du début.</p>
            </body>
            </html>
            """
            with open("ProgQuest_1_0.html", "w", encoding="utf-8") as f:
                f.write(html_fin)
            return  # Ajout de return pour arrêter la fonction ici
        
        # Mise à jour de la réponse précédente pour la prochaine itération
        reponse_precedente = reponse

        niveau_joueur_actuel += 1
        if niveau_joueur_actuel > niveau_joueur_max:
            niveau_joueur_actuel = 1

# Niveau initial du joueur
niveau_joueur_actuel = 1

# Lancement de la progression
progression_circulaire(niveau_joueur_actuel, 10)