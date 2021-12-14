from collections import deque
from dataclasses import dataclass

from types.managers.manager import Manager
from types.detail.department import Department


@dataclass
class DepartmentManager(Manager):
    pickle_file_name: str
    entities: deque[Department] = []
