import Personne

personne1 = Personne.Personne("Dupont", age=20)
personne2 = Personne.Personne("Dupoint", prenom="James")

agentSpecial = Personne.AgentSpecial("Bond", "Pistolet")

personne1.nom = "Patrick"
personne1._setNom("Patrick")

V = [1, 54, 30]

for i in V[0:2]:
    print(i)

print(V[-1])

D = dict()
D = {}

D["Prof"] = 10;
D["Etudiant"] = 200
D["Personnel"] = 30

print(D)