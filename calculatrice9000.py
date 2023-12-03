historique = []
# La fonction pour les calculs
def calculatrice():
    try:
        num1 = float(input("Saisir votre premier nombre : "))
        operator = input("Saisir votre operation (+,-,*,/,%) : ")
        num2 = float(input("Saisir votre deuxieme nombre : "))
    except ValueError:
        print("Les nombre que vous avez saisi ne sont pas corrects")
        return None
       
    if operator == "+":
        resultat = num1 + num2   
    
    elif operator == "-":
        resultat = num1 - num2
    
    elif operator == "*":
        resultat = num1 * num2

    elif operator == "/":
        
        if num1 == 0 or num2 == 0:
            print("Ce n'est pas possible de diviser par zero")
            return None
        resultat = num1 / num2 

    elif operator == "%":
        
        if num1 == 0 or num2 == 0:
            print("Ce n'est pas possible de diviser par zero")
            return None
        resultat = num1 % num2 
    
    else:
        print("Votre operation n'est pas pris en compte")
        return None 
#Pour recuperer les input et les rentrer dans la liste
    historique.append((num1, operator, num2, resultat))
    return resultat

resultat = calculatrice()
if resultat is not None:
    print("\nle resultat du calcule est ", resultat)
        
# La deuxieme fonction pour afficher un historique

def afficher_historique():
    print("\nHistorique des calculs:")
    for i, (num1, operator, num2, resultat) in enumerate(historique, start=1):
        print(f"{i}. {num1} {operator} {num2} = {resultat}")
    print()

histo = input("\nSaisir 'oui' pour voir l'historique : ")
if histo == "oui":
    afficher_historique()

def effacer_historique():
    historique.clear()
    print("L'historique a été effacé.")

effacer = input("\nSaisir 'oui' pour effacer l'historique : ")
if effacer == "oui":
    effacer_historique()
