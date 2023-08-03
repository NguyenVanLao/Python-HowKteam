set1 = {1,2}
print(set1)
print(type(set1))
set2 = {'Nguyen Van Lao'}
print(set2)
set1 = set([1,2,3])
print(set1)
set2 = set('Nguyen Van Lao')
print(set2)
#tao empty trong set
set0 = set()
print(set0)
#Toan tu in 
print(9 in {1,2,3})
S1 = {1,2,3,4,5}
S2 = {2,3}
print(S1-S2)
print(S1 & S2)
print(S1 ^ S2)
print(S1 | {6,7,8})
set1.clear()
print(set1)
S2.pop()
print(S2) #Lay phan tu dau tien trong kieu set
S1.remove(2)
print(S1)
S3 = {1,2,3}
S3.discard(2)
print(S3)
S3 = S1.copy()
print(S3)
S3.add(2)
print(S3)
#Set khong phai la mot hash object
S3 = {1,2}
print(id(S3))
S3.add(3)
print(id(S3))


#Bai tap cung co 
a = {1,2}
b=a
b.clear()
print(a)
print(b)


