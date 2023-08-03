a='nguyen van lao'
b=a.capitalize()# viết hoa chữ cái đầu tiên ở đầu dòng 
print(b) 
c=a.upper()#Viết hoa tất cả các kí tự 
print(c)
d=c.lower()#tất cả kí tự viết thường
print(d)
e=b.swapcase()#Kí tự viết thường thành hoa và ngược lại
print(e)
f=a.title()
print(f) # viết hoa kí tự đầu ở từ  
s= a.center(31,'*') #căn giữa, chỉ sử dụng 1 char
print(s)
g=a.rjust(50,'-')# căn lề phải or căn lề trái (ljust)
print(g)
t=a.encode(encoding='utf-8',errors='strict')
print(t)
print('có gì cold'.encode())
print(a.join(['1',' 2',' 3']))
print(a.replace('a','Lào',1))#thay thế một string, theo thứ tự thay thế theo thứ tự lần lượt
print(a.strip('o')) #loại bỏ các ký tự nằm ở 2 đầu string
print(a.rstrip('ao'))#loại bỏ các ký tự nằm ở bên phải hoặc bên trái(lstrip)
