class Corso:
    def __init__(self, codins, crediti, nome, pd):
        self._codins = codins
        self._crediti = crediti
        self._nome = nome
        self._pd = pd

    @property
    def codins(self):
        return self._codins

    @property
    def crediti(self):
        return self._crediti

    @property
    def nome(self):
        return self._nome

    @property
    def pd(self):
        return self._pd

    def __str__(self):
        return self._nome+" ("+self.codins+")"