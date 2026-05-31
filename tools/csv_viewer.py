#!/usr/bin/env python3
import csv
import os

def read_csv(filepath, max_rows=50):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = []
            for i, row in enumerate(reader):
                if i >= max_rows:
                    break
                rows.append(row)
            return rows
    except Exception as e:
        return [["Error", str(e)]]

def main():
    print("=" * 50)
    print("       CSV VIEWER")
    print("=" * 50)
    
    filepath = input("CSV file path: ")
    
    if not os.path.exists(filepath):
        print("File not found!")
        input("Press Enter to exit...")
        return
    
    rows = read_csv(filepath)
    
    print(f"\nShowing {len(rows)} rows:\n")
    for i, row in enumerate(rows):
        print(" | ".join(row))
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()