#How to call x method from A class and y method from B class

##SOLUTION

class A:
    def x(self):
        print('A class X method')

    def y(self):
        print('A class y method')


class B:
    def x(self):
        print('B class X method')

    def y(self):
        print('B class y method')


class C(A, B):
    def y(self):
        pass
        B.y(self)


obj = C()
obj.x()
obj.y()

