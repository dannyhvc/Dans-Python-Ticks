from dataclasses import dataclass
from collections import deque

from types.managers.manager import Manager
from types.detail.document import Document


@dataclass
class DocumentManager(Manager):
    pickle_file_name: str
    entities: deque[Document] = []
