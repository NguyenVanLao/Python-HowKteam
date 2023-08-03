#Tuple
a = (1,2,3,4)
print(a)
a1 = ()
print(a1)
a2 = ([1,2],['Nguyen'])
print(a2)
print(type(a2))
#Tuple Comprehension
tup = (i for i in range(10))
print(tup)
#Contructor Tuple
tup = tuple([1,2,3])
print(tup)
tup = tuple('Nguyen Van')
print(tup)
tup = (i for i in range(100) if i%2 == 0)
a=tuple(tup)
print(a)

#Toan tu
tup = (1,2,3)
tup += ('Nguyen',36)
print(tup)
tup = tup*2
print(tup)
a = (1,)*3
print(a)
v = 1 in tup 
print(v)

#indexing va cat trong Python
a = (1,2,3,'Nguyen',36)
b=a[3] 
print(b)

#Ma tran
tup = ((1,2,3),[4,5,6])
tup = tup[0][2]
print(tup)

#Cac phuong thuc cua Tuple
#Count
tup = (1,2,2,1,1,5)
c=tup.count(2)
print(c)
#index
a = tup.index(5)
print(a)

#Baitap
#1/
#tup= tuple([(1,2,3),+,[3,4]])
#print(tup)
#2/
tup = (1,2,[3,4])
tup[2] += ([50,60])
print(tup)
