"""
IX-Dade Core Module

Handles loading and querying specialized biology and medicine knowledge bases,
serving as the medical reasoning engine for IX-Gibson system.
"""

import json
from typing import Optional

class DadeCore:
    def __init__(self, knowledge_base_path: str):
        """
        Initialize DadeCore with path to the medical knowledge base JSON.

        Args:
            knowledge_base_path (str): Path to medical knowledge JSON file.
        """
        self.knowledge_base_path = knowledge_base_path
        self.knowledge_base = self._load_knowledge_base()

    def _load_knowledge_base(self) -> dict:
        """
        Load medical knowledge base JSON into memory.

        Returns:
            dict: Loaded medical knowledge data.
        """
        try:
            with open(self.knowledge_base_path, 'r', encoding='utf-8') as kb_file:
                data = json.load(kb_file)
            return data
        except FileNotFoundError:
            print(f"Knowledge base file not found at {self.knowledge_base_path}")
            return {}
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {self.knowledge_base_path}")
            return {}

    def query(self, question: str) -> Optional[str]:
        """
        Basic keyword search query interface against loaded knowledge base.

        Args:
            question (str): User question string.

        Returns:
            Optional[str]: Best matched answer or None if not found.
        """
        question = question.lower()
        for key, answer in self.knowledge_base.items():
            if key.lower() in question:
                return answer
        return None
