
def give_the_bill():
    # Le bloc try permet d'éviter que le programme plante si l'utilisateur entre autre chose qu'un chiffre.
    # Si une erreur de type ValueError se produit lors de la conversion, le except affiche un message d'erreur personnalisé.
    try:
            language=int(input("1.français 2.english"))
            if language == 1 :
                give_the_bill_fr()
            elif language==2:
                give_the_bill_en()
            else:
                print("please choose a valid option, merci de choisir une option valide ") 
                give_the_bill()               
    except ValueError:
        print("just a number , juste un chiffre")

def give_the_bill_fr():
        print("Bienvenu au calculateur de pourboire !")
        while True :
            try:
                bill=float(input("Quelle était la facture Totale ? € \n"))  # Génère un prompt et attend un chiffre (float)
                tip=int(input("Quel pourcentage de pourboire voudriez vous donner ? 10, 12, or 15? \n "))  # Génère un prompt et attend un chiffre (int)
                bill_split=int(input("Combien de personne pour payer la facture ? \n"))  # Génère un prompt et attend un chiffre (int)
                tip_percentage=tip/100  # Calcule le pourcentage de pourboire choisi
                tip_amount=bill*tip_percentage  # Calcule le montant du pourboire
                total_bill_with_tip=tip_amount+bill  # Additionne le pourboire à la facture totale
                total_bill_per_person=total_bill_with_tip/bill_split  # Divise le total par le nombre de personnes
                print(f"Chaque personne devra payer :€{round(total_bill_per_person,2) }")  # Affiche le montant à payer par personne
                break
            except ValueError:
                print("Nous acceptons que des chiffres, mais bien essayé :) si vous avez rajouter une virgule merci de la remplacer par un point !")  # Message d'erreur si l'utilisateur n'entre pas un chiffre


def give_the_bill_en():
    print("Welcome to the tip calculator!")
    while True :
        try:
            bill=float(input("What was the total bill? $ \n"))  # Génère un prompt et attend un chiffre (float)
            tip=int(input("What percentage tip would you like to give? 10, 12, or 15? \n "))  # Génère un prompt et attend un chiffre (int)
            bill_split=int(input("how many people to split the bill ? \n"))  # Génère un prompt et attend un chiffre (int)
            tip_percentage=tip/100  # Calcule le pourcentage de pourboire choisi
            tip_amount=bill*tip_percentage  # Calcule le montant du pourboire
            total_bill_with_tip=tip_amount+bill  # Additionne le pourboire à la facture totale
            total_bill_per_person=total_bill_with_tip/bill_split  # Divise le total par le nombre de personnes
            print(f"each person should pay:${round(total_bill_per_person,2) }")  # Affiche le montant à payer par personne
            break
        except ValueError:
            print("accept just number, but nice try :) if you added a comma please replace it with a dot!")  # Message d'erreur si l'utilisateur n'entre pas un chiffre

give_the_bill() #fais appel a la fonction pour lancer le programme

