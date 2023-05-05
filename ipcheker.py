from ipaddress import ip_address
import socket

host = input ("Masukan link website/domain : ")
ip_address = socket.gethostbyname(host)

print(f"Nama Domain : {host}")
print(f"IP Address : {ip_address}")