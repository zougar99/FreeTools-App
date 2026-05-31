#!/usr/bin/env python3
import os

def get_directory_stats(directory="."):
    stats = {
        "total_files": 0,
        "total_dirs": 0,
        "total_size": 0,
        "file_types": {},
    }
    
    for root, dirs, files in os.walk(directory):
        stats["total_dirs"] += len(dirs)
        for file in files:
            stats["total_files"] += 1
            filepath = os.path.join(root, file)
            try:
                size = os.path.getsize(filepath)
                stats["total_size"] += size
                ext = os.path.splitext(file)[1] or "no_ext"
                stats["file_types"][ext] = stats["file_types"].get(ext, 0) + 1
            except OSError:
                pass
    
    return stats

def format_size(size):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"

def main():
    print("=" * 50)
    print("       STATISTICS")
    print("=" * 50)
    
    directory = input("Directory (default current): ") or "."
    
    stats = get_directory_stats(directory)
    
    print(f"\nTotal Files: {stats['total_files']}")
    print(f"Total Directories: {stats['total_dirs']}")
    print(f"Total Size: {format_size(stats['total_size'])}")
    print("\nFile Types:")
    for ext, count in sorted(stats['file_types'].items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  {ext}: {count}")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()