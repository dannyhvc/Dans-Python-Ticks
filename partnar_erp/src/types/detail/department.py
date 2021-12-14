from dataclasses import dataclass

from types.detail.entity import Entity

@dataclass
class Department(Entity):
    name: str
    location: str
