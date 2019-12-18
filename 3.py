import subprocess

code = subprocess.call(["ping", "www.yandex.exe"])
print(code)