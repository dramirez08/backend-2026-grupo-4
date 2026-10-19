class ReseñaService:
    def __init__(self):
        self.db_falsa = [
            {"id": 1, "titulo_id": 1, "comentario": "exelente pelicula", "calificacion": 4.5}
        ]
        self.contador_id = 2

    def obtener_todo(self):
        return self.db_falsa

    def obtener_id(self, r_id: int):
        for r in self.db_falsa:
            if r["id"] == r_id:
                return r
        return None

    def create(self, datos: dict):
        new = {
            "id": self.contador_id,
            "titulo_id": datos["titulo_id"],
            "comentario": datos["comentario"],
            "calificacion": datos["calificacion"]
        }
        self.db_falsa.append(new)
        self.contador_id += 1
        return new

    def update(self, r_id: int, datos: dict):
        for i, r in enumerate(self.db_falsa):
            if r["id"] == r_id:
                self.db_falsa[i]["comentario"] = datos.get("comentario", r["comentario"])
                self.db_falsa[i]["calificacion"] = datos.get("calificacion", r["calificacion"])
            return self.db_falsa[i]
        return None

    def delete(self, r_id: int):
        for i, r in enumerate(self.db_falsa):
            if r["id"] == r_id:
                return self.db_falsa.pop(i)
        return None