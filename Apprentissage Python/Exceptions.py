"""Dans ce fichier vous trouvez des exemples d'utilisations des exceptions
N'hesitez pas a vous exercer pour mieux comprendre comment on utilise cela"""

def bonjour(nombre):
    if(type(nombre) != type (int)):#On vérifie que le nombre est bien un entier
        if(nombre>0):#on verifie que le nombre est bien positif
            while nombre>0:
                print("Bonjour !")
                nombre -= 1 # c'est une autre manière d'écrire nombre = nombre - 1
        else:
            raise(ValueError) #On lève ici une exception si le nombre est négatif
    else:
        raise(TypeError)

if __name__ == '__main__':
    try:
        bonjour(-12)
    except:#On attrape ici toutes les exceptions levées par la fonciton bonjour
        print("veuillez entrer un nombre positif !")

    try:
        bonjour(int(input("Saissisez un nombre : ")))#On récupère l'entree de l'utilisateur et on le transforme en entier
    except ValueError:
        print("veuillez entrer un nombre positif !")
    except TypeError:
        print("Veuillez entrer un nombre !")

