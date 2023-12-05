from datetime import datetime

heure_actuelle = datetime.now().time()


def est_palindrome(chaine):
    chaine = chaine.lower()
    return chaine == chaine[::-1]


print("Quelle est votre langue?")
print("a. Anglais")
print("b. Français")

choix_utilisateur = ''

while choix_utilisateur.lower() not in ['a', 'b']:

    choix_utilisateur = input("Votre choix (a ou b) : ")

    if choix_utilisateur.lower() == 'a':
        if 4 <= heure_actuelle.hour < 12:
            partie_journee = "good morning"
        elif 12 <= heure_actuelle.hour < 18:
            partie_journee = "Hello!"
        else:
            partie_journee = "Good evening"

    elif choix_utilisateur.lower() == 'b':

        if 4 <= heure_actuelle.hour < 12:
            partie_journee = "Bon matin"
        elif 12 <= heure_actuelle.hour < 18:
            partie_journee = "Bonjour"
        else:
            partie_journee = "Bonsoir"

    else:
        print("Choix invalide. Veuillez sélectionner a ou b.")

print(f"{partie_journee}")

while True:

    entree_utilisateur = input("Saisissez du texte (ou 'exit' pour quitter) : ")

    if entree_utilisateur.lower() == 'exit':
        if choix_utilisateur.lower() == 'a':
            if 4 <= heure_actuelle.hour < 12:
                partie_journee = "Bye"
            elif 12 <= heure_actuelle.hour < 18:
                partie_journee = "Goodbye!"
            else:
                partie_journee = "Have a good evening"

        elif choix_utilisateur.lower() == 'b':

            if 4 <= heure_actuelle.hour < 12:
                partie_journee = "Bonne matinée"
            elif 12 <= heure_actuelle.hour < 18:
                partie_journee = "bonne journée"
            else:
                partie_journee = "bonne soiré"

        print(f"{partie_journee}")
        break

    texte_en_miroir = entree_utilisateur[::-1]
    print(f"{texte_en_miroir}")

    # Vérifier si la saisie est un palindrome
    if est_palindrome(entree_utilisateur):
        print("Bien dit!")
