#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

def list_directory(path="."):
    try:
        items = []
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                items.append(f"[DIR]  {item}")
            else:
                size = os.path.getsize(full_path)
                items.append(f"[FILE] {item} ({size} bytes)")
        return items
    except Exception as e:
        return [f"Error: {e}"]

def create_file(filepath, content=""):
    try:
        with open(filepath, 'w') as f:
            f.write(content)
        return True
    except Exception as e:
        return str(e)

def delete_item(path):
    try:
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)
        return True
    except Exception as e:
        return str(e)

def create_directory(path):
    try:
        os.makedirs(path, exist_ok=True)
        return True
    except Exception as e:
        return str(e)

def main():
    current_dir = os.getcwd()
    
    while True:
        print("\n" + "=" * 50)
        print(f"  FILE MANAGER - {current_dir}")
        print("=" * 50)
        print("\n1. List files")
        print("2. Create file")
        print("3. Create directory")
        print("4. Delete item")
        print("5. Change directory")
        print("6. Go to parent directory")
        print("0. Exit")
        
        choice = input("\nSelect: ")
        
        if choice == "1":
            items = list_directory(current_dir)
            print("\nFiles:")
            for item in items:
                print(f"  {item}")
            input("\nPress Enter...")
            
        elif choice == "2":
            filename = input("Filename: ")
            content = input("Content (optional): ")
            result = create_file(os.path.join(current_dir, filename), content)
            print("Created!" if result is True else f"Error: {result}")
            input("Press Enter...")
            
        elif choice == "3":
            dirname = input("Directory name: ")
            result = create_directory(os.path.join(current_dir, dirname))
            print("Created!" if result is True else f"Error: {result}")
            input("Press Enter...")
            
        elif choice == "4":
            name = input("Name to delete: ")
            result = delete_item(os.path.join(current_dir, name))
            print("Deleted!" if result is True else f"Error: {result}")
            input("Press Enter...")
            
        elif choice == "5":
            new_dir = input("New directory path: ")
            if os.path.isdir(new_dir):
                current_dir = os.path.abspath(new_dir)
            else:
                print("Directory not found!")
            input("Press Enter...")
            
        elif choice == "6":
            parent = os.path.dirname(current_dir)
            if parent != current_dir:
                current_dir = parent
            input("Press Enter...")
            
        elif choice == "0":
            break

if __name__ == "__main__":
    main()