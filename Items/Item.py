from pydantic import BaseModel


class Item(BaseModel):

    id: str
    name: str
    description: str

    def jsonify(self):
        return {"id": self.id,
                "name": self.name,
                "description": self.description}
