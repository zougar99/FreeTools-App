#!/usr/bin/env python3
import hashlib
import os

def generate_hash(text, algorithm='sha256'):
    try:
        hash_obj = hashlib.new(algorithm)
        hash_obj.update(text.encode('utf-8'))
        return hash_obj.hexdigest()
    except ValueError as e:
        return f"Error: {e}"

def main():
    print("=" * 50)
    print("       HASH GENERATOR")
    print("=" * 50)
    
    text = input("Enter text: ")
    
    print("\nAlgorithm:")
    print("1. MD5")
    print("2. SHA1")
    print("3. SHA256")
    print("4. SHA512")
    
    choice = input("\nSelect: ")
    algos = {'1': 'md5', '2': 'sha1', '3': 'sha256', '4': 'sha512'}
    algorithm = algos.get(choice, 'sha256')
    
    result = generate_hash(text, algorithm)
    print(f"\n{algorithm.upper()} Hash:")
    print(result)
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()