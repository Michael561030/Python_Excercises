class A(type): pass
class B(A):pass
class C(A):pass
class D(B):pass
class G(C):pass
class E(D,B):pass
class F(C):pass
class H(F,E,G): pass

print(E.__mro__)
