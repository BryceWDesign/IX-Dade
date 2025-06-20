"""
IX-Dade CLI Interface

Command-line tool for querying biomedical knowledge
via the IX-Dade module.
"""

import sys
from core.query_processor import IXDadeQueryProcessor

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"What is [topic]\"")
        sys.exit(1)

    query = sys.argv[1]
    processor = IXDadeQueryProcessor()
    response = processor.process_query(query)

    print("\n🧠 IX-Dade Response 🧠")
    print(response)

if __name__ == "__main__":
    main()
