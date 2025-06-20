"""
IX-Dade Query Processor

Handles biomedical query interpretation and retrieval
from the biomedical knowledge base.
"""

from core.biomed_knowledge import BiomedicalKnowledge

class IXDadeQueryProcessor:
    def __init__(self):
        self.biomed = BiomedicalKnowledge()

    def process_query(self, query: str) -> str:
        query_lower = query.lower().strip()

        if query_lower.startswith("what is") or query_lower.startswith("tell me about"):
            # Extract topic after the phrase
            topic = query_lower.replace("what is", "").replace("tell me about", "").strip()
            if not topic:
                return "Please specify a biomedical topic to look up."
            info = self.biomed.get_info(topic)
            if "error" in info:
                return info["error"]
            details = (
                f"Function: {info.get('function', 'N/A')}\n"
                f"Components: {', '.join(info.get('components', []))}\n"
                f"Common Diseases: {', '.join(info.get('common_diseases', []))}"
            )
            return details
        else:
            return (
                "IX-Dade specializes in biomedical knowledge. "
                "Try asking 'What is [topic]' or 'Tell me about [topic]'."
            )

# Standalone test
if __name__ == "__main__":
    qp = IXDadeQueryProcessor()
    print(qp.process_query("What is heart"))
    print(qp.process_query("Tell me about brain"))
    print(qp.process_query("Explain lung"))
