"""Deterministic synthetic rotation-curve data for software testing.

The data generated here are entirely artificial. They are not derived from,
and must not be interpreted as representing, any astronomical catalogue.
"""

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

FloatArray = NDArray[np.float64]


@dataclass(frozen=True)
class MockGalaxy:
    """Container for one explicitly synthetic galaxy rotation curve."""

    name: str
    radius_kpc: FloatArray
    velocity_kms: FloatArray
    velocity_error_kms: FloatArray
    true_velocity_kms: FloatArray


def generate_mock_galaxy(
    *,
    name: str = "MOCK-GALAXY-001",
    seed: int = 42,
    n_points: int = 24,
) -> MockGalaxy:
    """Generate a reproducible, non-scientific mock rotation curve.

    The smooth profile is only a convenient shape for exercising the software;
    it is not a fitted or physically motivated galaxy model.
    """
    if n_points < 3:
        msg = "n_points must be at least 3"
        raise ValueError(msg)

    rng = np.random.default_rng(seed)
    radius_kpc = np.linspace(0.5, 15.0, n_points, dtype=np.float64)
    true_velocity_kms = 185.0 * (1.0 - np.exp(-radius_kpc / 3.5))
    velocity_error_kms = rng.uniform(4.0, 9.0, size=n_points)
    velocity_kms = true_velocity_kms + rng.normal(0.0, velocity_error_kms)

    return MockGalaxy(
        name=name,
        radius_kpc=radius_kpc,
        velocity_kms=velocity_kms,
        velocity_error_kms=velocity_error_kms,
        true_velocity_kms=true_velocity_kms,
    )
