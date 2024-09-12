import nmap

scanner = nmap.PortScanner()

print("Welcome, this is a simple nmap automation tool")
print("<---------------------------------------------------->")

target = input("Enter the target IP address: ")
type = input("Enter the type of scan you want to run? (1 for SYN ACK Scan) (2 for UDP Scan) (3 for Comprehensive Scan): ")

if type == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(target, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[target].state())
    print(scanner[target].all_protocols())
    print("Open Ports: ", scanner[target]['tcp'].keys())
elif type == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(target, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[target].state())
    print(scanner[target].all_protocols())
    print("Open Ports: ", scanner[target]['udp'].keys())
elif type == '3':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(target, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[target].state())
    print(scanner[target].all_protocols())
    print("Open Ports: ", scanner[target]['tcp'].keys())
else:
    print("Invalid option. Please enter a valid option.")