"""Shared types and interface for rotation-curve predictors."""

from abc import ABC, abstractmethod
from dataclasses import dataclass

import numpy as np
from numpy.typing import ArrayLike, NDArray

from galaxy_discriminants.validation import validate_rotation_curve_arrays

FloatArray = NDArray[np.float64]


@dataclass(frozen=True)
class ModelPrediction:
    """Validated rotation-curve prediction in the project's internal units.

    Arrays are copied and made read-only so a validated prediction cannot be
    changed accidentally after construction.
    """

    model_name: str
    radius_kpc: FloatArray
    velocity_kms: FloatArray
    is_physical_model: bool
    notes: str = ""
    radius_unit: str = "kpc"
    velocity_unit: str = "km/s"

    def __post_init__(self) -> None:
        """Validate metadata and numerical arrays."""
        if not self.model_name.strip():
            msg = "model_name must not be empty"
            raise ValueError(msg)
        if self.radius_unit != "kpc":
            msg = "radius_unit must be 'kpc'"
            raise ValueError(msg)
        if self.velocity_unit != "km/s":
            msg = "velocity_unit must be 'km/s'"
            raise ValueError(msg)

        radius, velocity = validate_rotation_curve_arrays(
            self.radius_kpc,
            self.velocity_kms,
        )
        radius_copy = np.array(radius, dtype=np.float64, copy=True)
        velocity_copy = np.array(velocity, dtype=np.float64, copy=True)
        radius_copy.flags.writeable = False
        velocity_copy.flags.writeable = False
        object.__setattr__(self, "radius_kpc", radius_copy)
        object.__setattr__(self, "velocity_kms", velocity_copy)


class RotationCurveModel(ABC):
    """Common interface for predictions at radii in kpc and speeds in km/s."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Return a human-readable model name."""

    @property
    @abstractmethod
    def is_physical(self) -> bool:
        """Report whether the implementation represents a physical model."""

    @abstractmethod
    def predict(self, radius_kpc: ArrayLike) -> ModelPrediction:
        """Predict velocities in km/s at strictly increasing radii in kpc."""
