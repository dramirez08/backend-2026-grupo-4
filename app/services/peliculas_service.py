class PeliculaService:
    def __init__(self):
        self.db_falsa = [
            {"id": 1, "titulo": "Inception", "director": "Christopher Nolan", "año": 2010}
        ]

    def obtener_todas(self):
        return self.db_falsa