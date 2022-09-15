#imports libs
from urllib.request import urlopen
import sys
import requests
from bs4 import BeautifulSoup

try:
    #taking the ip informent from argument.
    ip = requests.get("https://api.ipify.org/").text

    if ip:
        #URL API
        url = f"http://ip-api.com/json/{ip}?fields=query,country,city"
    
        #Start to Request
        request = urlopen(url)
        data = request.read().decode()
        
        #Convert string API to DICT(dictionary)
        data = eval(data)

        for i in data:
            with open ("./data/ipv4.json", "a", newline="", encoding="UTF-8") as f:
                for ip in ip:
                    ipv4 = (f"{i} == {data[i]}")
                    ipv4_linha = ipv4 + "\n"
                    print(ipv4_linha)
                    f.write(ipv4_linha)
except Exception as ex:
    print(f"Error: {ex}")
