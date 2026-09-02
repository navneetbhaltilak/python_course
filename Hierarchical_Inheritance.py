class Parent:
    def __init__(self, name):
        self.name = name
        print(f"Parent initialized with name: {self.name}")

    def common_feature(self):
        print(f"{self.name} has a common feature")

    @classmethod
    def class_info(cls):
        print("This is a class method of Parent")

    @staticmethod
    def utility():
        print("This is a static method")

    def __del__(self):
        print(f"Parent object {self.name} destroyed")


class Child1(Parent):
    def feature1(self):
        print(f"{self.name} has feature1")


class Child2(Parent):
    def feature2(self):
        print(f"{self.name} has feature2")


class Child3(Parent):
    def feature3(self):
        print(f"{self.name} has feature3")


# Testing
c1 = Child1("Child1")
c1.common_feature()
c1.feature1()
Child1.class_info()
Child1.utility()

c2 = Child2("Child2")
c2.common_feature()
c2.feature2()

c3 = Child3("Child3")
c3.common_feature()
c3.feature3()
