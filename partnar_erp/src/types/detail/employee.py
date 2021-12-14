from dataclasses import dataclass

from types.detail.entity import Entity

@dataclass
class Employee(Entity):
    first_name: str
    last_name: str
    department_id: int
