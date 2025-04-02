from dataclasses import dataclass

@dataclass
class Studente:
    matricola: int
    cognome: str
    nome: str
    CDS: str
    # corsi: list[Corso] = None
    # codins: list[str] = None

    def __eq__(self, other):
        return self.matricola == other.matricola

    def __hash__(self):
        return hash(self.matricola)

    def __str__(self):
        return f"{self.nome} {self.cognome} ({self.matricola}) - {self.CDS}"

