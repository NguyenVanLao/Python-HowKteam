a= 'aaaAAaaaooaaneu mot Ngay naO Doaaaaaaa'
#
b=a[12:31].lower().title()
print(a)
print(b)
#
s = a.lower()
s = s.strip('a')
s = s.lstrip('ao')
print(s)
#
b = a.lower().strip('a').lstrip('oa').title()
print(b)