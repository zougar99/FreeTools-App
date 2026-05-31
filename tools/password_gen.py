#!/usr/bin/env python3
import secrets
import string

def generate_password(length=16, include_special=True):
    chars = string.ascii_letters + string.digits
    if include_special:
        chars += string.punctuation
    
    return ''.join(secrets.choice(chars) for _ in range(length))

def main():
    print("=" * 50)
    print("    PASSWORD GENERATOR")
    print("=" * 50)
    
    length_input = input("Password length (default 16): ")
    try:
        length = int(length_input) if length_input else 16
        if length < 1:
            length = 16
    except ValueError:
        length = 16
    
    use_special = input("Include special characters? (y/n, default y): ").lower() != 'n'
    
    password = generate_password(length, use_special)
    
    print(f"\nGenerated Password: {password}")
    print(f"Length: {len(password)}")
    
    save = input("\nSave to file? (y/n): ").lower()
    if save == 'y':
        filename = input("Filename: ")
        with open(filename, 'w') as f:
            f.write(password)
        print("Saved!")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()