class MyClass:
    class_variable = 10  # This is a class variable

    def __init__(self, value):
        self.instance_variable = value  # This is an instance variable

    @staticmethod
    def static_method(self):
        print("This is a static method.")

# You can call the static method directly on the class itself
obj = MyClass("anna")
MyClass.static_method()