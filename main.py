#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent

TOOLS = {
    "1": ("System Info", "tools/system_info.py", "Get system information"),
    "2": ("File Manager", "tools/file_manager.py", "Manage files and directories"),
    "3": ("Scanner", "tools/scanner.py", "Network/Directory scanner"),
    "4": ("Web Server", "tools/web_server.py", "Simple HTTP server"),
    "5": ("Archive Extractor", "tools/archive_extractor.py", "Extract archives"),
    "6": ("Password Generator", "tools/password_gen.py", "Generate secure passwords"),
    "7": ("URL Checker", "tools/url_checker.py", "Check URL validity"),
    "8": ("JSON Formatter", "tools/json_formatter.py", "Format JSON data"),
    "9": ("Base64 Encoder/Decoder", "tools/base64_tool.py", "Encode/decode Base64"),
    "10": ("Hash Generator", "tools/hash_gen.py", "Generate hash from text"),
    "11": ("CSV Viewer", "tools/csv_viewer.py", "View CSV files"),
    "12": ("Image Info", "tools/image_info.py", "Get image metadata"),
    "13": ("Notes", "tools/notes.py", "Take notes"),
    "14": ("Contact Manager", "tools/contact_manager.py", "Manage contacts"),
    "15": ("Automation", "tools/automation.py", "Run automated tasks"),
    "16": ("Stats", "tools/stats.py", "Statistics and analytics"),
    "17": ("Logger", "tools/logger.py", "Logging utility"),
    "18": ("Config Editor", "tools/config_editor.py", "Edit config files"),
    "19": ("Validators", "tools/validators.py", "Validate data formats"),
    "20": ("Updater", "tools/updater.py", "Check for updates"),
    "21": ("Wordlist Generator", "tools/wordlist_gen.py", "Generate wordlists"),
    "22": ("Weather", "tools/weather.py", "Check weather"),
    "23": ("Text Tools", "tools/text_tools.py", "Text manipulation"),
    "24": ("Domain Checker", "tools/domain_checker.py", "Check domain info"),
    "25": ("QR Code Generator", "tools/qrcode_gen.py", "Generate QR codes"),
}

CATEGORIES = {
    "System": ["1", "16", "20"],
    "Files": ["2", "5", "11", "12", "18"],
    "Network": ["3", "4", "7", "24"],
    "Security": ["6", "10"],
    "Data": ["8", "9", "19"],
    "Productivity": ["13", "14", "15", "17"],
    "Utilities": ["21", "22", "23", "25"],
}

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.columns import Columns
    from rich.text import Text
    from rich import box
    HAS_RICH = True
    con = Console()
except ImportError:
    HAS_RICH = False

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    if HAS_RICH:
        title = Text("FREE TOOLS APPLICATION v1.0", style="bold cyan")
        con.print(Panel(title, box=box.DOUBLE_EDGE, border_style="cyan"))
        con.print()
    else:
        print("=" * 60)
        print("              FREE TOOLS APPLICATION v1.0")
        print("=" * 60)
        print()

def print_menu():
    if HAS_RICH:
        table = Table(show_header=True, header_style="bold magenta", box=box.SIMPLE)
        table.add_column("Key", style="dim", width=6)
        table.add_column("Tool", width=22)
        table.add_column("Description")
        for key, (name, _, desc) in TOOLS.items():
            table.add_row(f"[{key}]", name, desc)
        con.print(table)
        con.print("\n[bold yellow][0][/] Exit", highlight=False)
        con.print()
    else:
        print("Available Tools:")
        print("-" * 60)
        for key, (name, _, desc) in TOOLS.items():
            print(f"  [{key}] {name:20} - {desc}")
        print("-" * 60)
        print("  [0] Exit")
        print()

def print_menu_categorized():
    if not HAS_RICH:
        print_menu()
        return

    table = Table(show_header=True, header_style="bold magenta", box=box.SIMPLE)
    table.add_column("Key", style="dim", width=6)
    table.add_column("Tool", width=22)
    table.add_column("Description")
    current = None
    for key, (name, _, desc) in TOOLS.items():
        for cat, keys in CATEGORIES.items():
            if key in keys:
                if cat != current:
                    table.add_section()
                    table.add_row(f"[bold cyan]{cat}[/]", "", "", style="bold cyan")
                    current = cat
                break
        table.add_row(f"[{key}]", name, desc)
    con.print(table)
    con.print("\n[bold yellow][0][/] Exit", highlight=False)
    con.print()

def run_tool(tool_path):
    if not os.path.exists(tool_path):
        if HAS_RICH:
            con.print(f"[red]Error: Tool not found at {tool_path}[/]")
        else:
            print(f"Error: Tool not found at {tool_path}")
        input("Press Enter to continue...")
        return

    script_dir = os.path.dirname(os.path.abspath(__file__))
    tool_abs_path = os.path.join(script_dir, tool_path)

    try:
        subprocess.run([sys.executable, tool_abs_path])
    except Exception as e:
        if HAS_RICH:
            con.print(f"[red]Error running tool: {e}[/]")
        else:
            print(f"Error running tool: {e}")
        input("Press Enter to continue...")

def main():
    while True:
        clear_screen()
        print_banner()
        print_menu_categorized()

        choice = input("Select a tool: ").strip()

        if choice == '0':
            if HAS_RICH:
                con.print("\n[bold green]Goodbye![/]")
            else:
                print("\nGoodbye!")
            break
        elif choice in TOOLS:
            _, tool_path, _ = TOOLS[choice]
            clear_screen()
            if HAS_RICH:
                con.print(f"[bold cyan]Running: {TOOLS[choice][0]}...[/]")
                con.print("─" * 40)
            else:
                print(f"Running: {TOOLS[choice][0]}...")
                print("-" * 40)
            run_tool(tool_path)
        else:
            if HAS_RICH:
                con.print("\n[red]Invalid selection![/]")
            else:
                print("\nInvalid selection!")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()