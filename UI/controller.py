import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_hello(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def aggiungiBottoni(self):
        for el in self._model.btnCorsi():
            self._view._dd.options.append(ft.dropdown.Option(el))
        self._view.update_page()

    def handleCercaIscritti(self, e):
        self._view._lv.clean()
        if self._view._dd.value is None:
            self._view.create_alert("Selezionare un corso!")
            return
        corsoCorretto = None
        for corso in self._model.elencoCorsi():
            if corso.nome == self._view._dd.value:
                corsoCorretto = corso
                break
        self._view._lv.controls.append(
            ft.Text(f"Ci sono {len(self._model.elencoCorsiStudenti()[corsoCorretto.codins])} studenti:"))
        self._view.update_page()
        for matricola in self._model.elencoCorsiStudenti()[corsoCorretto.codins]:
            for studente in self._model.listaStudenti():
                if str(studente.matricola) == str(matricola):
                    self._view._lv.controls.append(ft.Text(studente))
        self._view.update_page()

    def handleCercaStudente(self, e):
        self._view._lv.clean()
        if self._view._matricola.value is None or self._view._matricola.value == "":
            self._view.create_alert("Digitare una matricola!")
            return
        matricola = self._view._matricola.value
        for studente in self._model.listaStudenti():
            if str(studente.matricola) == str(matricola):
                self._view._nome.value = studente.nome
                self._view._cognome.value = studente.cognome
                self._view.update_page()
                return studente
        self._view.create_alert("Matricola non presente!")
        return None

    def handleCercaCorsi(self, e):
        self._view._lv.clean()
        if self.handleCercaStudente(e) is None:
            return
        studente = self.handleCercaStudente(e)
        self._view._lv.controls.append(
            ft.Text(f"Lo studente frequenta {len(self._model.elencoStudentiCorsi()[studente.matricola])} corsi:"))
        for corsoFreq in self._model.elencoStudentiCorsi()[studente.matricola]:
            for corso in self._model.elencoCorsi():
                if str(corso.codins) == str(corsoFreq):
                    self._view._lv.controls.append(ft.Text(corso))
        self._view.update_page()

    def handleIscrivi(self, e):
        self._view._lv.clean()
        if self.handleCercaStudente(e) is None:
            return
        studente = self.handleCercaStudente(e)
        if self._view._dd.value is None:
            self._view.create_alert("Selezionare un corso!")
            return
        corsoCorretto = None
        for corso in self._model.elencoCorsi():
            if corso.nome == self._view._dd.value:
                corsoCorretto = corso
                break
        if self._model.elencoCorsiStudenti()[corsoCorretto.codins].__contains__(studente.matricola):
            return
        if self._model.elencoStudentiCorsi()[studente.matricola].__contains__(corsoCorretto.codins):
            return
        self._model.aggiungiStudenteCorso(studente.matricola, corsoCorretto.codins)
        self._view.create_alert("Studente aggiunto correttamente!")