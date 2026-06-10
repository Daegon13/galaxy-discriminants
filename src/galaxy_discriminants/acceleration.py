"""Conversions between circular velocity and centripetal acceleration."""

import numpy as np
from numpy.typing import ArrayLike

from galaxy_discriminants.units import KILOMETER_IN_METERS, KPC_IN_METERS
from galaxy_discriminants.validation import (
    FloatArray,
    validate_acceleration_m_s2,
    validate_radius_kpc,
    validate_velocity_kms,
)


def circular_velocity_to_acceleration_m_s2(
    radius_kpc: ArrayLike,
    velocity_kms: ArrayLike,
) -> FloatArray:
    """Convert circular velocities in km/s to accelerations in m/s².

    The pointwise conversion uses ``g = v² / r``. Radial samples must be
    positive but do not need to be sorted because this utility does not build a
    rotation-curve prediction.
    """
    radius = validate_radius_kpc(
        radius_kpc,
        require_strictly_increasing=False,
    )
    velocity = validate_velocity_kms(velocity_kms)
    _require_identical_shapes(radius, velocity, second_name="velocity_kms")

    radius_m = radius * KPC_IN_METERS
    velocity_m_s = velocity * KILOMETER_IN_METERS
    return np.asarray(np.square(velocity_m_s) / radius_m, dtype=np.float64)


def acceleration_to_circular_velocity_kms(
    radius_kpc: ArrayLike,
    acceleration_m_s2: ArrayLike,
) -> FloatArray:
    """Convert accelerations in m/s² to circular velocities in km/s.

    The pointwise conversion uses ``v = sqrt(g * r)``. Radial samples must be
    positive but do not need to be sorted because this utility does not build a
    rotation-curve prediction.
    """
    radius = validate_radius_kpc(
        radius_kpc,
        require_strictly_increasing=False,
    )
    acceleration = validate_acceleration_m_s2(acceleration_m_s2)
    _require_identical_shapes(
        radius,
        acceleration,
        second_name="acceleration_m_s2",
    )

    radius_m = radius * KPC_IN_METERS
    velocity_m_s = np.sqrt(acceleration * radius_m)
    return np.asarray(velocity_m_s / KILOMETER_IN_METERS, dtype=np.float64)


def _require_identical_shapes(
    radius: FloatArray,
    values: FloatArray,
    *,
    second_name: str,
) -> None:
    """Require pointwise radius/value inputs to have identical shapes."""
    if radius.shape != values.shape:
        msg = (
            f"radius_kpc and {second_name} must have identical shapes; "
            f"received {radius.shape} and {values.shape}"
        )
        raise ValueError(msg)
