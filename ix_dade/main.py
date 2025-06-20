"""
IX-Dade CLI Entry Point

Allows direct command-line queries to IX-Dade’s biology and medicine AI.
Prints responses to terminal.
"""

import sys
from core.query_processor import IXDadeQueryProcessor

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"Your biology or medical question here\"")
        sys.exit(1)

    query = sys.argv[1]
    processor = IXDadeQueryProcessor()
    response = processor.process_query(query)

    print("\n🧬 IX-Dade Response 🧬")
    print(response)

if __name__ == "__main__":
    main()
