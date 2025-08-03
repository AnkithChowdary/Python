class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")
    #cls is the class itself
    # These are often used as factory methods
    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")
        # It can be called with the class name
        # They are used to just place a method inside a class
    @staticmethod
    def static_method():
        print("Called static_method.")

test=ClassTest()
test.instance_method()
ClassTest.instance_method(test)
# As it is a class method it can be called without an instance
ClassTest.class_method
ClassTest.static_method()