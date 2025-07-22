import socket
import sys
def basic_port_scanner():
    print("--- Very Basic Port Scanner ---")
    target_host = input("Enter the target IP address or hostname (e.g., localhost, 127.0.0.1): ")
    target_ip = socket.gethostbyname(target_host)
    print(f"Scanning target: {target_host} ({target_ip})")
    ports_to_scan = [21, 22, 23, 25, 80, 110, 443, 3389]
    print(f"Attempting to scan common ports: {', '.join(map(str, ports_to_scan))}")
    print("Timeout set to 1 second per port.")
    open_ports = []
    for port in ports_to_scan:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} is OPEN")
            open_ports.append(port)
        sock.close()
    print("\n--- Scan Summary ---")
    if open_ports:
        print(f"Open ports found on {target_host} ({target_ip}):")
        for p in open_ports:
            print(f"  - {p}")
    else:
        print(f"No open ports found in the scanned range on {target_host} ({target_ip}).")
    print("--------------------")
if __name__ == "__main__":
    basic_port_scanner()
