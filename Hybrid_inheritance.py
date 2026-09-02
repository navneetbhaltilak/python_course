# Base class
class A:
    def feature_a(self):
        print("Feature from A")

# Single inheritance
class B(A):
    def feature_b(self):
        print("Feature from B")

# Another base class
class C:
    def feature_c(self):
        print("Feature from C")

# Hybrid inheritance: combines multiple + multilevel
class D(B, C):
    def feature_d(self):
        print("Feature from D")

# Testing
obj = D()
obj.feature_a()  # From A (via B)
obj.feature_b()  # From B
obj.feature_c()  # From C
obj.feature_d()  # From D

print(D.mro())   # Shows Method Resolution Order
