# Write your code here
from abc import ABC, abstractmethod
class A(ABC):           #C has access to this class-D has access- E has access 
    def a(self):
        self.b()

    def e(self):
        self.c()

    @abstractmethod
    def b(self):
        pass
    @abstractmethod
    def c(self):
        pass
    @abstractmethod
    def f(self):
        pass


class B(A):  #B inherits class A - C has access to this class
    def b(self):
        self.a()

    def c(self):
        self.e()


class C(ABC, B):     #C inherits B- D has acess to this class- E has access to this class
    @abstractmethod
    def f(self):
        pass


class D(A, C):            #D inherits A- E has access to this class
    def b(self):
        self.f()


class E(D):             #E inherits D
    def c(self):
        self.a()

    def f(self):
        self.e()

    def g(self):
        self.f()


class F(A):                
    def a(self):
        self.b()
        self.f()
