"""
Dans ce fichier vous pourrez voir :
-un exemple de creation d'une classe
-l'utilisation des getters et setters avec la fonction property
-l'utilisation des variables globales
"""

class Equipement():
        """Classe Stockage va permettre de stocker les differentes informations du formulaire
        elle va contenir les attributs suivants :
        -un attribut global pour la liste des categories d'equipements
        -un attribut global pour la liste des salles
        -un attribut global pour la liste des centres de service
        -un attribut dictionnaire qui servira a stocker les differents informations des formulaires"""
        global listeCategorieEquipement
        listeCategorieEquipement= ["Categorie1", "Categorie2", "Categorie3"]
        global listeSalle
        listeSalle= ["Chambre patient", "Salle d'operation", "salle de reunion"]
        global listeCentreService
        listeCentreService= ["Centre de service 1", "Centre de service 2", "Centre de service 3"]
        global listeBonsDeTravail
        listeBonsDeTravail = ["Bon 1", "Bon 2", "Bon 3", "Bon 4", "Bon 5"]
        def __init__(self):  # Définition de la méthode de création d'un objet de la classe
            self._dictionnaire = dict()
            self.remplissage()
            self.ajoutListeMethodes()

        def _getDictionnaire(self):  # accesseur sur la variable _age
            return self._dictionnaire

        def _setDictionnaire(self, dict):  # mutateur sur la variabe _age
            self._dictionnaire = dict


        dictionnaire = property(_getDictionnaire, _setDictionnaire)


        def remplissage(self):
            self.dictionnaire["categorieEquipement"] = ""
            self.dictionnaire["marque"] = ""
            self.dictionnaire["modele"] = ""
            self.dictionnaire["numSerie"] = ""
            self.dictionnaire["salle"] = ""
            self.dictionnaire["centreService"] = ""
            self.dictionnaire["dateAcquisition"] = ""
            self.dictionnaire["dateEntretien"] = ""
            self.dictionnaire["provenance"] = ""
            self.dictionnaire["etatService"] = ""
            self.dictionnaire["etatConservation"] = ""
            self.dictionnaire["commentaire"] = ""

        def modifierCategorieEquipement(self, categorieEquipement):
            self.dictionnaire["categorieEquipement"] = categorieEquipement

        def modifierMarque(self, marque):
            self.dictionnaire["marque"] = marque

        def modifierModele(self, modele):
            self.dictionnaire["modele"] = modele

        def modifierNumSerie(self, numSerie):
            self.dictionnaire["numSerie"] = numSerie

        def modifierSalle(self, salle):
            self.dictionnaire["salle"] = salle

        def modifierCentreService(self, centreService):
            self.dictionnaire["centreService"] = centreService

        def modifierDateAcquisition(self, dateAcquisition):
            self.dictionnaire["dateAcquisition"] = dateAcquisition

        def modifierDateEntretien(self, dateEntretien):
            self.dictionnaire["dateEntretien"] = dateEntretien

        def modifierProvenance(self, provenance):
            self.dictionnaire["provenance"] = provenance

        def modifierEtatService(self, etatService):
            self.dictionnaire["etatService"] = etatService

        def modifierEtatConversation(self, etatConservation):
            self.dictionnaire["etatConservation"] = etatConservation

        def modifierCommentaire(self, commentaire):
            self.dictionnaire["commentaire"] = commentaire


        def ajoutListeMethodes(self):
            self.listeMethodes = list()
            self.listeMethodes.append(self.modifierCategorieEquipement)
            self.listeMethodes.append(self.modifierMarque)
            self.listeMethodes.append(self.modifierModele)
            self.listeMethodes.append(self.modifierNumSerie)
            self.listeMethodes.append(self.modifierSalle)
            self.listeMethodes.append(self.modifierCentreService)
            self.listeMethodes.append(self.modifierDateAcquisition)
            self.listeMethodes.append(self.modifierDateEntretien)
            self.listeMethodes.append(self.modifierEtatService)
            self.listeMethodes.append(self.modifierEtatConversation)
            self.listeMethodes.append(self.modifierEtatService)
            self.listeMethodes.append(self.modifierEtatConversation)
            self.listeMethodes.append(self.modifierCommentaire)


class BonDeTravail():
    """Classe Stockage va permettre de stocker les differentes informations du formulaire
    elle va contenir les attributs suivants :
    -un attribut global pour la liste des categories d'equipements
    -un attribut global pour la liste des salles
    -un attribut global pour la liste des centres de service
    -un attribut dictionnaire qui servira a stocker les differents informations des formulaires"""

    def __init__(self):  # Définition de la méthode de création d'un objet de la classe
        self._dictionnaire = dict()
        self.remplissage()
        self.ajoutListeMethodes()

    def __init__(self):  # Définition de la méthode de création d'un objet de la classe
        self._dictionnaire = dict()
        self.ajoutListeMethodes()

    def _getDictionnaire(self):  # accesseur sur la variable _age
        return self._dictionnaire

    def _setDictionnaire(self, dict):  # mutateur sur la variabe _age
        self._dictionnaire = dict

    dictionnaire = property(_getDictionnaire, _setDictionnaire)

    def remplissage(self, equipement):
        self.dictionnaire["idEquipement"] = equipement.dictionnaire["idEquipement"]
        self.dictionnaire["categorieEquipement"] = equipement.dictionnaire["categorieEqipement"]
        self.dictionnaire["marque"] = equipement.dictionnaire["marque"]
        self.dictionnaire["modele"] = equipement.dictionnaire["modele"]
        self.dictionnaire["salle"] = equipement.dictionnaire["salle"]
        self.dictionnaire["centreService"] = equipement.dictionnaire["centreService"]
        self.dictionnaire["numeroBonDeTravail"] = ""
        self.dictionnaire["DescriptionSituation"] = ""
        self.dictionnaire["date"] = ""
        self.dictionnaire["tempsEstime"] = ""
        self.dictionnaire["descriptionInventaire"] = ""
        self.dictionnaire["etat"] = ""

    def modifierCategorieEquipement(self, categorieEquipement):
        self.dictionnaire["categorieEquipement"] = categorieEquipement

    def modifierMarque(self, marque):
        self.dictionnaire["marque"] = marque

    def modifierModele(self, modele):
        self.dictionnaire["modele"] = modele

    def modifierSalle(self, salle):
        self.dictionnaire["salle"] = salle

    def modifierCentreService(self, centreService):
        self.dictionnaire["centreService"] = centreService

    def modifierNumeroBonDeTravail(self, numeroBonDeTravail):
        self.dictionnaire["numeroBonDeTravail"] = numeroBonDeTravail

    def modifierDescriptionSituation(self, descriptionSituation):
        self.dictionnaire["DescriptionSituation"] = descriptionSituation

    def modifierDate(self, date):
        self.dictionnaire["date"] = date

    def modifierTempsEstime(self, tempsEstime):
        self.dictionnaire["tempsEstime"] = tempsEstime

    def modifierDescriptionInventaire(self, descriptionInventaire):
        self.dictionnaire["descriptionInventaire"] = descriptionInventaire

    def modifierEtat(self, etat):
        self.dictionnaire["etat"] = etat

    def ajoutListeMethodes(self):
        self.listeMethodes = list()
        # self.listeMethodes.append(self.modifierIdEquipement)
        # self.listeMethodes.append(self.modifierCategorieEquipement)
        # self.listeMethodes.append(self.modifierMarque)
        # self.listeMethodes.append(self.modifierModele)
        # self.listeMethodes.append(self.modifierSalle)
        # self.listeMethodes.append(self.modifierCentreService)
        self.listeMethodes.append(self.modifierNumeroBonDeTravail)
        self.listeMethodes.append(self.modifierDescriptionSituation)
        self.listeMethodes.append(self.modifierDate)
        self.listeMethodes.append(self.modifierTempsEstime)
        self.listeMethodes.append(self.modifierDescriptionInventaire)
        self.listeMethodes.append(self.modifierEtat)

def listeCle(dictionnaire) :
    cles = list()
    for key in dictionnaire:
        cles.append(key)
    return cles