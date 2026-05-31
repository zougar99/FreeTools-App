#!/usr/bin/env python3
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email)) and len(email) <= 254

def validate_phone(phone):
    pattern = r'^\+?[\d\s\-\(\)]{10,}$'
    return bool(re.match(pattern, phone))

def validate_url(url):
    pattern = r'^https?://[^\s]+$'
    return bool(re.match(pattern, url))

def validate_ip(ip):
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if not re.match(pattern, ip):
        return False
    parts = ip.split('.')
    for p in parts:
        # Reject leading zeros (except single zero)
        if len(p) > 1 and p[0] == '0':
            return False
        if not (0 <= int(p) <= 255):
            return False
    return True

def main():
    print("=" * 50)
    print("      VALIDATORS")
    print("=" * 50)
    
    print("\n1. Email")
    print("2. Phone")
    print("3. URL")
    print("4. IP Address")
    
    choice = input("\nSelect type: ")
    value = input("Enter value: ")
    
    validators = {
        '1': (validate_email, "Email"),
        '2': (validate_phone, "Phone"),
        '3': (validate_url, "URL"),
        '4': (validate_ip, "IP"),
    }
    
    if choice in validators:
        func, name = validators[choice]
        result = func(value)
        print(f"\n{name} is {'VALID' if result else 'INVALID'}")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()