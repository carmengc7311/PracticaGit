
import numpy as np


DNA_CONFIG = {
    'bases_per_turn': 10.5,
    'z_step': 0.34,
    'radius': 1.0,
    'angle_step': 0.6,
    'strand_offset': 2 * np.pi / 3,
    'smooth_per_base': 10,
}


class DNAHelixGeometry:
    def __init__(self, n_bases, config=None):
        if config is None:
            config = DNA_CONFIG
        self.config = dict(config)
        try:
            self.n_bases = max(1, int(n_bases))
        except Exception:
            self.n_bases = 10

        self.n_turns = float(self.n_bases) / float(self.config.get('bases_per_turn', 10.5))

        self.helix1 = []
        self.helix2 = []
        self.base_pairs = []

        self.calculate_geometry()

    def calculate_geometry(self):
        """Orchestrates the calculation (placeholder implemented for the exercise)."""
        self._calculate_strands()
        self._calculate_base_pairs()

    def _calculate_strands(self):
        # TODO
        cfg = self.config
        z_step = float(cfg.get('z_step', 0.34))
        r = float(cfg.get('radius', 1.0))

        total_z = self.n_bases * z_step

        # Two points per strand (vertical line) — sufficient for the visualizer to display lines
        self.helix1 = [(r, 0.0, 0.0), (r, 0.0, total_z)]
        self.helix2 = [(-r, 0.0, 0.0), (-r, 0.0, total_z)]

    def _calculate_base_pairs(self):
        # TODO
        cfg = self.config
        z_step = float(cfg.get('z_step', 0.34))
        r = float(cfg.get('radius', 1.0))

        # Create up to 5 pairs spaced along the Z axis to show progress
        n_display = min(5, max(1, self.n_bases))
        self.base_pairs = []
        for i in range(n_display):
            z = i * (self.n_bases * z_step) / max(1, n_display - 1) if n_display > 1 else 0.0
            p1 = (r, 0.0, z)
            p2 = (-r, 0.0, z)
            self.base_pairs.append((p1, p2))

