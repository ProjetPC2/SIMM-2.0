# coding=utf-8
from tinydb import *
from bbd_equipement import yamlStorage
import re


class EquipementManager:
    def __init__(self, pathname, archive_id_eq_pathname):
        self._pathname = pathname                               # pathname de la base de données des équipements
        self._nextID = 0   # pathname de la base de données de l'archive des équip.
        # nextID à mettre dans le fichier de configuration

    def AjouterEquipement(self, dictio):
        #print('ouverture de la bdd')
        db1 = TinyDB(self._pathname, storage=yamlStorage.YAMLStorage)        # data base des équipements
        #print('Attribution du ID')
        id_eq = self._ObtenirProchainID()                                   # id du nouvel équipement
        #print(str(id_eq))
        #print('Insertion de equipement')
        dictio['ID'] = id_eq
        # Verifier que tout ce qui est dans dictio est conforme à la forme d'un équipement et COMPLET
        db1.insert(dictio)           # ajout du nouvel équipement dans la base de données

    def SupprimerEquipement(self, id_supp):
        Equipement = Query()
        db = TinyDB(self._pathname, storage=yamlStorage.YAMLStorage)        # data base des équipements
        result = db.remove(Equipement['ID'] == id_supp)                              # suppression de l'équipement (à voir...)
        return result

    def RechercherEquipement(self, regex_dict):
        db = TinyDB(self._pathname, storage=yamlStorage.YAMLStorage)

        recherche = Query()
        
        firstEntry = True
        for key,value in regex_dict:
            if firstEntry:
                queryUser = recherche[key].matches(value)
                firstEntry = False
            else:
                queryUser = & recherche[key].matches(value)
        result = db.search(queryUser)
        return result

    def ModifierEquipement(self, id_modif, dict_modif):
        Equipement = Query()
        db = TinyDB(self._pathname, storage=yamlStorage.YAMLStorage)        # data base des équipements
        # Verifier que tout ce qui est dans dict_modif est conforme à la forme d'un équipement et COMPLET
        db.update(dict_modif, Equipement['ID'] == id_modif)  # modif du dict associé à l'équipement

    def _ObtenirProchainID(self):
        ID = self._nextID
        self._nextID = self._nextID + 1                             # nb d'équipements dans a base de données
        return ID                                                   # nouvel id (prochain numéro sur la liste)

    def _VerifierDict(self, dictio):
        conforme = self.verifierChamps(dictio)
        # Vérifier que le contenu de chaque champ est conforme à ce qui est attendu
        for key, value in dictio:
            if key == '':
                if (value != TODO)
                    conforme = False
            elif key == '':
            ...
            else:
                
        
    def _verifierChamps(self, dictio)
    # verifier la présence de tous les champs et qu'aucun champs supplémentaire ne soit présent
    conforme = True
    return conforme
