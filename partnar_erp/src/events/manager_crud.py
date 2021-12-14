from typing import Callable
from types.contexter.context import Context
from types.detail.entity import Entity
from types.managers.manager import Manager
import pickle


def serializer(mgr: Manager or Context):
    with open(mgr.pickle_file_name, 'wb+') as pickle_file:
        pickle.dump(mgr, pickle_file)
        

def deserialize(pickle_file_name: str) -> Manager | Context | None:
    try:
        with open(pickle_file_name, 'rb') as pickle_file:
            return pickle.load(pickle_file)
    except FileNotFoundError:
        print(f'{pickle_file_name} not found')


def add_new(ctx: Context, mgr: Manager, entity: Entity):
    ctx.add_id(entity)
    mgr.entities.append(entity)


def remove(mgr: Manager, entity: Entity) -> None:
    mgr.entities.remove(entity)


def clear(mgr: Manager) -> None:
    mgr.entities.clear()


def get_by_id(mgr: Manager, id: int) -> Entity:
    for entity in mgr.entities:
        if entity.Id == id:
            return entity
    return None


def first_or_default(
    mgr: Manager, fn: Callable[[Entity], Entity]
) -> Entity:
    for entity in mgr.entities:
        if fn(entity):
            return entity
    return None


def get_latest(mgr: Manager) -> Entity:
    return mgr.entities[0]


def get_all(mgr: Manager) -> list[Entity]:
    return list(mgr.entities)
