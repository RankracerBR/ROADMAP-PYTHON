class A:
    def method_a(self):
        print("Method of the A class")

class B:
    def method_b(self):
        print("Method of the B class")
    
class C(A,B):
    def method_c(self):
        print("Method of the C class")
        
obj = C()
obj.method_a()
obj.method_b()
obj.method_c()