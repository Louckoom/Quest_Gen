def quest_result():
    quest = input("Voulez-vous infliger des dégats? (oui/non): ")
    if quest.lower() == "oui":
        quest_result = True
        print('Quest Accomplished')
        print(quest_result)

    elif quest.lower() == "non":
        quest_result = False
        print('Quest Failed')
        print(quest_result)

    else:
        print(f"Vous avez décider de répondre par autre chose que 'oui' ou 'non' donc vous avez échoué la quêtes, s'il y a des régles c'est pour les respecter !")
        quest_result = False
        print('Quest Failed')
        print(quest_result)

quest_result()