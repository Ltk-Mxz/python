import socket
def grab_banner(host, port):
    s = socket.socket()
    s.connect((host, int(port)))
    banner = s.recv(1024).decode().strip()
    print(f"{host}:{port} : {banner}")
    s.close()

if __name__ == "__main__":
    import sys
    try:
        host = sys.argv[1]
        port = sys.argv[2]
        grab_banner(host, port)
    except IndexError:
        print(f"Usage: {sys.argv[0]} host port")
        sys.exit()