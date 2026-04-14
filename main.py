import matplotlib

import matplotlib.pyplot as plt

from dna_helix_geometry import DNAHelixGeometry
from dna_sequence import DNASequence
from dna_visualizer import DNAVisualizer

if __name__ == "__main__":
    sequence = DNASequence("ATGCGTACGTAGCTAGCTAGATGATCGATCGTACGTAGCTAGCTAGCTAGCTAGCTAGC")
    geometry = DNAHelixGeometry(n_bases=len(sequence.sequence))
    visualizer = DNAVisualizer(geometry, sequence)
    visualizer.plot()
