#sysinfo.ry

import subprocess

def systeminfo():
    command = 'systeminfo'
    print('Получение информации о системе с помощьб команды: %s' % command)
    subprocess.call(command)

def fsutil():
    command = 'fsutil'
    param1 = 'volume'
    param2 = 'diskfree'
    param3 = 'C:'
    print("Получение информации о диске командой: %s" % command)
    subprocess.call([command, param1, param2, param3])

def main():
    systeminfo()
    fsutil()

main()