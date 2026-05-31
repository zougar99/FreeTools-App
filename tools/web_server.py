#!/usr/bin/env python3
import http.server
import socketserver
import os

PORT = 8000

def start_server(port=PORT, directory="."):
    original_dir = os.getcwd()
    os.chdir(directory)
    
    handler = http.server.SimpleHTTPRequestHandler
    handler.extensions_map.update({
        '.wasm': 'application/wasm',
    })
    
    print(f"Starting server on port {port}")
    print(f"Serving directory: {os.getcwd()}")
    print(f"Open http://localhost:{port} in your browser")
    print("Press Ctrl+C to stop")
    
    try:
        with socketserver.TCPServer(("", port), handler) as httpd:
            httpd.serve_forever()
    finally:
        os.chdir(original_dir)

def main():
    print("=" * 50)
    print("        WEB SERVER")
    print("=" * 50)
    
    port_input = input(f"Port (default {PORT}): ")
    try:
        port = int(port_input) if port_input else PORT
    except ValueError:
        port = PORT
    
    dir_input = input("Directory (default current): ")
    directory = dir_input if dir_input else "."
    
    try:
        start_server(port, directory)
    except KeyboardInterrupt:
        print("\nServer stopped.")

if __name__ == "__main__":
    main()