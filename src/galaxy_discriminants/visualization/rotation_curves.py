"""Basic visualizations for explicitly synthetic rotation curves."""

from pathlib import Path

import matplotlib.pyplot as plt
from numpy.typing import NDArray

from galaxy_discriminants.data.mock import MockGalaxy


def plot_mock_rotation_curve(
    galaxy: MockGalaxy,
    predicted_velocity_kms: NDArray,
    output_path: Path,
) -> Path:
    """Save an explicitly labelled mock-data and placeholder-model plot."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    figure, axis = plt.subplots(figsize=(8, 5))
    axis.errorbar(
        galaxy.radius_kpc,
        galaxy.velocity_kms,
        yerr=galaxy.velocity_error_kms,
        fmt="o",
        capsize=3,
        label="Synthetic observations",
    )
    axis.plot(
        galaxy.radius_kpc,
        predicted_velocity_kms,
        label="Non-scientific placeholder prediction",
    )
    axis.set(
        title=f"{galaxy.name} — MOCK / SYNTHETIC DATA ONLY",
        xlabel="Radius [kpc]",
        ylabel="Velocity [km/s]",
    )
    axis.legend()
    axis.grid(alpha=0.25)
    figure.tight_layout()
    figure.savefig(output_path, dpi=150)
    plt.close(figure)
    return output_path
