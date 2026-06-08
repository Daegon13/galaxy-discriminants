"""Validation helpers for rotation-curve arrays and their documented units."""

import numpy as np
from numpy.typing import ArrayLike, NDArray

FloatArray = NDArray[np.float64]


def validate_radius_kpc(
    radius_kpc: ArrayLike,
    *,
    require_strictly_increasing: bool = True,
) -> FloatArray:
    """Return validated one-dimensional radii expressed in kiloparsecs.

    Radii must be non-empty, finite, and strictly positive. Model predictions
    use strictly increasing samples by default so their ordering is explicit.
    """
    radius = np.asarray(radius_kpc, dtype=np.float64)
    if radius.ndim != 1:
        msg = "radius_kpc must be a one-dimensional array"
        raise ValueError(msg)
    if radius.size == 0:
        msg = "radius_kpc must not be empty"
        raise ValueError(msg)
    if not np.all(np.isfinite(radius)):
        msg = "radius_kpc must contain only finite values"
        raise ValueError(msg)
    if np.any(radius <= 0):
        msg = "radius_kpc must contain only positive values"
        raise ValueError(msg)
    if require_strictly_increasing and np.any(np.diff(radius) <= 0):
        msg = "radius_kpc must be strictly increasing"
        raise ValueError(msg)
    return radius


def validate_velocity_kms(velocity_kms: ArrayLike) -> FloatArray:
    """Return validated one-dimensional speeds expressed in kilometres/second."""
    velocity = np.asarray(velocity_kms, dtype=np.float64)
    if velocity.ndim != 1:
        msg = "velocity_kms must be a one-dimensional array"
        raise ValueError(msg)
    if velocity.size == 0:
        msg = "velocity_kms must not be empty"
        raise ValueError(msg)
    if not np.all(np.isfinite(velocity)):
        msg = "velocity_kms must contain only finite values"
        raise ValueError(msg)
    if np.any(velocity < 0):
        msg = "velocity_kms must contain only non-negative values"
        raise ValueError(msg)
    return velocity


def validate_rotation_curve_arrays(
    radius_kpc: ArrayLike,
    velocity_kms: ArrayLike,
    *,
    require_strictly_increasing: bool = True,
) -> tuple[FloatArray, FloatArray]:
    """Validate a radius/velocity pair and require identical shapes."""
    radius = validate_radius_kpc(
        radius_kpc,
        require_strictly_increasing=require_strictly_increasing,
    )
    velocity = validate_velocity_kms(velocity_kms)
    if radius.shape != velocity.shape:
        msg = (
            "radius_kpc and velocity_kms must have identical shapes; "
            f"received {radius.shape} and {velocity.shape}"
        )
        raise ValueError(msg)
    return radius, velocity
