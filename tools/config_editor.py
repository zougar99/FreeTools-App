#!/usr/bin/env python3
import os

def read_config(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error: {e}"

def write_config(filepath, content):
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return "Saved!"
    except Exception as e:
        return f"Error: {e}"

def main():
    print("=" * 50)
    print("    CONFIG EDITOR")
    print("=" * 50)
    
    filepath = input("Config file path: ")
    
    if not os.path.exists(filepath):
        print("File not found. Create new? (y/n)")
        if input().lower() != 'y':
            return
        content = ""
    else:
        content = read_config(filepath)
        print(f"\nCurrent content:\n{content}")
    
    print("\nEnter new content (type 'EOF' on a new line to save and exit):")
    lines = []
    while True:
        line = input()
        if line == "EOF":
            break
        lines.append(line)
    
    result = write_config(filepath, '\n'.join(lines))
    print(result)
    
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()