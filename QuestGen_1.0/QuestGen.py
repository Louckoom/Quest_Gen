import random

objectif_combat = ["tuer 4 feu follets","vaincre 10 gobelins","exterminer 20 slimes"]
donneurs_quetes_combat = ["Le chef du village", "Un guerrier blessé", "La guilde des aventuriers"]
lieu_quete_combat = ["au Donjon de Stoleis", "à la Grotte de la montagne","dans le Marais enchanté"]
recompenses_combat = ["100 pièces d'or", "Une épée en acier", "Un bouclier renforcé"]

objectif_exploration = ["trouver un artefact","chercher la fleur noire","retrouver le casque magique"]
donneurs_quetes_exploration = ["Un vieux sage", "Un cartographe royal", "Un marchand d'objets rares"]
lieu_quete_exploration = ["dans la Forêt de Stoleis", "autour du Jardin du chateaux","dans les profondeurs du Marais enchanté"]
recompenses_exploration = ["Une carte au trésor", "Un artefact ancien", "Des informations secrètes"]

objectif_social = ["Ramener le renard blanc à son propriétaire","Aider à couper des légumes","Porter les sacs de minerais"]

objectif_collecte =["Récolter 12 lapis lazuli","Couper 6 arbres","Récolter 20 épis de blé"]

objectif_artisanat = ["Forger une épée","Taner 4 cuire","Faire fondre un minerai de fer"]




modeles_quetes_combat = ["[donneur_quete] vous donne l'objectif de [objectif] se trouvant [lieu_quete], Récompense : [recompense]."]
modeles_quetes_exploration = ["[donneur_quete] vous annonce que votre but est de [objectif], rendez vous [lieu_quete], Récompense : [recompense]."]

categories = ["Combat","Exploration"]
categorie_choisie = random.choice(categories)

if categorie_choisie == "Combat":
    objectif = random.choice(objectif_combat)
    donneur_quete = random.choice(donneurs_quetes_combat)
    lieu_quete = random.choice(lieu_quete_combat)
    recompense = random.choice(recompenses_combat)
    modele_choisi = random.choice(modeles_quetes_combat)

elif categorie_choisie == "Exploration":
    objectif = random.choice(objectif_exploration)
    donneur_quete = random.choice(donneurs_quetes_exploration)
    lieu_quete = random.choice(lieu_quete_exploration)
    recompense = random.choice(recompenses_exploration)
    modele_choisi = random.choice(modeles_quetes_exploration)


description_quete = modele_choisi.replace("[objectif]", objectif) \
                                 .replace("[lieu_quete]", lieu_quete) \
                                 .replace("[donneur_quete]", donneur_quete) \
                                 .replace("[recompense]", recompense)

print(description_quete)

# Générer le contenu HTML
contenu_html = f"""
<!DOCTYPE html>
<html>
<head>
  <title>Générateur de Quête</title>
</head>
<body>
  <h1>Quête du jour</h1>
  <div id="quete">
    {description_quete} 
  </div>
</body>
</html>
"""

# Écrire dans le fichier HTML
with open("QuestGen_1.html", "w", encoding="utf-8") as f:
  f.write(contenu_html)