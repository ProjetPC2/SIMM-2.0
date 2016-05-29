# coding=utf-8
from tinydb import *
from bbd_equipement import yamlStorage
import re


class EquipementManager:
    def __init__(self, pathname, archive_id_eq_pathname):
        self._pathname = pathname                               # pathname de la base de données des équipements
        self._archive_id_eq_pathname = archive_id_eq_pathname   # pathname de la base de données de l'archive des équip.

    def AjouterEquipement(self, dictio):
        #print('ouverture de la bdd')
        db1 = TinyDB(self._pathname, storage=yamlStorage.YAMLStorage)        # data base des équipements
        db2 = TinyDB(self._archive_id_eq_pathname, storage=yamlStorage.YAMLStorage)
        #print('Attribution du ID')
        id_eq = self._ObtenirProchainID()                                   # id du nouvel équipement
        db2.insert({'id': str(id_eq), 'utilisation': True})          # ajout d'un nouvel équipement utilisé dans l'archive
        #print(str(id_eq))
        #print('Insertion de equipement')
        db1.insert({'id': str(id_eq), 'data': dictio['data']})           # ajout du nouvel équipement dans la base de données

    def SupprimerEquipement(self, id_supp):
        Equipement = Query()
        db = TinyDB(self._pathname, storage=yamlStorage.YAMLStorage)        # data base des équipements
        db_arch = TinyDB(self._archive_id_eq_pathname, storage=yamlStorage.YAMLStorage) # data base de l'archive
        db.remove(Equipement['id'] == id_supp)                  # suppression de l'équipement (à voir...)
        db_arch.update({'utilisation': False}, Equipement['id'] == id_supp)

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

    def RechercherEquipement(self, regex_dict):
        db = TinyDB(self._pathname, storage=yamlStorage.YAMLStorage)

        recherche = Query()
        # Définir les critères de recherche

        result = db.search(recherche['id'].matches(regex_dict['id']) & recherche['data'].matches['CategorieEquipement'])
        return result

    def ModifierEquipement(self, id_modif, dict_modif):
        Equipement = Query()
        db = TinyDB(self._pathname, storage=yamlStorage.YAMLStorage)        # data base des équipements
        db.update({'data': dict_modif}, Equipement['id'] == id_modif)  # modif du dict associé à l'équipement

    def _ObtenirProchainID(self):
        db = TinyDB(self._archive_id_eq_pathname, storage=yamlStorage.YAMLStorage)   # data base de l'ARCHIVE des équipements
        nb_element = len(db)                                                         # nb d'équipements dans la base de données
        return nb_element + 1                                       # nouvel id (prochain numéro sur la liste)
