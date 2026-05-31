#!/usr/bin/env python3
import os

NOTES_FILE = "notes.txt"

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

def save_notes(content):
    with open(NOTES_FILE, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    print("=" * 50)
    print("         NOTES")
    print("=" * 50)
    
    content = load_notes()
    print("Current notes:\n")
    print(content if content else "(No notes)")
    print("\n" + "=" * 50)
    
    print("\n1. Edit notes")
    print("2. Clear notes")
    print("0. Exit")
    
    choice = input("\nSelect: ")
    
    if choice == "1":
        print("Enter new notes (type 'END' on a new line to finish):")
        lines = []
        while True:
            line = input()
            if line.strip() == "END":
                break
            lines.append(line)
        new_content = "\n".join(lines)
        save_notes(new_content)
        print("Saved!")
    elif choice == "2":
        save_notes("")
        print("Cleared!")
    
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()