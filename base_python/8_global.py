x = 50
'''全局作用域在整个程序中都是可访问的，除非被局部作用域的同名变量遮蔽。'''
def func_1 ():
    x = 1
    print('x in func_1 =',x)


def func_2():
    global x
    x = 2
    print('x in func_2 is ',x)


print('x = ', x)
func_1()
print('x after func_1 =',x)
func_2()
print('x after func_2 is',x)
