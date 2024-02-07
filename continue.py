while True:
    i = input('Enter sth:')
    if i == 'quit':
        break
    if len(i) < 3:
        print('Too short')
        continue
    print('Length is ',len(i))