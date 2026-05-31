#!/usr/bin/env python3
import re

def to_uppercase(text):
    return text.upper()

def to_lowercase(text):
    return text.lower()

def reverse_text(text):
    return text[::-1]

def word_count(text):
    return len(text.split())

def char_count(text):
    return len(text)

def remove_spaces(text):
    return re.sub(r'\s+', '', text)

def main():
    print("=" * 50)
    print("      TEXT TOOLS")
    print("=" * 50)
    
    text = input("Enter text: ")
    
    print("\n1. UPPERCASE")
    print("2. lowercase")
    print("3. Reverse")
    print("4. Word count")
    print("5. Character count")
    print("6. Remove spaces")
    
    choice = input("\nSelect: ")
    
    tools = {
        '1': (to_uppercase, "UPPERCASE"),
        '2': (to_lowercase, "lowercase"),
        '3': (reverse_text, "Reversed"),
        '4': (word_count, "Words"),
        '5': (char_count, "Characters"),
        '6': (remove_spaces, "No spaces"),
    }
    
    if choice in tools:
        func, name = tools[choice]
        result = func(text)
        print(f"\n{name}: {result}")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()