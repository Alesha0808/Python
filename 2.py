import subprocess

code = subprocess.call("win32calc.exe")
if code == 0:
    print("Успешно!")
else:
    print("Ошибка!")