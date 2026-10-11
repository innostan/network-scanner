import socket
import ipaddress
import errno
from service_detection import detect_service

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

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)

        try:
            result = sock.connect_ex((target, port))
        finally:
            sock.close()

        if result == 0:
            print(f"Port {port} on target {target} is OPEN")

            service, banner = detect_service(target, port)
            print(f"  Service: {service}")

            if banner:
                print(f"  Banner: {banner.splitlines()[0]}")

        elif result == errno.ECONNREFUSED:
            print(f"Port {port} on target {target} is CLOSED")

        else:
            print(f"Port {port} on target {target} returned error {result}")
    








