import flet as ft

class View(ft.UserControl):
    """
        Passare ft.UserControl come parametro in class View(ft.UserControl): significa che View eredita da UserControl.
        UserControl ] classe fornita da Flet, permette di creare componenti riutilizzabili e indipendenti.
        - Permette di aggiornare solo il componente (self.update()) senza ricaricare tutta la pagina.
        - Migliora la modularità e la riutilizzabilità del codice.
        - È riconosciuto da Flet come un vero componente UI.
    """
    def __init__(self, page: ft.Page):
        #parametro passato: pagina (page) su cui il componente UI sarà inserito.
        #page: ft.Page specifica che page è di tipo ft.Page
        super().__init__() #utilizzata per chiamare il costruttore della classe base (UserControl)
        # page stuff
        self._page = page #memorizza la pagina passata al costruttore nella variabile self._page
        self._page.title = "Gestore Corsi - Edizione 2025"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller
        self._controller = None
        # graphical elements
        self._title = None
        self.ddPD = None
        self.ddCodins = None
        self.btnPrintCorsiPD = None
        self.btnPrintIscrittiCorsiPD = None
        self.btnPrintIscrittiCodins = None
        self.btnPrintCDSCodins = None
        self.lvTxtOut = None

    def load_interface(self):
        # title
        self._title = ft.Text("Gestore Corsi - Edizione 2025", color="blue", size=24)
        self._page.controls.append(self._title)

        self.ddPD = ft.Dropdown(label="Periodo Didattico",
                                options=[ft.dropdown.Option('1'), ft.dropdown.Option('2')],
                                width=300)
        self.ddCodins = ft.Dropdown(label="Codice Insegnamento",
                                    width=300)
        self._controller.fillddCodins()
        self.btnPrintCorsiPD = ft.ElevatedButton(text="Stampa corsi",
                                                 on_click=self._controller.handlebtnPrintCorsiPD,
                                                 width=300)
        self.btnPrintNumIscrittiCorsiPD = ft.ElevatedButton(text="Stampa numero iscritti",
                                                         on_click=self._controller.handlebtnPrintNumIscrittiCorsiPD,
                                                         width=300)
        self.btnPrintIscrittiCodins = ft.ElevatedButton(text="Stampa iscritti al corso",
                                                         on_click=self._controller.handlebtnPrintIscrittiCodins,
                                                         width=300)
        self.btnPrintCDSCodins = ft.ElevatedButton(text="Stampa CDS afferenti",
                                                   on_click=self._controller.handlebtnPrintCDSCodins,
                                                   width=300)
        self.lvTxtOut = ft.ListView(expand=True)

        row1 = ft.Row([self.ddPD, self.btnPrintCorsiPD, self.btnPrintNumIscrittiCorsiPD])
        row2 = ft.Row([self.ddCodins, self.btnPrintIscrittiCodins, self.btnPrintCDSCodins])
        self._page.add(row1, row2, self.lvTxtOut)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def alert(self, message):
        #creazione dialogo di avviso
        dlg = ft.AlertDialog(title=ft.Row([ft.Icon(ft.icons.ERROR, color="red"), ft.Text("Errore:", color="red")]),
                             content=ft.Text(message, color="red"),
                             actions=[ft.TextButton("OK", on_click=lambda e: self.closealert(dlg))])
        self._page.dialog = dlg #impostazione del dialogo della pagina
        dlg.open = True #apertura del dialogo
        self._page.update()

    def closealert(self, dlg):
        dlg.open = False  # chiude il dialogo
        self._page.update()  # aggiorna la pagina

    def update_page(self):
        self._page.update()
