
import socket
import errno


def detect_service(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)

    try:
        sock.connect((target, port))

        # This version currently tests for HTTP.
        sock.sendall(b"GET / HTTP/1.0\r\n\r\n")
        response = sock.recv(512)

        if response.startswith(b"HTTP/"):
            return "HTTP", response.decode(errors="ignore")

        return "Unknown", response.decode(errors="ignore")

    except socket.timeout:
        return "Timeout", ""

    except OSError as error:
        if error.errno == errno.ECONNREFUSED:
            return "Connection refused", ""
        return f"Error: {error}", ""

    finally:
        sock.close()


if __name__ == "__main__":
    service, banner = detect_service("127.0.0.1", 8000)
    print(f"Service: {service}")
    print(f"Banner:\n{banner}")

