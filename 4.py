import subprocess

command = 'systeminfo'
print('Получение информмации о системе с помощщью команды: %s' % command)
subprocess.call(command)

command = 'fsutil'
param1 = 'volume'
param2 = 'diskfree'
param3 = 'C:'
print("Получение информации о диске командой: %s" % command)
subprocess.call([command, param1, param2, param3])
