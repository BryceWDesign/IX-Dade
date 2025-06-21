"""
IX-Dade Core Module

Processes user medical queries and retrieves
relevant information from the medical knowledge base.
"""

import json
from .config.dade_config import MEDICAL_KNOWLEDGE_BASE_PATH, MAX_MEDICAL_QUERY_LENGTH
from .utils.text_utils import normalize_text, tokenize

class DadeCore:
    def __init__(self):
        # Load medical knowledge base from JSON file
        with open(MEDICAL_KNOWLEDGE_BASE_PATH, 'r', encoding='utf-8') as file:
            self.knowledge_base = json.load(file)

    def process_query(self, query: str) -> str:
        """
        Process a medical query string and return
        relevant medical information.

        Args:
            query (str): User input medical question or symptom description.

        Returns:
            str: Retrieved medical information or fallback message.
        """
        if len(query) > MAX_MEDICAL_QUERY_LENGTH:
            return "Your query is too long. Please shorten it."

        normalized_query = normalize_text(query)
        tokens = tokenize(normalized_query)

        # Simple keyword matching for demo purposes
        for token in tokens:
            if token in self.knowledge_base:
                return self.knowledge_base[token]

        return "Sorry, I couldn't find information on that topic. Please consult a healthcare professional."
