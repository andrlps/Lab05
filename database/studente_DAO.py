# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection
from model.studente import Studente


class studente_DAO:
    def __init__(self):
        self._lista = []
        self._studentiCorsi = dict()
        self.getAllStudenti()
        self.getStudentiCorsi()

    def getAllStudenti(self):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM studente")

        for row in cursor:
            self._lista.append(Studente(str(row["matricola"]), row["nome"], row["cognome"], row["CDS"]))

    def getStudentiCorsi(self):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        for studente in self._lista:
            cod = studente.matricola
            cursor.execute("SELECT codins FROM iscrizione WHERE matricola = '" + cod + "'")
            self._studentiCorsi[cod] = []
            for row in cursor:
                self._studentiCorsi[cod].append(row["codins"])

    @property
    def lista(self):
        return self._lista

    @property
    def studentiCorsi(self):
        return self._studentiCorsi

    def aggiungiStudenteCorso(self, matricola, codins):
        print("aggiunto")

if __name__ == '__main__':
    corso = studente_DAO()
    corso.getAllStudenti()