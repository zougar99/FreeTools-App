#!/usr/bin/env python3
import platform
import os
import socket
import sys

def get_system_info():
    info = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Python Version": sys.version,
        "Hostname": socket.gethostname(),
        "Current User": os.environ.get("USERNAME", os.environ.get("USER", "Unknown")),
        "Current Directory": os.getcwd(),
    }
    return info

def main():
    print("=" * 50)
    print("        SYSTEM INFORMATION")
    print("=" * 50)
    print()
    
    info = get_system_info()
    for key, value in info.items():
        print(f"{key:20}: {value}")
    
    print()
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()