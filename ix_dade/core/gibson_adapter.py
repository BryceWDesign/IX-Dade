"""
IX-Dade Gibson Adapter

Handles communication with IX-Gibson, enabling biology and medicine
queries to be sent and results received.
"""

import requests
import time
from config.gibson_config import GIBSON_API_URL, REQUEST_TIMEOUT_SECONDS, RETRY_ATTEMPTS, RETRY_BACKOFF_SECONDS

class GibsonAdapter:
    def __init__(self):
        self.endpoint = GIBSON_API_URL
        self.timeout = REQUEST_TIMEOUT_SECONDS
        self.retries = RETRY_ATTEMPTS
        self.backoff = RETRY_BACKOFF_SECONDS

    def query_gibson(self, query: str) -> dict:
        """
        Send a query to IX-Gibson and return the JSON response.

        Args:
            query (str): The biological or medical query string.

        Returns:
            dict: Parsed JSON response or error.
        """
        payload = {
            "domain": "dade",
            "query": query,
            "source": "ix-dade"
        }
        for attempt in range(1, self.retries + 1):
            try:
                response = requests.post(self.endpoint, json=payload, timeout=self.timeout)
                if response.status_code == 200:
                    return response.json()
                else:
                    print(f"[Dade HTTP {response.status_code}] {response.text}")
            except requests.RequestException as e:
                print(f"[Dade] Gibson request error (attempt {attempt}): {e}")

            if attempt < self.retries:
                time.sleep(self.backoff)

        return {"error": "Failed to retrieve response from IX-Gibson after retries."}
