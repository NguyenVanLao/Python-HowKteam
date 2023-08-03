a=[1,2,3,4]
print(a)
print(['a','b',[2,'c']])
print([])
a=2
print(a)
a=[i for i in range(10)]
print(a)
a=[[n,n*1,n*2] for n in range(1,10)]
print(a)
a=list([1,2,3])
print(a)
a=list('Nguyen Van Lao')
print(a)
#Toan tu trong list
a=[1,2]
a +=['one','two']
print(a)
a +='Nguyen Van Lao'
print(a)

a=list('TD19CLC')
print(a*2)
b=[1,2,3]
print(b*2)

#Toan tu in
a=['Nguyen Van Lao',1,2]
b= 'Nguyen' in a #Kiem tra phan tu co trong list true or false
print(b)

#indexing va cat list trong Python
lst=[1,2,'a','b',[3,4]]
print(lst[2]) #trich phan tu tu list
print(lst[-2])
print(lst[-1][-1])
print(lst[0:2])#Cut list
print(lst[:2])
print(lst[2:])
print(lst[::])
print(lst[::-1])#dao chieu list

#Thay doi noi dung trong list
a=['Nguyen Van Lao','TD',36]
print(a[1])
a[1]='TD19CLC'
print(a)

#Matrix
a=[[1,2,3],[4,5,6]]
print(a[0])
print(a[-1])
print(a[0][1])#truy cap vao phan tu cua list
print(a[0][:])

#1
a=list()
print(a)
b=list(list(list('abc')))
print(b)
c=[0]*3
print(c)

s='aaaaaaaAAAAAaaa//123123//000000//&&TTT%%abcxyznontqfadf'
#s=list(s)
#s=s[35:38]
#print(s)


g=list(list(list('abc')))
print(g)
code = s.split('&&')[-1].split('%%')[0]
print(code)

	