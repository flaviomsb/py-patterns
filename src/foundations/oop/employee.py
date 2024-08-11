from user import User


class Employee(User):
    company_name = "Patterns corp"

    def __init__(self, name: str, uuid: int, role: str):
        super().__init__(name, uuid)
        self.__role = role

    def display_name(self) -> str:
        return super().display_name() + " - " + self.__role

    @classmethod
    def company(cls):
        return cls.company_name
