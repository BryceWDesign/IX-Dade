"""
IX-Dade CLI Interface

Provides an interactive command-line interface for biology and medical
queries routed through DadeCore to IX-Gibson.
"""

from core.dade_core import DadeCore

def run_dade_cli():
    core = DadeCore()
    print("IX-Dade — Biology and Medicine Specialist")
    print("Enter your queries below. Type 'exit' to quit.\n")

    while True:
        user_input = input("Dade> ").strip()
        if user_input.lower() in ("exit", "quit"):
            print("Exiting IX-Dade interface. Stay healthy.")
            break
        output = core.handle_query(user_input)
        print(f"→ {output}")

if __name__ == "__main__":
    run_dade_cli()
