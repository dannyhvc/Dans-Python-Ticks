from types.detail.department import Department
from types.detail.document import Document
from types.detail.employee import Employee
from types.managers.manager import Manager
from types.detail.entity import Entity


class Context:
    def __init__(self) -> None:
        self.__counter_ctx: dict[Manager, int] = {
            Employee: 0,
            Document: 0,
            Department: 0,
        }

    def add_id(self, entity: Entity) -> None:
        entity.Id = self.__counter_ctx.get(type(entity), 0)
        self.__counter_ctx[type(entity)] += 1

    def get_infs(self) -> tuple[int, int, int]:
        return (self.__counter_ctx[Employee], 
                self.__counter_ctx[Document], 
                self.__counter_ctx[Department])
