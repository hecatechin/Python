#turple test
s='abc'
t=(s,3,5)
#TurpleItemTest: to test if an item in Turple could be an object 
print(t)
print(s)

class Test:
    a=1

t1 = Test()
t2 = Test()

t1.a = 1
t2.a = 2

tt = (t1,t2)
t1.a = 2
t2.a = 1
print(tt[0].a)

