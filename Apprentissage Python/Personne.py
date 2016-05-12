""" Voici un exemple de création d'une classe et de l'héritage"""

class Personne:
    """Classe Personne qui représentera une personne par son nom, prenom et age"""
    def __init__(self, nom, prenom="Martin", age=1):#Définition de la méthode de création d'un objet de la classe
        self._nom = nom
        self._prenom = prenom
        self._age = age

    def __str__(self):#Méthode permettant l'affichage des informations de la classe par la fonction print
        return "Nom: {0}, Prenom: {1}, Age: {2}".format(self._nom, self._prenom, self.age)

    def _getAge(self):#accesseur sur la variable _age
        return self._age

    def _setAge(self, newAge):#mutateur sur la variabe _age
        if newAge > 0:
            self._age = newAge

    age = property(_getAge, _setAge)#Exemple de l'utilisation de la fonction property


class AgentSpecial(Personne):
    """Agent Special est une classe héritant de Personne
    C'est une personne qui possede une arme"""
    def __init__(self, nom, arme):
        Personne.__init__(self, nom)
        self._arme = arme

    def __str__(self):
        return "Nom: {0}, Prenom: {1}, Age: {2}, Arme: {3}".format(self._nom, self._prenom, self.age, self._arme)