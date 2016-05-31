from Equipement import Equipement
from tinydb import *

class BonTravail:

    ETAT_BON_TRAVAIL = {'Ouvert', 'Fermé'}

    def __init__(self, num_bon_travail, date_bon_travail, temps_estime,
                 description_situation, description_intervention, etat_bon_travail):
        self._num_bon_travail = num_bon_travail
        self._date_bon_travail = date_bon_travail
        self._temps_estime = temps_estime
        self._description_situation = description_situation
        self._description_intervention = description_intervention
        self._etat_bon_travail = etat_bon_travail

    # getter/setter num_bon_travail
    def get_num_bon_travail(self):
        return self._num_bon_travail

    def set_num_bon_travail(self, new_num_bon_travail):
        self._num_bon_travail = new_num_bon_travail

    num_bon_travail = property(get_num_bon_travail, set_num_bon_travail)

    # getter/setter date_bon_travail
    def get_date_bon_travail(self):
        return self._date_bon_travail

    def set_date_bon_travail(self, new_date_bon_travail):
        self._date_bon_travail = new_date_bon_travail

    date_bon_travail = property(get_date_bon_travail, set_date_bon_travail)

    # getter/setter temps_estime
    def get_temps_estime(self):
        return self._temps_estime

    def set_temps_estime(self, new_temps_estime):
        self._temps_estime = new_temps_estime

    temps_estime = property(get_temps_estime, set_temps_estime)

    # getter/setter description_situation
    def get_description_situation(self):
        return self._description_situation

    def set_description_situation(self, new_description_situation):
        self._description_situation = new_description_situation

    description_situation = property(get_description_situation, set_description_situation)

    # getter/setter description_intervention
    def get_description_intervention(self):
        return self._description_intervention

    def set_description_intervention(self, new_description_intervention):
        self._description_intervention = new_description_intervention

    description_intervention = property(get_description_intervention, set_description_intervention)

    # getter/setter etat_bon_travail
    def get_etat_bon_travail(self):
        return self._etat_bon_travail

    def set_etat_bon_travail(self, new_etat_bon_travail):
        if new_etat_bon_travail not in self.ETAT_BON_TRAVAIL:
            print('Non valide')
        else:
            self._etat_bon_travail = new_etat_bon_travail

    etat_bon_travail = property(get_etat_bon_travail, set_etat_bon_travail)






