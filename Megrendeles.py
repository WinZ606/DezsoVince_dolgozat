class Megrendeles:
    def __init__(self,datum,rendeles:int,email):
        self.datum = datum
        self.rendeles = rendeles
        self.email = email

    def __str__(self):
        return f"{self.datum} {self.rendeles} {self.email}"