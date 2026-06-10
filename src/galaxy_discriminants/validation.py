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


def _validate_non_negative_array(values: ArrayLike, *, name: str) -> FloatArray:
    """Return a copied one-dimensional, finite, non-negative float array."""
    array = np.array(values, dtype=np.float64, copy=True)
    if array.ndim != 1:
        msg = f"{name} must be a one-dimensional array"
        raise ValueError(msg)
    if array.size == 0:
        msg = f"{name} must not be empty"
        raise ValueError(msg)
    if not np.all(np.isfinite(array)):
        msg = f"{name} must contain only finite values"
        raise ValueError(msg)
    if np.any(array < 0):
        msg = f"{name} must contain only non-negative values"
        raise ValueError(msg)
    return array


def validate_velocity_kms(velocity_kms: ArrayLike) -> FloatArray:
    """Return validated one-dimensional speeds in kilometres per second."""
    return _validate_non_negative_array(velocity_kms, name="velocity_kms")


def validate_acceleration_m_s2(acceleration_m_s2: ArrayLike) -> FloatArray:
    """Return validated one-dimensional accelerations in metres per second²."""
    return _validate_non_negative_array(
        acceleration_m_s2,
        name="acceleration_m_s2",
    )


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
