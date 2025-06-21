"""
Text processing utilities for IX-Dade

Includes functions for cleaning, normalizing, and tokenizing
medical domain user queries to improve matching accuracy.
"""

import re

def normalize_text(text: str) -> str:
    """
    Normalize input text by lowercasing and removing
    punctuation and extra whitespace.

    Args:
        text (str): Raw input text.

    Returns:
        str: Normalized text.
    """
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def tokenize(text: str) -> list[str]:
    """
    Tokenize normalized text into a list of word tokens.

    Args:
        text (str): Normalized text string.

    Returns:
        list[str]: List of tokens.
    """
    return text.split()
