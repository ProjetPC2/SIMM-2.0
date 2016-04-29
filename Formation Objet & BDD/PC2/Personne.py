class Personne:
    def __init__(self, nom, prenom="Martin", age=1):
        self._nom = nom
        self._prenom = prenom
        self._age = age

    def __str__(self):
        return "Nom: {0}, Prenom: {1}, Age: {2}".format(self._nom, self._prenom, self.age)

    def _getAge(self):
        return self._age

    def _setAge(self, newAge):
        if newAge > 0:
            self._age = newAge

    age = property(_getAge, _setAge)


class AgentSpecial(Personne):
    def __init__(self, nom, arme):
        Personne.__init__(self, nom)
        self._arme = arme

    def __str__(self):
        return "Nom: {0}, Prenom: {1}, Age: {2}, Arme: {3}".format(self._nom, self._prenom, self.age, self._arme)