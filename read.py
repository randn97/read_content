import requests

link = requests.get('https://www.google.com')
print(link.text)
file = open("url Data.txt","w")
file.write(link.text)
file.close()