"""
IX-Dade Core Module

Processes biology and medical queries, interfacing with IX-Gibson
through the GibsonAdapter to provide expert domain responses.
"""

from .gibson_adapter import GibsonAdapter

class DadeCore:
    def __init__(self):
        self.gibson = GibsonAdapter()

    def handle_query(self, query: str) -> str:
        """
        Send a medical or biology query to IX-Gibson and retrieve response.

        Args:
            query (str): User input related to biology or medicine.

        Returns:
            str: Response from IX-Gibson or error message.
        """
        response = self.gibson.query_gibson(query)
        if "error" in response:
            return f"[Dade Error] {response['error']}"
        return response.get("answer", "[Dade] No answer available.")
