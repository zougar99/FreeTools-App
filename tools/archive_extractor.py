#!/usr/bin/env python3
import zipfile
import tarfile
import os

def extract_zip(filepath, destination="."):
    try:
        with zipfile.ZipFile(filepath, 'r') as zip_ref:
            for member in zip_ref.namelist():
                dest_path = os.path.abspath(os.path.join(destination, member))
                if not dest_path.startswith(os.path.abspath(destination)):
                    return f"Error: Path traversal detected in archive ({member})"
            zip_ref.extractall(destination)
        return "Extracted successfully!"
    except Exception as e:
        return f"Error: {e}"

def extract_tar(filepath, destination="."):
    try:
        with tarfile.open(filepath, 'r:*') as tar:
            for member in tar.getmembers():
                dest_path = os.path.abspath(os.path.join(destination, member.name))
                if not dest_path.startswith(os.path.abspath(destination)):
                    return f"Error: Path traversal detected in archive ({member.name})"
            tar.extractall(destination)
        return "Extracted successfully!"
    except Exception as e:
        return f"Error: {e}"

def extract_archive(filepath, destination="."):
    if not os.path.exists(filepath):
        return f"Error: File not found: {filepath}"
    ext = os.path.splitext(filepath)[1].lower()
    if ext in ['.zip']:
        return extract_zip(filepath, destination)
    elif ext in ['.tar', '.gz', '.bz2', '.xz']:
        return extract_tar(filepath, destination)
    else:
        return "Unsupported format"

def main():
    print("=" * 50)
    print("    ARCHIVE EXTRACTOR")
    print("=" * 50)
    
    filepath = input("Archive file path: ")
    dest = input("Destination (default .): ") or "."
    
    result = extract_archive(filepath, dest)
    print(result)
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()