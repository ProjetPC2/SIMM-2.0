"""Dans ce fichier vous trouvez des exemples d'utilisations des structures conditionnelles
N'hesitez pas a vous exercer pour mieux comprendre comment on utilise cela"""


maVariable = 1 #On déclare une variable qui est un entier (int)
maVariableReel = 1.1 #On déclare une variable qui est un réel (float)
maVariableText = "Bonjour" #On crée ici une variable qui contient un texte
maVariableText1 = 'Bonjour' #Une autre méthode pour déclarer une varaible qui contient du texte

if maVariable >= 1 :
    print("maVariable est supérieur à 1")

if maVariable <= 1:
    print("maVariable est inférieur à 1")
else:
    print("maVariable est strictement supérieur à 1")

if maVariable < 1:
    print("maVariable est strictement inférieur à 1")
elif maVariable == 1: #Pour savoir si c'est égale faites bien attention à utiliser == et non =
    print("maVariable est égale à 1")
else:
    print("maVariable est strictement supérieur à 1")

if maVariable == 1 and maVariableReel>1:
    print("La condition précédente est bien vérifiée")

#Exemple d'utilisation des conditions dans une fonction

def positivite(nombre):
    if nombre > 0:
        print("Le nombre ", nombre, " est bien positif")
    elif nombre == 0:
        print("Le nombre ", nombre, " est nul")
    else:
        print("Le nombre ", nombre, " est négatif")

positivite(maVariable)
positivite(maVariableReel)
positivite(0)
positivite(-25)
positivite(-1.2)

