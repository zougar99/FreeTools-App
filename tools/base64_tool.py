#!/usr/bin/env python3
import base64

def encode_base64(text):
    try:
        return base64.b64encode(text.encode('utf-8')).decode('utf-8')
    except Exception as e:
        return f"Error: {e}"

def decode_base64(text):
    try:
        return base64.b64decode(text.encode('utf-8')).decode('utf-8')
    except Exception as e:
        return f"Error: {e}"

def main():
    print("=" * 50)
    print("    BASE64 ENCODER/DECODER")
    print("=" * 50)
    
    print("\n1. Encode")
    print("2. Decode")
    
    choice = input("\nSelect: ")
    
    text = input("Enter text: ")
    
    if choice == "1":
        result = encode_base64(text)
    elif choice == "2":
        result = decode_base64(text)
    else:
        result = "Invalid option"
    
    print(f"\nResult:\n{result}")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()