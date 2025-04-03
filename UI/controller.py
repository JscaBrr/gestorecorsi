import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._ddCodinsValue = None

    def fillddCodins(self):
        objCorso = self._model.getAllCorsi()
        for c in objCorso:
            self._view.ddCodins.options.append(ft.dropdown.Option(key=c.codins, #identifica univocamnete l'opzione - valore che viene salvato in on_change della _view
                                                                                #Flet converte automaticamente l’oggetto c in una stringa chiamando il suo metodo __str__(). Se __str__() non è stato definito in Corso, Python usa il repr di default
                                                                  data = c, #contiene i dati associati all'opzione
                                                                  text = c.codins, #testo mostrato in UI
                                                                  on_click=self.handleddCodins
                                                                  ))

    def handleddCodins(self, e):
        self._ddCodinsValue = e.control.data
        print(f"Codins selezionato: {e.control.data.nome} ({e.control.data.codins}) - type: {type(e.control.data)}")
        return e.control.data

    def handlebtnPrintCorsiPD(self, e):
        self._view.lvTxtOut.controls.clear()
        pd = self._view.ddPD.value
        if not pd:
            self._view.alert("Periodo didattico non selezionato")
            self._view.update_page()
            return
        objCorso = self._model.getCorsiPD(int(pd))
        if len(objCorso) == 0:
            self._view.alert("Nessun corso trovato")
        for obj in objCorso:
            self._view.lvTxtOut.controls.append(ft.Text(obj))
        self._view.update_page()

    def handlebtnPrintNumIscrittiCorsiPD(self, e):
        self._view.lvTxtOut.controls.clear()
        pd = self._view.ddPD.value
        if not pd:
            self._view.alert("Periodo didattico non selezionato")
            self._view.update_page()
            return
        tuplaObjInt = self._model.getIscrittiCorsiPD(int(pd))
        if len(tuplaObjInt) == 0:
            self._view.alert("Nessuno studente trovato")
        for tupla in tuplaObjInt:
            self._view.lvTxtOut.controls.append(ft.Text(f"{tupla[0]} - N Iscritti: {tupla[1]}"))
        self._view.update_page()

    def handlebtnPrintIscrittiCodins(self, e):
        self._view.lvTxtOut.controls.clear()
        codins = self._view.ddCodins.value
        if not codins:
            self._view.alert("Corso non selezionato")
            self._view.update_page()
            return
        objStudente = self._model.getIscrittiCodins(codins)
        if len(objStudente) == 0:
            self._view.alert("Nessuno studente trovato")
        for obj in objStudente:
            self._view.lvTxtOut.controls.append(ft.Text(obj))
        self._view.update_page()

    def handlebtnPrintCDSCodins(self, e):
        self._view.lvTxtOut.controls.clear()
        codins = self._view.ddCodins.value
        print(codins)
        if not codins:
            self._view.alert("Corso non selezionato")
            self._view.update_page()
            return
        cds = self._model.getCDSofCorso(codins)
        if len(cds) == 0:
            self._view.lvTxtOut.controls.append(
                ft.Text("Nessun CDS offerto da questo corso"))
            self._view.update_page()
            return
        for c in cds:
            self._view.lvTxtOut.controls.append(ft.Text(f"CDS: {c[0]} - N Iscritti: {c[1]}"))
            self._view.update_page()

