"""
IX-Dade Core Biology Knowledge Module

Provides curated biology and medicine knowledge,
including human anatomy, cellular biology, genetics,
and common medical concepts.

Designed for modular integration with IX-Gibson.
"""

class BiologyKnowledge:
    def __init__(self):
        # Core static biological facts and definitions
        self.facts = {
            "cell": "The basic structural, functional, and biological unit of all known living organisms.",
            "dna": "Deoxyribonucleic acid, the carrier of genetic information in most living organisms.",
            "mitochondria": "Organelles known as the powerhouse of the cell, generating most of the cell's supply of ATP.",
            "anatomy": "The branch of science concerned with the bodily structure of humans, animals, and other living organisms.",
            "virus": "A small infectious agent that replicates only inside the living cells of an organism.",
            "gene": "A sequence of DNA that codes for a molecule that has a function.",
            "medicine": "The science and practice of the diagnosis, treatment, and prevention of disease."
        }

    def get_fact(self, term: str) -> str:
        """
        Retrieve a fact or definition for a given biological term.
        """
        term_lower = term.lower()
        return self.facts.get(term_lower, f"Sorry, I don't have information on '{term}' yet.")

# Simple test
if __name__ == "__main__":
    bk = BiologyKnowledge()
    print(bk.get_fact("Cell"))
    print(bk.get_fact("DNA"))
    print(bk.get_fact("Heart"))
