shoplist = ['appale', 'mango', 'carrot']

print('i have', len(shoplist), 'items')

print('These items are:',end=' ')
for i in shoplist:
    print(i, end=' ')

shoplist.append('rice')
print(shoplist)

shoplist.append(['1', '2'])
print(shoplist)