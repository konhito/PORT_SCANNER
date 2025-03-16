import socket


def scan_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")


def main():
    host = input("Enter the IP address to scan: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    print(f"\nScanning {host} from port {start_port} to {end_port}...\n")

    for port in range(start_port, end_port + 1):
        scan_port(host, port)


if __name__ == "__main__":
    main()
