
import requests

ip_public = requests.get("https://api.ipify.org/").text
print(f"IP Publico: {ip_public}")
