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
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT studente.*
                    FROM studente
                    JOIN iscrizione ON studente.matricola = iscrizione.matricola
                    JOIN corso ON iscrizione.codins = corso.codins
                    WHERE corso.pd = %s """
        cursor.execute(query, (pd,))
        objStudente = []
        for dizionario in cursor:
            objStudente.append(Studente(**dizionario))
        cursor.close()
        cnx.close()
        return objStudente

    @staticmethod
    def getIscrittiCodins(codins):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT studente.*
                   FROM studente
                   JOIN iscrizione ON studente.matricola = iscrizione.matricola 
                   JOIN corso ON iscrizione.codins = corso.codins
                   WHERE corso.codins = %s """
        cursor.execute(query, (codins,))
        objStudente = []
        for dizionario in cursor:
            objStudente.append(Studente(**dizionario))
        cursor.close()
        cnx.close()
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
        cursor.execute(query, (codins,))
        tupla = []
        for row in cursor:
            tupla.append((row["CDS"], row["n"]))
        cursor.close()
        cnx.close()
        return tupla





