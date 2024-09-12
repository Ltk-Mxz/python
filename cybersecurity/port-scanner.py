import socket

target = input("Enter the target IP address: ")
port = int(input("Enter the target port: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(0.5)

result = s.connect_ex((target, port))
if result == 0:
    print(f"Port {port} is open")
else:
    print(f"Port {port} is closed")
s.close()
