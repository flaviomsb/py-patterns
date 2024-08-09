class User:
    def __init__(self, name: str, uuid: int):
        self.__name = name
        self.uuid = uuid

    # regular getter and setter
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # declare getter and setter using decorators
    @property
    def uuid(self):
        return self.__uuid

    @uuid.setter
    def uuid(self, uuid: int):
        self.__uuid = f"000{uuid}"

    def display_name(self) -> str:
        return f"{self.__name} ({self.uuid})"


user = User("John Doe", 87593)
print(user.display_name())
