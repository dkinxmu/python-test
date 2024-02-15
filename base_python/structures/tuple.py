#元组不可变！！！！！！！！！
zoo = ('python', 'elephant', 'penguin')
print('number of animals in the zoo is ', len(zoo))

new_zoo = ('ant', 'cat', zoo)

print('all animals are:', new_zoo)

print('last animals brought from old zoo is: ',new_zoo[1][2])#?、？
print('last animals brought from old zoo is: ',new_zoo[2][2])