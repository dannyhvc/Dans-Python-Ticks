from dataclasses import dataclass

from types.detail.entity import Entity

@dataclass
class Document(Entity):
    name: str
    department_id: int
