objectif = "Trouver un renard blanc et le ramener à sa propriétaire"
donneur_quete = "Boulangère du village"
lieu_depart = "Village de Stoleis"
lieu_arrivee = "Forêt des cyprès"
animal = "renard blanc"  # On précise que l'objet de la quête est un animal
obstacle = "2 Feu follets de la forêt"
recompense = "5 écus d'argent, " + " et une baguette de pain"

description_quete = f"Bonjour l'objectif de la quête est de : {objectif}, \
Vous vous situez actuellement au {lieu_depart}, et vous devez aller à la {lieu_arrivee} \
afin de retrouver le {animal}. \
Attention, sur votre chemin vous croiserez {obstacle}, il vous faudra les vaincre avant de retrouver le {animal}.\
Votre récompense sera {recompense}. \
Quête donnée par la {donneur_quete}."

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