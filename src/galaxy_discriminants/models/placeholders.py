"""Non-scientific placeholder models for validating the v0.1 pipeline."""

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

from galaxy_discriminants.models.base import RotationCurveModel


@dataclass(frozen=True)
class ConstantVelocityModel(RotationCurveModel):
    """Return one constant velocity; this is not a physical galaxy model."""

    velocity_kms: float

    def __post_init__(self) -> None:
        if not np.isfinite(self.velocity_kms) or self.velocity_kms < 0:
            msg = "velocity_kms must be finite and non-negative"
            raise ValueError(msg)

    def predict(self, radius_kpc: NDArray) -> NDArray:
        """Return the configured constant with the input array's shape."""
        radius = np.asarray(radius_kpc, dtype=np.float64)
        return np.full(radius.shape, self.velocity_kms, dtype=np.float64)
