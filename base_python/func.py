def compare( a , b ):
    if(a > b):
        print('a>b')
    elif(a < b):
        print('a<b')
    else:
        print('a=b')
a,b=input('Enter a and b:').split()
compare(a,b)