#!/usr/bin/env python3
from PIL import Image
import os

def get_image_info(filepath):
    try:
        img = Image.open(filepath)
        info = {
            "Format": img.format,
            "Mode": img.mode,
            "Size": f"{img.width} x {img.height}",
            "Aspect Ratio": f"{img.width/img.height:.2f}" if img.height > 0 else "N/A",
        }
        return info
    except Exception as e:
        return {"Error": str(e)}

def main():
    print("=" * 50)
    print("       IMAGE INFO")
    print("=" * 50)
    
    filepath = input("Image file path: ")
    
    if not os.path.exists(filepath):
        print("File not found!")
        input("Press Enter to exit...")
        return
    
    info = get_image_info(filepath)
    
    print("\nImage Information:")
    for key, value in info.items():
        print(f"  {key}: {value}")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()