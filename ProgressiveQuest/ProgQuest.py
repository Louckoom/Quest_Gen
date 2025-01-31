import random

import random

# Paramètres de la difficulté
niveau_base = 2
facteur_croissance = 1.5
nombre_de_niveaux = 50

# Génération des niveaux de difficulté
niveaux_difficulte = {
    i: int(niveau_base * facteur_croissance**(i - 1))
    for i in range(1, nombre_de_niveaux + 1)
}

# Niveaux de monstres
niveaux_monstres = {
    "beginner": list(range(1, 13)),
    "intermediate": list(range(13, 21)),
    "advanced": list(range(21, 43)),
    "hard": list(range(43, 51)),
}

# Types d'ennemis
types_ennemis = {
    "beginner": ["Slimes", "Feu folets", "Guêpes"],
    "intermediate": ["Gobelins", "Loups", "Bandits", "Demon"],
    "advanced": ["Chef Gobelin", "Mega-Loup", "Tireur_Demon"],
    "hard": ["Roi Gobelin", "Maitre Loup", "Chef_Demon", "Dieu_Demon"],
}

def generer_objectif():
    niveau = random.randint(1, nombre_de_niveaux)
    difficulte = niveaux_difficulte[niveau]

    if niveau <= 10:
        niveau_monstre = "beginner"
    elif niveau <= 20:
        niveau_monstre = "intermediate"
    elif niveau <= 30: # Ajout d'une condition pour les niveaux advanced
        niveau_monstre = "advanced"
    else:
        niveau_monstre = "hard"

    nombre_ennemis = random.randint(1, 10)  # Ajuster les plages si nécessaire
    level_mob = random.choice(niveaux_monstres[niveau_monstre])
    type_ennemi = random.choice(types_ennemis[niveau_monstre])

    objectif = f"Éliminer {nombre_ennemis} {type_ennemi} de niveau {level_mob}."
    return objectif , niveau_monstre

# Génération et affichage de l'objectif
objectif_final, niveau_monstre = generer_objectif()
print(objectif_final, niveau_monstre)

# ... (génération de l'objectif)

# Création du contenu HTML
contenu_html = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ProgQuest - Objectif de Quête</title>
    <style>
        body {{
            font-family: sans-serif;
            margin: 20px;
            background-color: #f0f0f0;
        }}
        h1 {{
            color: #333;
        }}
        p {{
            font-size: 1.2em;
        }}
    </style>
</head>
<body>
    <h1>Objectif de niveau : {niveau_monstre}</h1>
    <p>{objectif_final}</p>
</body>
</html>
"""

# Écriture du contenu dans le fichier HTML
try:
    with open("ProgQuest.html", "w", encoding="utf-8") as f:
        f.write(contenu_html)
    print("Fichier ProgQuest.html créé avec succès.")
except Exception as e:
    print(f"Erreur lors de la création du fichier HTML : {e}")