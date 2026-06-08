"""Shared interface for rotation-curve predictors."""

from abc import ABC, abstractmethod

from numpy.typing import NDArray


class RotationCurveModel(ABC):
    """Minimal interface implemented by rotation-curve predictors."""

    @abstractmethod
    def predict(self, radius_kpc: NDArray) -> NDArray:
        """Return predicted velocity in km/s at each supplied radius."""
