"""Fichier montrant quelques exemples sur la manipulation de classe"""

import Personne #exemple d'importation d'une classe que nous avons créé

#On crée des objets qui sont des instanciations de la classe personne
personne1 = Personne.Personne("Dupont", age=20) #Les valeurs non obligatoires peuvent être initialisé en leur assignant une valeur
personne2 = Personne.Personne("Dupoint", prenom="James")

agentSpecial = Personne.AgentSpecial("Bond", "Pistolet")

personne1.nom = "Patrick"

V = [1, 54, 30]# Exemple de création d'une liste

#Exemple d'utilisation de la boucle for pour une liste
for i in V[0:2]:
    print(i)
liste = list()
#ajout d'élément dans la liste
liste.append(12)
liste.append("Bonjour")
#Affichage du dernier élément de la liste V
print(V[-1])


#Exemple de création d'un dictionnaire
D = dict()
D = {}

D["Prof"] = 10;
D["Etudiant"] = 200
D["Personnel"] = 30

print(D)