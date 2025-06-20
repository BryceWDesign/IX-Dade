"""
IX-Dade Utility Functions

Provides support for text cleaning and input validation
for biomedical knowledge queries.
"""

import re

def normalize_query(text: str) -> str:
    """
    Clean and normalize user input query.
    """
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s\-]', '', text)
    return text.lower()

def is_valid_query(text: str) -> bool:
    """
    Basic validation to ensure query is non-empty and plausible.
    """
    return bool(text and len(text) > 5 and any(c.isalpha() for c in text))

# Example usage
if __name__ == "__main__":
    queries = [
        "   What is heart?? ",
        "",
        "??",
        "Tell me about neurons"
    ]
    for q in queries:
        cleaned = normalize_query(q)
        valid = is_valid_query(cleaned)
        print(f"Original: '{q}' | Cleaned: '{cleaned}' | Valid: {valid}")
