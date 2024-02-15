shoplist = ['a', 'b', 'c']
newlist = shoplist
del shoplist[0]

print(shoplist)
print(newlist)

new = shoplist.copy()
neww = shoplist[:]
del shoplist[0]

print(shoplist)
print(new)
print(neww)