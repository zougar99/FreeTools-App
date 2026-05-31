#!/usr/bin/env python3
import os
import socket

def scan_ports(host, ports=None):
    if ports is None:
        ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 993, 995, 3306, 3389, 5432, 8080, 8443]
    
    print(f"Scanning {host}...")
    print("-" * 40)
    
    open_ports = []
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
                print(f"Port {port}: OPEN")
            sock.close()
        except Exception as e:
            print(f"  Port {port}: Error - {e}")
    
    return open_ports

def scan_local_files(directory=".", extension=None):
    print(f"Scanning directory: {directory}")
    print("-" * 40)
    
    files = []
    try:
        for root, dirs, filenames in os.walk(directory):
            for filename in filenames:
                if extension is None or filename.endswith(extension):
                    filepath = os.path.join(root, filename)
                    files.append(filepath)
                    print(filepath)
    except Exception as e:
        print(f"Error: {e}")
    
    return files

def main():
    print("=" * 50)
    print("        SCANNER TOOL")
    print("=" * 50)
    print("\n1. Scan ports (network)")
    print("2. Scan local files")
    
    choice = input("\nSelect: ")
    
    if choice == "1":
        host = input("Host (e.g., localhost or IP): ")
        scan_ports(host)
    elif choice == "2":
        directory = input("Directory (or press Enter for current): ")
        ext = input("File extension (e.g., .py, or Enter for all): ")
        scan_local_files(directory if directory else ".", ext if ext else None)
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()