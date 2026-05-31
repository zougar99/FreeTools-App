#!/usr/bin/env python3
import os
import subprocess
import time

TASKS_FILE = "tasks.txt"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        for task in tasks:
            f.write(task + '\n')

def run_task(command):
    try:
        confirm = input(f"Run command '{command}'? (y/n): ")
        if confirm.lower() != 'y':
            return "Cancelled."
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else result.stderr
    except Exception as e:
        return str(e)

def main():
    print("=" * 50)
    print("      AUTOMATION TOOL")
    print("=" * 50)
    
    tasks = load_tasks()
    
    while True:
        print("\n1. Add task")
        print("2. List tasks")
        print("3. Run task")
        print("4. Delete task")
        print("0. Exit")
        
        choice = input("\nSelect: ")
        
        if choice == "1":
            task = input("Command to run: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Added!")
        elif choice == "2":
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        elif choice == "3":
            try:
                idx = int(input("Task number: ")) - 1
                if 0 <= idx < len(tasks):
                    print(f"Running: {tasks[idx]}")
                    result = run_task(tasks[idx])
                    print(result)
            except ValueError:
                print("Invalid number!")
        elif choice == "4":
            try:
                idx = int(input("Task number: ")) - 1
                if 0 <= idx < len(tasks):
                    tasks.pop(idx)
                    save_tasks(tasks)
                    print("Deleted!")
            except ValueError:
                print("Invalid number!")
        elif choice == "0":
            break
    
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()