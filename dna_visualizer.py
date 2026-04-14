"""
Visualizes the double helix in interactive 3D (rotate and zoom with the mouse).
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


class DNAVisualizer:
    def __init__(self, geometry, sequence):
        # TODO
        self.geometry = geometry
        self.sequence = sequence
        # Base colors — default behavior for the skeleton
        self.base_colors = {'A': 'green', 'T': 'yellow', 'C': 'cyan', 'G': 'magenta'}

    def _create_3d_axes(self):
        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(111, projection='3d')
        return fig, ax

    def _plot_strand(self, ax, helix, outer_color, inner_color, label):
        # TODO
        x_vals, y_vals, z_vals = zip(*helix)
        ax.plot(
            x_vals,
            y_vals,
            z_vals,
            color=inner_color,
            linewidth=3.2,
            solid_capstyle='round',
            label=label,
        )

    def _plot_helices(self, ax):
        # TODO
        helix1 = []
        if self.geometry:
            helix1 = getattr(self.geometry, 'helix1', []) or []

        self._plot_strand(ax, helix1, outer_color='#93c5fd', inner_color='#2563eb', label='Helix 1')

    def _plot_base_pairs(self, ax):
        # TODO
        # Use provided sequence and geometry to draw base-pair connectors and a midpoint marker.
        seq = getattr(self.sequence, 'sequence', '') if self.sequence is not None else ''
        complementary_seq = self.sequence.get_complementary()

        base_pairs = self.geometry.base_pairs
        for i, pair in enumerate(base_pairs):
            (x1, y1, z1), (x2, y2, z2) = pair
            base = seq[i % len(seq)] if seq else None
            color = self.base_colors.get(base, 'gray')
            ax.plot([x1, x2], [y1, y2], [z1, z2], color=color, linewidth=3, alpha=0.9)
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2
            mid_z = (z1 + z2) / 2
            ax.scatter([mid_x], [mid_y], [mid_z], color=color, s=20)

    def _configure_axes(self, ax):
        # TODO: configure axis labels, limits and viewing angle
        pass

    def _add_legend(self, ax):
        # TODO: add a legend for base colors and helix labels
        pass

    def plot(self):
        _, ax = self._create_3d_axes()
        self._plot_helices(ax)
        self._plot_base_pairs(ax)
        self._configure_axes(ax)
        self._add_legend(ax)
        plt.show(block = True)
            # plt.pause(0.1)
