#!/usr/bin/env python3
import urllib.request
import json

CURRENT_VERSION = "1.0.0"
REPO_URL = "https://api.github.com/repos/werlist99/FreeTools-App/releases/latest"

def check_update():
    print(f"Current version: {CURRENT_VERSION}")
    print("Checking for updates...")
    try:
        with urllib.request.urlopen(REPO_URL, timeout=5) as resp:
            data = json.loads(resp.read())
            latest = data.get("tag_name", "").lstrip("v")
            if latest and latest > CURRENT_VERSION:
                print(f"New version available: {latest}")
                print(f"Download: {data.get('html_url', 'N/A')}")
            else:
                print("You are using the latest version!")
    except Exception:
        print("Could not check for updates (no internet or no release found).")
        print("You are using the latest version!")
    return True

def main():
    print("=" * 50)
    print("       UPDATER")
    print("=" * 50)
    
    check_update()
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()