set1 = {'Nguyen Van Lao',1,2,3}
print(set1)

set2 = {2,3,2,3}
print(set2)
print(type(set2))

set3 = {}
print(set3)
print(type(set3))

set4 = {i for i in range(3)}
print(set4)

set5 = set((1,2,3,4))
print(set5)
set6 = set('Nguyen Van Lao')
print(set6)
#tao empty set bang contructor
set7 = set()
print(set7)
print(type(set7))
#Venn
print((1,2) in {1,2,3})
#Toan tu 
print({1,2,3,4} - {2,3})
print({3,4} - {3,4,5,6})
print({1,2,3} & {3,4,5})
print({1,2,3} | {3,4,5})
print({1,2,3} ^ {3,4,5})
print(set5)
set5.clear()
print(set5)
set5 = {1,2,3,4}
print(set5)
set5.pop()
print(set5)
set5.remove(4)
print(set5)
#Loai bo gia tri value trong set
set5.discard(2)
print(set5)
#Phương thức
#copy
set51 = set5.copy()
print(set51)

set5.add(2,)
print(set5)

set8 = {1,2,3,4}
print(id(set8))
set8.add(5)
print(id(set8))  
print('Nguyen Van Lao')
