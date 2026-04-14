"""
Handles the nucleotide base sequence.
"""
class DNASequence:
    def __init__(self, sequence):
        self.sequence = sequence.upper()
        self.validate_sequence()

    def validate_sequence(self):
        valid_bases = set('ATCG')
        if not all(base in valid_bases for base in self.sequence):
            raise ValueError("Invalid sequence: only A, T, C, and G are allowed.")
    def get_complementary(self):
        comp = {'A':'T','T':'A','C':'G','G':'C'}
        return ''.join(comp[base] for base in self.sequence)