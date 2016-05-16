import datetime
from tinydb import *
from yamlStorage import YAMLStorage




class Equipement:

    ETAT_SERVICE =['En service', 'En maintenance', 'Au rebut']
    ETAT_CONSERVATION = ['Quasi neuf', 'Acceptable', 'En fin de vie', 'Désuet']

    def __init__(self, id, categorie_equipement, marque, modele, numero_serie, salle, centre_de_service,
                 date_acquisition, date_dernier_entretien, provenance, etat_service, etat_conservation,
                 commentaires):
        self._id = id
        self._categorie_equipement = categorie_equipement
        self._marque = marque
        self._modele = modele
        self._numero_serie = numero_serie
        self._salle = salle
        self._centre_de_service = centre_de_service
        self._date_acquisition = date_acquisition
        self._date_dernier_entretien = date_dernier_entretien
        self._provenance = provenance
        self._etat_service = etat_service
        self._etat_conservation = etat_conservation
        self._commentaires = commentaires

    # getters et setters pour id
    def get_id(self):
        return self._id

    def set_id(self, new_id):
        self._id = new_id

    id = property(get_id, set_id)

    # getters et setters pour categorie_equipement
    def get_categorie_equipement(self):
        return self._categorie_equipement

    def set_categorie_equipement(self, new_categorie_equipement):
        self._categorie_equipement = new_categorie_equipement

    categorie_equipement = property(get_categorie_equipement, set_categorie_equipement)

    # getters et setters pour marque
    def get_marque(self):
        return self._marque

    def set_marque(self, new_marque):
        self._marque = new_marque

    marque = property(get_marque, set_marque)

    # getters et setters pour modele
    def get_modele(self):
        return self._modele

    def set_modele(self, new_modele):
        self._modele = new_modele

    modele = property(get_modele, set_modele)

    # getters et setters pour numero_serie
    def get_numero_serie(self):
        return self._numero_serie

    def set_numero_serie(self, new_numero_serie):
        self._numero_serie = new_numero_serie

    numero_serie = property(get_numero_serie, set_numero_serie)

    # getters et setters pour salle
    def get_salle(self):
        return self._salle

    def set_salle(self, new_salle):
        self._salle = new_salle

    salle = property(get_salle, set_salle)

    # setters et getters pour centre_de_service
    def get_centre_de_service(self):
        return self._centre_de_service

    def set_centre_de_service(self, new_centre_de_service):
        self._centre_de_service = new_centre_de_service

    centre_de_service = property(get_centre_de_service, set_centre_de_service)

    # getters et setters pour date_acquisition
    def get_date_acquisition(self):
        return self._date_acquisition

    def set_date_acquisition(self, new_date_acquisition):
        self._date_acquisition = new_date_acquisition

    date_acquisition = property(get_date_acquisition, set_date_acquisition)

    # getter et setter pour date_dernier_entretien
    def get_date_dernier_entretien(self):
        return self._date_dernier_entretien

    def set_date_dernier_entretien(self, new_date_dernier_entretien):
        self._date_dernier_entretien = new_date_dernier_entretien

    date_dernier_entretien = property(get_date_dernier_entretien, set_date_dernier_entretien)

    # getters et setters pour provenance
    def get_provenance(self):
        return self._provenance

    def set_provenance(self, new_provenance):
        self._provenance = new_provenance

    provenance = property(get_provenance, set_provenance)

    # setters et getters etat_service
    def get_etat_service(self):
        return self._etat_service

    def set_etat_service(self, new_etat_service):
        if new_etat_service not in self.ETAT_SERVICE:
            print("Valeur non acceptable")
        else:
            self._etat_service = new_etat_service

    etat_service = property(get_etat_service, set_etat_service)

    # getters/setters pour etat_conservation

    def get_etat_conservation(self):
        return self._etat_conservation

    def set_etat_conservation(self, new_etat_conservation):
        if new_etat_conservation not in self.ETAT_CONSERVATION:
            print("Valeur non acceptable")
        else:
            self._etat_conservation = new_etat_conservation

    etat_conservation = property(get_etat_conservation, set_etat_conservation)

    # setter/getter commentaires

    def get_commentaires(self):
        return self._commentaires

    def set_commentaires(self, new_commentaires):
        self._commentaires = new_commentaires

    commentaires = property(get_commentaires, set_commentaires)

    def enregistrer_equipement(self, filename):
        while True:
            try:    # Tente d'ouvrir la base de données et la créee si elle n'existe pas
                open(filename)  # renvoie False si elle n'existe pas ou s'il y a une prob d'ouverture
                db = TinyDB(filename, storage=YAMLStorage)  # ouverture de la bdd en YAML
                db.insert(self.__dict__)
            except IOError as e:
                print("I/O error({0}): {1}".format(e.errno, e.strerror))
                print("CrÃ©ation de la base de donnÃ©es...")
                TinyDB(filename, storage=YAMLStorage)
                continue
            break


# tests

equipement1 = Equipement(id=1, categorie_equipement='IRM', marque='Siemens', modele='SI20',
                         numero_serie='SI1021309', salle='B01', centre_de_service='maternité',
                         date_acquisition=datetime.date(2016, 10, 10),
                         date_dernier_entretien=datetime.date(2016, 10, 10), provenance='CHU St-Justine',
                         etat_service=Equipement.ETAT_SERVICE[1], etat_conservation=Equipement.ETAT_CONSERVATION[2],
                         commentaires='RAS')
equipement1.enregistrer_equipement('storage_temp.json')

equipement2 = Equipement(id=2, categorie_equipement='défibrillateur', marque='GE', modele='GE03',
                         numero_serie='GE12313', salle='D19', centre_de_service='accueil',
                         date_acquisition=datetime.date(2016, 3, 2),
                         date_dernier_entretien=datetime.date(2016, 4, 10), provenance='Croix-Rouge',
                         etat_service=Equipement.ETAT_SERVICE[0], etat_conservation=Equipement.ETAT_CONSERVATION[3],
                         commentaires='Il est gros')
equipement2.enregistrer_equipement('storage_temp.json')

equipement3 = Equipement(id=3, categorie_equipement='Microscope', marque='Nikon', modele='NI12',
                         numero_serie='NI11213', salle='G15', centre_de_service='analyse',
                         date_acquisition=datetime.date(2013, 3, 10),
                         date_dernier_entretien=datetime.date(2015, 2, 27), provenance='CHU St-Justine',
                         etat_service=Equipement.ETAT_SERVICE[0], etat_conservation=Equipement.ETAT_CONSERVATION[0],
                         commentaires='Occulaire brisé')
equipement3.enregistrer_equipement('storage_temp.json')


db2 = TinyDB('storage_temp.json', storage=YAMLStorage)
equipement = db2.all()
print(type(equipement))











