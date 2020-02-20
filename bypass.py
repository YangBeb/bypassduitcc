import requests,time,os
r = requests.Session()
from bs4 import BeautifulSoup as bs
if os.name == 'nt':os.system('cls')
else:os.system('clear')
print("""
# Tool Bypass Shortlink Duit.cc
# Author : AkasakaID
""")
try:
	url = input("Masukkan url: ")
	a = r.get(url).text
	b = bs(a,'html.parser')
	c = b.find("link",attrs={"itemprop":"mainEntityOfPage"})
	print('Hasil:',c["href"])
except requests.exceptions.MissingSchema:
	print("Masukkan url dengan benar!!")
except requests.exceptions.ConnectionError:
	print("Periksa Koneksi Internet Anda!!")
except:
	print("Gagal Bypass!!")