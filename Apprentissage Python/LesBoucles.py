"""Dans ce fichier vous trouvez des exemples d'utilisations des boucles
N'hesitez pas a vous exercer pour mieux comprendre comment on utilise cela"""

def Bonjour(nombre):
    """Cette fonction va servir à afficher la valeur absolu de nombre fois le mot bonjour
        elle va prendre en paramètre un nombre qui indiquer le nombre d'affichage (int)"""
    if nombre<0: #on va dist
        while nombre < 0:
            nombre = nombre + 1
            print("Bonjour !")
    else:
        while nombre > 0:
            nombre = nombre - 1
            print("Bonjour !!")

#Pour l'utilisation de la boucle for, vous aurez un exemple dans le fichier Liste
#Pour l'utilisation des mots-cles break et continue, je vous laisse vous amusez avec ^^


if __name__ == '__main__':
    Bonjour(12)
    Bonjour(-3)