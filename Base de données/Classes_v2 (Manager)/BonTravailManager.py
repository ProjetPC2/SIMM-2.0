# coding=utf-8
from tinydb import *
from yamlStorage import YAMLStorage
import datetime
import re


class BonTravailManager:
    def __init__(self, bdt_pathname, archive_id_bdt_pathname):
        self._pathname = bdt_pathname                            # pathname de la base de données des bons de travail
        self._archive_id_bdt_pathname = archive_id_bdt_pathname  # pathname de la base de données de l'archive des bdt

    def AjouterBonTravail(self, id_equipement, dictio):
        db = TinyDB(self._pathname, storage=YAMLStorage)        # data base des bons de travail
        db_ID_bdT = TinyDB(self._archive_id_bdt_pathname, storage=YAMLStorage)
        id_bdt = self._ObtenirProchainIDdeBDT(id_equipement)  # id du nouveau bon de travail
        db_ID_bdT.insert({'id-eq': str(id_equipement), 'id-bdt': str(id_bdt), 'utilisation': True}) # ajout d'un nouveau bdt en cours
        db.insert({'id-eq': str(id_equipement), 'id-bdt': str(id_bdt), 'data': dictio})  # ajout du nouveau bdt dans la db

    def SupprimerBonTravail(self, id_eq_supp, id_bdt_supp):
        BonTravail = Query()
        db = TinyDB(self._pathname, storage=YAMLStorage)        # data base des bons de travail
        db.remove((BonTravail['id-eq'] == id_eq_supp) & (BonTravail['id-bdt'] == id_bdt_supp))  # suppression du bdt (???)
        db_arch = TinyDB(self._archive_id_bdt_pathname, storage=YAMLStorage) # data base de l'archive
        db_arch.update({'utilisation': False}, (BonTravail['id-eq'] == id_eq_supp) & (BonTravail['id-bdt'] == id_bdt_supp))

        # **************************************************************************************************
        # Voir avec Maxime et Alex:
        # # lorsqu'on supprime un équipement, est-ce qu'on fait seulement que changer l'état de
        # l'équipement, c-à-d changer le champ 'état de service' : Au rebut, dans le dictionnaire? Cela ferait en sorte
        # qu'on garderait tous les équipements 'au rebut' dans la bdd, mais ce champ indiquerait si on les affiche ou
        # non lorsqu'on fait un recherche. Pour les afficher, il faudrait préciser que l'équipement est au rebut.
        #
        # A quel point est-ce nécessaire d'avoir 2 bases de données : base de données + archive? On pourrait mettre dans
        # la base de donnée directement un champ "utilisation" ou "statut" ...
        # **************************************************************************************************

    def RechercherBonTravail(self, regex_dict):
        db = TinyDB(self._pathname, storage=YAMLStorage)

        recherche = Query()
        #définir les critères de recherche

        result = db.search(recherche['id-eq'].matches(regex_dict['id-eq']) & recherche['id-bdt'].matches(regex_dict['id-bdt']))
        return result

    def ModifierBonTravail(self, id_eq_modif, id_bdt_modif, dict_modif):
        BonTravail = Query()
        db = TinyDB(self._pathname, storage=YAMLStorage)        # data base des bons de travail
        # modif du dict associé au bdt
        db.update({'data': dict_modif}, (BonTravail['id-eq'] == id_eq_modif) & (BonTravail['id-bdt'] == id_bdt_modif))

    def _ObtenirProchainIDdeBDT(self, id_equip):
        BonTravail = Query()
        db = TinyDB(self._archive_id_bdt_pathname, storage=YAMLStorage)   # data base de l'ARCHIVE des bdt
        nb_bdt_pour_eq = db.count(BonTravail['id-eq'] == str(id_equip))  # nb de bdt pour cet équipement dans la db
        print('count', nb_bdt_pour_eq)
        # faire étape de vérification
        new_id_bdt = nb_bdt_pour_eq + 1                         # nouvel id de bdt

        return new_id_bdt
























