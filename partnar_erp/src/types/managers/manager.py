
from collections import deque
from dataclasses import dataclass

from types.detail.entity import Entity


@dataclass
class Manager: 
    pickle_file_name: str
    entities: deque[Entity] = []
