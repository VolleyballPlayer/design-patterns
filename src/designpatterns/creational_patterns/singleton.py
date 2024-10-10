class Singleton:
    """The Singleton class can be implemented in different ways in Python.
    
    Some possible methods include: base class, decorator, metaclass.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Write a class and invoke it like a function."""
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Receipt(Singleton):
    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """

        # ...


if __name__ == "__main__":
    # The client code.

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")