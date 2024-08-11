from user import User


class Employee(User):
    def __init__(self, name: str, uuid: int, role: str):
        super().__init__(name, uuid)
        self.__role = role

    def display_name(self) -> str:
        return super().display_name() + " - " + self.__role
