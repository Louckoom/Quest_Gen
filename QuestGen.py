import random

objectif_combat = ["Tuer 4 feu follets","Vaincre 10 gobelins","Exterminer 20 slimes"]
objectif_exploration = ["Trouver un artefact","Chercher la fleur noire","Retrouver la courrone du roi"]
objectif_social = ["Ramener le renard blanc à son propriétaire","Aider à couper des légumes","Porter les sacs de minerais"]
objectif_collecte =["Récolter 12 lapis lazuli","Couper 6 arbres","Récolter 20 épis de blé"]
objectif_artisanat = ["Forger une épée","Taner 4 cuire","Faire fondre un minerai de fer"]

modeles_quetes_combat = ["L'objectif de cette mission est de [objectif]","Afin de rassurer le village il vous ai demandé de [objectif]"]
modeles_quetes_exploration = ["Votre but est de [objectif]","On vous a demander de [objectif]"]

categories = ["Combat","Exploration"]
categorie_choisie = random.choice(categories)

if categorie_choisie == "Combat":
    objectif = random.choice(objectif_combat)
    modele_choisi = random.choice(modeles_quetes_combat)

elif categorie_choisie == "Exploration":
    objectif = random.choice(objectif_exploration)
    modele_choisi = random.choice(modeles_quetes_exploration)


description_quete = modele_choisi.replace("[objectif]", objectif)

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
with open("index.html", "w", encoding="utf-8") as f:
  f.write(contenu_html)