from database.DB_connect import get_connection
from model.corso import Corso


class corso_DAO:
    def __init__(self):
        self._lista = []
        self._corsiStudenti = dict()
        self.getAllCorsi()
        self.getCorsiStudenti()

    def getAllCorsi(self):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM corso")

        for row in cursor:
            self._lista.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))

        for row in cursor:
            print(row)

    def getCorsiStudenti(self):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        for corso in self._lista:
            cod = corso.codins
            cursor.execute("SELECT matricola FROM iscrizione WHERE codins = '"+cod+"'")
            self._corsiStudenti[cod] = []
            for row in cursor:
                self._corsiStudenti[cod].append(row["matricola"])

    @property
    def lista(self):
        return self._lista

    @property
    def corsiStudenti(self):
        return self._corsiStudenti

if __name__ == '__main__':
    corso = corso_DAO()
    corso.getAllCorsi()
    corso.getCorsiStudenti()