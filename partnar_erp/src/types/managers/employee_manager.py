from collections import deque
from dataclasses import dataclass

from types.managers.manager import Manager
from types.detail.employee import Employee


@dataclass
class EmployeeManager(Manager):
    pickle_file_name: str
    entities: deque[Employee] = []
