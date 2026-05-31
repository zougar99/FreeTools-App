#!/usr/bin/env python3
import itertools
import os

def generate_wordlist(chars, min_len, max_len, output_file):
    with open(output_file, 'w') as f:
        for length in range(min_len, max_len + 1):
            for combo in itertools.product(chars, repeat=length):
                f.write(''.join(combo) + '\n')
    return "Generated!"

def main():
    print("=" * 50)
    print("   WORDLIST GENERATOR")
    print("=" * 50)
    
    chars = input("Characters (default abc123): ") or "abc123"
    try:
        min_len = int(input("Min length (default 1): ") or 1)
        if min_len < 1:
            min_len = 1
    except ValueError:
        min_len = 1
    try:
        max_len = int(input("Max length (default 3): ") or 3)
        if max_len < min_len:
            max_len = min_len
    except ValueError:
        max_len = min_len
    output = input("Output file: ")
    
    if not output:
        print("Output file required!")
        return
    
    total = sum(len(chars) ** i for i in range(min_len, max_len + 1))
    if total > 100_000_000:
        confirm = input(f"WARNING: This will generate ~{total:,} entries (large file). Continue? (y/n): ")
        if confirm.lower() != 'y':
            print("Cancelled.")
            return
    elif total > 10_000:
        print(f"Note: Generating ~{total:,} entries...")
    
    print("\nGenerating...")
    result = generate_wordlist(chars, min_len, max_len, output)
    print(result)
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()