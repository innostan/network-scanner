import socket
import ipaddress


while True:
    target = input("Enter an IP address (or q to quit): ")

    if target.lower() == "q":
        print("Program ended.")
        break
    try:
        ipaddress.ip_address(target)
        print(f"{target} is a valid IP address")
    except ValueError:
        print(f"{target} is NOT a valid IP address")
        print("Please enter a proper IP address.")
        continue

    try:
        start_port = int(input("enter a starting port number : "))
        end_port = int(input("enter ending port number. "))

        if start_port < 1 or start_port > 65535:
            print("invalid starting port number")
            continue
        if end_port  <1 or end_port > 65535:
            print("invalid end port number ")
            continue

        if start_port > end_port:
            print("start port cannot be greater than ending port ")
            continue

    except ValueError:
        print("that is not a valid port number. ")
        continue
    for port in range(start_port, end_port + 1 ):
        sock = socket.socket()
        sock.settimeout(3)
        result = sock.connect_ex((target,port))
        if result == 0:
            print(f"port {port} on target {target} is open.")
        else:
            print(f"port {port} on target {target} is closed or unreachable ")
        sock.close()
