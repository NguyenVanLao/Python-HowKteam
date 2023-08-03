#Lấy toàn bộ nội dung của thư viện decimal
from decimal import*
#Lấy tối đa 30 chữ số của cả phần nguyên và phần thập phân decimal
getcontext().prec = 30
x = 10/3
print(x)
print(Decimal(10)/Decimal(3)) 
print(10/Decimal(3)) 