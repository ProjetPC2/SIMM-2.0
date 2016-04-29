
























class Personne:
    def __init__(self, nom, prenom="Martin", age=1):
        self._nom = nom
        self._prenom = prenom
        self._age = age

    def __str__(self):
        return "Nom: {0}, Prenom: {1}, Age: {2}".format(self._nom, self._prenom, self._age)
    
    def getNom(self):
        return self._nom

    def setNom(self, nouveauNom):
        self._nom = nouveauNom

    def getAge(self):
        return self._age

    def setAge(self, nouvelAge):
        if (nouvelAge > 0):
            self._age = nouvelAge

    age = property(getAge, setAge)

    variableDeClasse = "Humain"

class AgentSpecial(Personne):
    def __init__(self, nom, arme):
        Personne.__init__(self, nom)
        self._arme = arme
        
    def __str__(self):
        return "Nom : {0}, Prenom : {1}, Age : {2}, Arme : {3}".format(self._nom, self._prenom, self._age, self._arme)