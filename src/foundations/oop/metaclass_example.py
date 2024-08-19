class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Created instance of {name}")
        return super().__new__(cls, name, bases, dct)


class CustomClass(metaclass=Meta):
    pass


obj = CustomClass()
