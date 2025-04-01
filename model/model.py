from database.corso_DAO import corso_DAO
from database.studente_DAO import studente_DAO

class Model:
    def __init__(self):
        self._listaStudenti = studente_DAO()
        self._listaCorsi = corso_DAO()

    def btnCorsi(self):
        lista = []
        for el in self._listaCorsi.lista:
            lista.append(el.nome)
        return lista

    def elencoStudenti(self):
        lista = []
        for el in self._listaCorsi.lista:
            lista.append(el.nome)
        return lista

    def elencoStudentiCorsi(self):
        return self._listaStudenti.studentiCorsi

    def elencoCorsiStudenti(self):
        return self._listaCorsi.corsiStudenti

    def elencoCorsi(self):
        return self._listaCorsi.lista

    def listaStudenti(self):
        return self._listaStudenti.lista

    def aggiungiStudenteCorso(self, matricola, codice):
        self._listaStudenti.aggiungiStudenteCorso(matricola, codice)