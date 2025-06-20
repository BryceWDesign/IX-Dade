"""
IX-Dade Domain-Specific Query Processor

Processes user queries related to biology and medicine,
leveraging the core biology knowledge module.
"""

from biology_knowledge import BiologyKnowledge

class IXDadeQueryProcessor:
    def __init__(self):
        self.knowledge = BiologyKnowledge()

    def process_query(self, query: str) -> str:
        query_lower = query.lower()

        # Basic keyword matching to extract term for knowledge lookup
        # Very simple example: assume single-term queries or "what is" queries
        if query_lower.startswith("what is "):
            term = query_lower[8:].strip()
            return self.knowledge.get_fact(term)
        elif "tell me about" in query_lower:
            term = query_lower.split("tell me about")[-1].strip()
            return self.knowledge.get_fact(term)
        else:
            # Fallback generic answer
            return ("I'm IX-Dade, your biology and medical specialist AI. "
                    "Please ask me about biological terms or medical concepts.")

# Simple test
if __name__ == "__main__":
    processor = IXDadeQueryProcessor()
    print(processor.process_query("What is cell?"))
    print(processor.process_query("Tell me about mitochondria"))
    print(processor.process_query("Explain virus"))
