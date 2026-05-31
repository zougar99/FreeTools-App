#!/usr/bin/env python3
import urllib.request
import urllib.error
import socket

def check_url(url):
    if not url.startswith('http'):
        url = 'http://' + url
    
    try:
        response = urllib.request.urlopen(url, timeout=5)
        return f"Status: {response.status} OK"
    except urllib.error.HTTPError as e:
        return f"HTTP Error: {e.code} {e.reason}"
    except urllib.error.URLError as e:
        return f"URL Error: {e.reason}"
    except Exception as e:
        return f"Error: {e}"

def main():
    print("=" * 50)
    print("        URL CHECKER")
    print("=" * 50)
    
    url = input("Enter URL: ")
    
    result = check_url(url)
    print(f"\n{result}")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()