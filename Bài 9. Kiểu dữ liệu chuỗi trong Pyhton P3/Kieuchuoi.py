# phần định dạng
row_1 = '+{:-<6} + {:-^15} + {:->10} +'.format('', '', '')
row_2 = '|{:<6} | {:^15} | {:>10} |'.format('ID', 'Ho va ten', 'Noi sinh')
row_3 = '|{:<6} | {:^15} | {:>10} |'.format('123', 'Nguyen Van Lao', 'Binh Duong')
row_4 = '|{:<6} | {:^15} | {:^10} |'.format('456', 'LaoF', 'AOV')
row_5 = '+{:-<6} + {:-^15} + {:->10} +'.format('', '', '')
# phần xuất kết quả
print(row_1)
print(row_2)
print(row_3)
print(row_4)
print(row_5)