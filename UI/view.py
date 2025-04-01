import flet as ft
from flet_core import MainAxisAlignment


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self._dd = None
        self._btnCerca = None
        self._matricola = None
        self._nome = None
        self._cognome = None
        self._btnCercaStudenti = None
        self._btnCercaCorsi = None
        self._btnIscrivi = None
        self._lv = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        self._dd = ft.Dropdown(label="Corso", hint_text="Seleziona un corso", width=550)
        self._controller.aggiungiBottoni()
        self._btnCerca = ft.ElevatedButton(text="Cerca Iscritti", width=200, height=50,
                                           on_click=self._controller.handleCercaIscritti)

        row2 = ft.Row([self._dd, self._btnCerca], alignment=MainAxisAlignment.CENTER)

        self._matricola = ft.TextField(label="Matricola", width=250)
        self._nome = ft.TextField(label="Nome", read_only=True, width=250)
        self._cognome = ft.TextField(label="Cognome", read_only=True, width=250)

        row3 = ft.Row([self._matricola, self._nome, self._cognome], alignment=MainAxisAlignment.CENTER)

        self._btnCercaStudenti = ft.ElevatedButton(text="Cerca Studente", width=200,
                                                   on_click=self._controller.handleCercaStudente)
        self._btnCercaCorsi = ft.ElevatedButton(text="Cerca Corsi", width=200, on_click=self._controller.handleCercaCorsi)
        self._btnIscrivi = ft.ElevatedButton(text="Iscrivi", width=200, on_click=self._controller.handleIscrivi)

        row4 = ft.Row([self._btnCercaStudenti, self._btnCercaCorsi, self._btnIscrivi],
                      alignment=MainAxisAlignment.CENTER)

        self._lv = ft.ListView(expand=True)

        self._page.add(row2, row3, row4, self._lv)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message, color="red"))
        self._page.dialog = dlg
        dlg.open = True
        self._lv.clean()
        self._cognome.value = None
        self._nome.value = None
        self._cognome.value = None
        self._matricola.value = None
        self._dd.value = None
        self._page.update()

    def update_page(self):
        self._page.update()
