#hiden method
class MyClass:

    def __init__(self):
        self._secret_method()

    def _secret_method(self):
        print("This is a hidden method.")

my_instance = MyClass()
my_instance._secret_method()

#private method

class __MyClass:
    pass