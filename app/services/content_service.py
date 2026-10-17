class ContentService:
    def __init__(self):
        self.db_falsa = [
            {"id": 1, "titulo": "Inception", "formato": "Película", "año": 2010},
            {"id": 2, "titulo": "Breaking Bad", "formato": "Serie", "año": 2008}
        ]
        self.contador_id = 3

    def obtener_todo(self):
        return self.db_falsa

    def obtener_id(self, c_id: int):
        for c in self.db_falsa:
            if c["id"] == c_id:
                return c
        return None

    def create(self, datos: dict):
        new =  {
            "id": self.contador_id,
            "titulo": datos["titulo"],
            "formato": datos["formato"],
            "año": datos["año"]
        }

        self.db_falsa.append(new)
        self.contador_id += 1
        return new

    def delete(self, c_id: int):
        for i,c in enumerate(self.db_falsa):
            if c["id"] == c_id:
                return self.db_falsa.pop(i)
        return None

    def update(self, c_id: int, datos: dict):
        for i,c in enumerate(self.db_falsa):
            if c["id"] == c_id:
                self.db_falsa[i]["titulo"] = datos.get("titulo", c["titulo"])
                self.db_falsa[i]["formato"] = datos.get("formato", c["formato"])
                self.db_falsa[i]["año"] = datos.get("año", c["año"])
            return self.db_falsa[i]
        return None


    