#!/usr/bin/env python3
import socket
import whois
import datetime

def check_domain(domain):
    try:
        ip = socket.gethostbyname(domain)
        w = whois.whois(domain)
        return {
            "Domain": domain,
            "IP": ip,
            "Registrar": w.registrar,
            "Created": str(w.creation_date),
            "Expiry": str(w.expiration_date),
        }
    except Exception as e:
        return {"Error": str(e)}

def format_date(d):
    if isinstance(d, list):
        return str(d[0]) if d else "N/A"
    return str(d) if d else "N/A"

def main():
    print("=" * 50)
    print("   DOMAIN CHECKER")
    print("=" * 50)
    
    domain = input("Domain (example.com): ")
    domain = domain.replace('http://', '').replace('https://', '').split('/')[0]
    
    result = check_domain(domain)
    
    for key, value in result.items():
        if key in ("Created", "Expiry"):
            value = format_date(value)
        print(f"{key}: {value}")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()