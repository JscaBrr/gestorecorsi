from database.DB_connect import DBConnect
from model.corso import Corso
from model.studente import Studente

class DAO():

    @staticmethod
    def getAllCorsi():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT *
                   FROM corso"""
        cursor.execute(query)
        """
        cursor.fetchall() -> lista di dizionari
        > carica tutti i dati subito in memoria come fetchall(). 
        cursor [tyipe: <mysql.connector.cursor.MySQLCursor object at 0x7f8a4c3d2c10>] -> non è una lista, ma un oggetto che recupera i dati su richiesta.
        > I dati non sono ancora stati caricati in memoria! Vengono recuperati uno alla volta quando iteri su cursor.
        > A ogni iterazione, il database invia una riga alla volta.
        """
        objCorso = []
        for dizionario in cursor:
            objCorso.append(Corso(**dizionario))
        cursor.close()
        cnx.close()
        return objCorso

    @staticmethod
    def getCorsiPD(pd):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * 
                    FROM corso
                    WHERE corso.pd = %s """
        cursor.execute(query, (pd,))
        objCorso = []
        for dizionario in cursor:
            objCorso.append(Corso(**dizionario))
        cursor.close()
        cnx.close()
        return objCorso

    @staticmethod
    def getIscrittiCorsiPD(pd):
        #restituisce per ogni corso il numero di iscritti filtrati dal pd
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT c.codins, c.crediti, c.nome, c.pd, count(*) as n
                        FROM corso c, iscrizione i
                        where c.codins = i.codins 
                        and c.pd = %s
                        group by c.codins, c.crediti, c.nome, c.pd"""
        cursor.execute(query, (pd,))
        tuple = []
        for dizionario in cursor:
            tuple.append((Corso(dizionario["codins"],
                                   dizionario["crediti"],
                                   dizionario["nome"],
                                   dizionario["pd"]), dizionario["n"]))
        cursor.close()
        cnx.close()
        return tuple

    @staticmethod
    def getIscrittiCodins(codins):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT studente.*
                   FROM studente
                   JOIN iscrizione ON studente.matricola = iscrizione.matricola 
                   JOIN corso ON iscrizione.codins = corso.codins
                   WHERE corso.codins = %s """
        #oppure:
        #SELECT s.*
        #FROM studente s, iscrizione i
        #WHERE s.matricola = i.matricola
        #AND i.codins = %s
        cursor.execute(query, (codins,))
        objStudente = []
        for dizionario in cursor:
            objStudente.append(Studente(**dizionario))
        cursor.close()
        cnx.close()
        #restituiti in ordine di matricola (PK)
        return objStudente

    @staticmethod
    def getCDSofCorso(codins):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT s.CDS, count(*) as n 
                            FROM studente s, iscrizione i 
                            WHERE s.matricola = i.matricola 
                            and i.codins = %s
                            and s.CDS != ""
                            group by s.CDS """
        #oppure
        #SELECT s.CDS, COUNT(*) as n
        #FROM studente s
        #JOIN iscrizione i ON s.matricola = i.matricola
        #WHERE i.codins = %s
        #AND s.CDS != ""
        #GROUP BY s.CDS;
        cursor.execute(query, (codins,))
        tupla = []
        for row in cursor:
            tupla.append((row["CDS"], row["n"]))
        cursor.close()
        cnx.close()
        #ordinati per matricola del primo studente che aveva quel corso
        return tupla

if __name__ == '__main__':
    print(DAO.getIscrittiCorsiPD(1))




