class TitulosService:
    def __init__(self):
        self.db_falsa = [
            {"id": 1, "titulo": "Inception", "formato": "Película", "año": 2010, "director_id": 1},
            {"id": 2, "titulo": "Breaking Bad", "formato": "Serie", "año": 2008, "director_id": 2}
        ]
        self.contador_id = 3

    def obtener_todo(self):
        return self.db_falsa

    def obtener_id(self, t_id: int):
        for t in self.db_falsa:
            if t["id"] == t_id:
                return t
        return None

    def create(self, datos: dict):
        new =  {
            "id": self.contador_id,
            "titulo": datos["titulo"],
            "formato": datos["formato"],
            "año": datos["año"],
            "director_id": datos["director_id"]
        }

        self.db_falsa.append(new)
        self.contador_id += 1
        return new

    def delete(self, t_id: int):
        for i, t in enumerate(self.db_falsa):
            if t["id"] == t_id:
                return self.db_falsa.pop(i)
        return None

    def update(self, t_id: int, datos: dict):
        for i, t in enumerate(self.db_falsa):
            if t["id"] == t_id:
                self.db_falsa[i]["titulo"] = datos.get("titulo", t["titulo"])
                self.db_falsa[i]["formato"] = datos.get("formato", t["formato"])
                self.db_falsa[i]["año"] = datos.get("año", t["año"])
                self.db_falsa[i]["director_id"] = datos.get("director_id", t["director_id"])
            return self.db_falsa[i]
        return None


    