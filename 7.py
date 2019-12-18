import subprocess
res = subprocess.Popen(['dir', 'c:/Temp'], stdout=subprocess.PIPE)
uname = res.stdout.read()
print(uname)