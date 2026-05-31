#!/usr/bin/env python3
import json
import os

def format_json(data, indent=2):
    try:
        if isinstance(data, str):
            data = json.loads(data)
        return json.dumps(data, indent=indent, ensure_ascii=False)
    except json.JSONDecodeError as e:
        return f"Invalid JSON: {e}"
    except Exception as e:
        return f"Error: {e}"

def main():
    print("=" * 50)
    print("     JSON FORMATTER")
    print("=" * 50)
    
    print("\n1. Input JSON string")
    print("2. Load from file")
    
    choice = input("\nSelect: ")
    
    if choice == "1":
        json_str = input("\nEnter JSON: ")
        result = format_json(json_str)
        print(f"\n{result}")
        
        save = input("\nSave to file? (y/n): ").lower()
        if save == 'y':
            filename = input("Filename: ")
            if os.path.exists(filename):
                confirm = input(f"File {filename} exists. Overwrite? (y/n): ")
                if confirm.lower() != 'y':
                    print("Cancelled.")
                    return
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(result)
            print("Saved!")
            
    elif choice == "2":
        filepath = input("File path: ")
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            print(format_json(data))
        except Exception as e:
            print(f"Error: {e}")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()