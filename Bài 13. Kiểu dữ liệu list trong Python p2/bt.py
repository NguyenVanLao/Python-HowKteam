#CAC PHUOGN THUC TIEN ICH
#Phuong thuc Count
a = [1,2,3,4,3,5,2,7]
b=a.count(2)
print(a)
print(b)
#Tìm phan tu trong list và tra ve vi tri
b1=a.index(2)
print(b1)
#Copy
a2=a.copy()
a2[1]='Nguyen Van Lao'
print(a2)
#Clear
a3=a.clear()
print(a3)
print(a)

##CAC PHUONG THUC CAP NHAT
#append: them phan tu vao cuoi list
a= [1,2,3,4,5]
a.append(6)
print(a)
a.append([7,8,9])
print(a)
#extend: them tung phan tu vao cuoi list
a= [1,2,3,4,5]
a.extend([4,5,[6,7,8]])
print(a)
#insert: them phan tu 7 vao vi tri 1 trong list
a= [1,2,3,4,5]
a.insert(1,7) #-20 trai, +20 phai
print(a)
#Pop: bo di phan tu thu 3 trong list vaf tra ve gia tri phan tu
c= [1,2,3,4,5]
c.pop(3)
print(c)
c1=c.pop(3)
print(c1)
#remove: bo di phan tu dau tien trong list co gia tri la 2
a= [1,2,3,4,5]
a.remove(2)
print(a)

##CAC PHUONG THUC XU LI
#reverse: dao nguoc phan tu trong list
a= [1,2,3,4,5]
a.reverse()
print(a)
#sort: <List>.sort(key=None, reverse=False)
    # So sanh cac phan tu tu be den lon bang cach ss truc tiep
    #Nếu là False, các phần tử được sắp xếp từ bé đến lớn, còn ngược lại là 
    #từ lớn đến bé.

a= [2,1,4,5,3]
a.sort()
print(a)
lst= ['a','c','b','d']
lst.sort()
print(lst)
    #Từ khóa reverse, cho 2 gia tri true or false
g=a.copy()
g.sort(reverse=True)
print(g)
g.sort(reverse=False)
print(g)

#Baitap
#1/ 
#lst=list()
#print(lst)
#q=lst.pop()
#print(q)
#2/
lst = [[1,2],['abc','def']]
z=lst.sort()
print(z)








