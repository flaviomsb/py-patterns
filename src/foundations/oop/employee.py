from user import User


class Employee(User):
    company_name = "Patterns corp"

    def __init__(self, name: str, uuid: int, role: str):
        super().__init__(name, uuid)
        self._role = role

    def display_name(self) -> str:
        return super().display_name() + " - " + self._role

    @classmethod
    def company(cls):
        return cls.company_name

    @staticmethod
    def work_schedule():
        return "40 hours / week"

    def __str__(self) -> str:
        return "{0} with role {1}".format(super().__str__(), self._role)
