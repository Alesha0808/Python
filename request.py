import requests

rage = requests.get('https://ngs.ru')
print(rage.text)
