""" Vous pouvez trouvez ici quelques exemples d'utilisation des variables
et des fonctions"""

#Les variables
maVariable = 1 #On déclare une variable qui est un entier (int)
maVariableReel = 1.1 #On déclare une variable qui est un réel (float)
maVariableText = "Bonjour" #On crée ici une variable qui contient un texte
maVariableText1 = 'Bonjour' #Une autre méthode pour déclarer une varaible qui contient du texte
#L'interet de changer la manière de déclarer votre texte va être selon que vous ayez besoin d'un guillemet
#ou d'une apostrophe dans votre code

#Les fonctions

def fonction(nom = "PC2"):
    """Cette fonction va servir à afficher le nom qui est entré
        elle va prendre en paramètre un nom (str)"""
    print ("Bonjour ", nom, " !") #Pour afficher du texte et des variables on les sépares par des virgules

def salut(nom, prenom):
    """la fonction salut va servir à afficher le nom et le prenom qui sont entrés
        elle va prendre en paramètre un nom (str) et un prenom"""
    print ("hey salut ", prenom, " ", nom, " !") #Pour afficher du texte et des variables on les sépares par des virgules

exempleFonctionLambda = lambda x : x*x; #exemple d'une fonction lambda qui nous donne le carre d'un nombre

def carre(valeur):
    """la fonction carre renvoie le carre de la valeur """
    return valeur * valeur

if __name__ == '__main__': #cette condition permet de lancer l'application que dans le cas où c'est le fichier principal
    maVariable
    maVariableReel
    maVariableText
    maVariableText1
    print("Affichage du type de maVariable", type(maVariable))
    fonction()
    fonction("Jarome")
    salut("iron", "man")
    print("Exemple d'utilisation de la fonction lambda avec la variable ", maVariable,
          "la valeur de retour est : ", exempleFonctionLambda(maVariable))
    print("Exemple d'utilisation de la fonction lambda avec la variable ", maVariable,
          "la valeur de retour est : ", exempleFonctionLambda(maVariableReel))
    variableEntree = input("Veuillez Entrer un nombre") #Saissez une valeur dans la partie Run de votre programme
    print("Affichage de variableEntree : ", variableEntree)