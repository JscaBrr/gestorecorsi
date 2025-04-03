from database.DAO import DAO

class Model:
    def __init__(self):
        self.c = None

    def getAllCorsi(self):
        #si passa self perchè è un metodo di istanza
        return DAO.getAllCorsi()

    def getCorsiPD(self, pd):
        return DAO.getCorsiPD(pd)

    def getIscrittiCorsiPD(self, pd):
        return DAO.getIscrittiCorsiPD(pd)

    def getIscrittiCodins(self, codins):
        objStudente = DAO.getIscrittiCodins(codins)
        objStudente.sort(key=lambda s: s.cognome) #la chiave è un campo di Studente
        return objStudente

    def getCDSofCorso(self, codins):
        tupla = DAO.getCDSofCorso(codins)
        tupla.sort(key=lambda c: c[1], reverse=True)
        return tupla