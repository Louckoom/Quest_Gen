import random

for i in range(1, 11):
    globals()[f"niveau_{i}"] = i

difficulty_levels_beginner = niveau_1 , niveau_2 , niveau_3
difficulty_levels_intermediate = niveau_4 , niveau_5
difficulty_levels_advanced = niveau_6 , niveau_7
difficulty_levels_hard = niveau_8 , niveau_9 , niveau_10

niveau_1 = random.randint(2, 5)
niveau_2 = random.randint(2, 7)
niveau_3 = random.randint(4, 10)
niveau_4 = random.randint(1, 4)
niveau_5 = random.randint(2, 7)
niveau_6 = random.randint(1, 5)
niveau_7 = random.randint(2, 6)
niveau_8 = 1
niveau_9 = 2
niveau_10 = 3

mob_level_beginner = list(range(1,13))
mob_level_intermediate = list(range(13, 29))
mob_level_advanced = list(range(29, 57))
mob_level_hard = list(range(57, 82))


print(f"Level Beginner : {difficulty_levels_beginner}")
print(f"Level intermediate : {difficulty_levels_intermediate}")
print(f"Level advanced : {difficulty_levels_advanced}")
print(f"Level hard : {difficulty_levels_hard}")

classic_mobs = ["Slimes","Feu folets","Guèpes"]
advanced_mobs = ["Gobelins", "Loups","Bandits","Demon"]
mini_boss = ["Chef Gobelin","Mega-Loup","Tireur_Demon"]
boss = ["Roi Gobelin","Maitre Loup","Chef_Demon"]
mega_boss = ["Dieu_Demon"]

# ... (définition des niveaux de difficulté et des classic_mobs) ...

def generer_objectif(difficulte):
    if difficulte in difficulty_levels_beginner:
        nombre_ennemis = niveau_1 or niveau_2 or niveau_3
        level_mob = random.choice(mob_level_beginner)
        type_ennemi = random.choice(classic_mobs)
    
    elif difficulte in difficulty_levels_intermediate:
        nombre_ennemis = niveau_4 or niveau_5
        level_mob = random.choice(mob_level_intermediate) 
        type_ennemi = random.choice(advanced_mobs)

    elif difficulte in difficulty_levels_advanced:
        nombre_ennemis = niveau_6 or niveau_7
        level_mob = random.choice(mob_level_advanced)
        type_ennemi = random.choice(mini_boss)
    
    elif difficulte in difficulty_levels_hard:
        nombre_ennemis = niveau_8 or niveau_9 or niveau_10
        level_mob = random.choice(mob_level_hard)
        type_ennemi = random.choice(boss) or mega_boss
    else:
        return "Difficulté non reconnue."

    objectif = f"Éliminer {nombre_ennemis} {type_ennemi} de niveau {level_mob}"
    return objectif

# Choisir une difficulté au hasard
difficultes = [niveau_1, niveau_2, niveau_3, niveau_4, niveau_5, niveau_6, niveau_7, niveau_8, niveau_9, niveau_10]
difficulte_choisie = random.choice(difficultes)
print(difficulte_choisie)

# Générer l'objectif en fournissant la difficulté
objectif_final = generer_objectif(difficulte_choisie)  # Ajouter l'argument difficulte_choisie

# Afficher l'objectif
print(objectif_final)

# Créer le contenu HTML
contenu_html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Objectif de quête</title>
</head>
<body>
    <h1>Objectif de niveau : {difficulte_choisie}:</h1>
    <p>{objectif_final}</p>
</body>
</html>
"""

# Écrire le contenu dans le fichier HTML
with open("ProgQuest.html", "w", encoding="utf-8") as f:
    f.write(contenu_html)