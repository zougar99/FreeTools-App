#!/usr/bin/env python3
import os
from datetime import datetime

LOG_FILE = "app.log"

def log_message(message, level="INFO"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{level}] {message}"
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(log_entry + '\n')

def read_logs():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            return f.read()
    return "No logs yet."

def main():
    print("=" * 50)
    print("        LOGGER TOOL")
    print("=" * 50)
    
    while True:
        print("\n1. Add log entry")
        print("2. View logs")
        print("3. Clear logs")
        print("0. Exit")
        
        choice = input("\nSelect: ")
        
        if choice == "1":
            msg = input("Message: ")
            print("1. INFO  2. WARNING  3. ERROR")
            lvl = input("Level (1-3): ")
            levels = {'1': 'INFO', '2': 'WARNING', '3': 'ERROR'}
            log_message(msg, levels.get(lvl, 'INFO'))
            print("Logged!")
        elif choice == "2":
            print(read_logs())
        elif choice == "3":
            with open(LOG_FILE, 'w') as f:
                pass
            print("Cleared!")
        elif choice == "0":
            break
    
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()