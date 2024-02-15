import os
import time

#source = ['C:\Users\23529\Desktop\git\python-test']
#形如'C:\Users\23529\Desktop\git\python-test'需要考虑转义字符

source = ["C:\\Users\\23529\\Desktop\\git\\python-test"]
target_dir = ["C:\\Users\\23529\\Desktop\\fangzhen"]

target = target_dir[0] + os.sep + \
    time.strftime('%Y%m%d%H%M%S') + '.zip'

if not os.path.exists(target_dir[0]):
    os.mkdir(target_dir[0])

zip_command = 'zip -r {0} {1}'\
    .format(target,' '.join(source))

print('zip command is:')
print(zip_command)

print('running:')
if os.system(zip_command) == 0:
    print('successful backup to: ',target)
else:
    print('BACKUP FAILED')
