from typing import Any, Callable

import numpy as np
import pytest
from numpy.typing import ArrayLike, NDArray

from galaxy_discriminants.acceleration import (
    acceleration_to_circular_velocity_kms,
    circular_velocity_to_acceleration_m_s2,
)
from galaxy_discriminants.units import KILOMETER_IN_METERS, KPC_IN_METERS
from galaxy_discriminants.validation import validate_acceleration_m_s2

FloatArray = NDArray[np.float64]
AccelerationConversion = Callable[[ArrayLike, ArrayLike], FloatArray]


def test_circular_velocity_to_acceleration_uses_project_units() -> None:
    acceleration = circular_velocity_to_acceleration_m_s2([1.0], [1.0])

    expected = np.array([KILOMETER_IN_METERS**2 / KPC_IN_METERS])
    np.testing.assert_allclose(acceleration, expected, rtol=1e-15)
    assert acceleration.dtype == np.float64


def test_acceleration_to_circular_velocity_uses_project_units() -> None:
    acceleration = [KILOMETER_IN_METERS**2 / KPC_IN_METERS]

    velocity = acceleration_to_circular_velocity_kms([1.0], acceleration)

    np.testing.assert_allclose(velocity, np.array([1.0]), rtol=1e-15)
    assert velocity.dtype == np.float64


def test_velocity_acceleration_round_trip() -> None:
    radius = np.array([0.5, 1.5, 4.0, 10.0])
    velocity = np.array([0.0, 80.0, 140.0, 220.0])

    acceleration = circular_velocity_to_acceleration_m_s2(radius, velocity)
    recovered_velocity = acceleration_to_circular_velocity_kms(
        radius,
        acceleration,
    )

    np.testing.assert_allclose(recovered_velocity, velocity, rtol=1e-15, atol=0.0)


def test_conversion_functions_accept_lists_and_numpy_arrays() -> None:
    acceleration = circular_velocity_to_acceleration_m_s2(
        [1.0, 2.0],
        np.array([100.0, 120.0]),
    )
    velocity = acceleration_to_circular_velocity_kms(
        np.array([1.0, 2.0]),
        acceleration.tolist(),
    )

    assert isinstance(acceleration, np.ndarray)
    assert isinstance(velocity, np.ndarray)
    np.testing.assert_allclose(velocity, np.array([100.0, 120.0]))


def test_conversion_functions_do_not_mutate_inputs() -> None:
    radius = np.array([1.0, 2.0])
    velocity = np.array([100.0, 120.0])
    acceleration = np.array([1.0e-10, 2.0e-10])
    original_radius = radius.copy()
    original_velocity = velocity.copy()
    original_acceleration = acceleration.copy()

    circular_velocity_to_acceleration_m_s2(radius, velocity)
    acceleration_to_circular_velocity_kms(radius, acceleration)

    np.testing.assert_array_equal(radius, original_radius)
    np.testing.assert_array_equal(velocity, original_velocity)
    np.testing.assert_array_equal(acceleration, original_acceleration)


@pytest.mark.parametrize(
    "conversion, second_values",
    [
        (circular_velocity_to_acceleration_m_s2, [100.0, 120.0]),
        (acceleration_to_circular_velocity_kms, [1.0e-10, 2.0e-10]),
    ],
)
@pytest.mark.parametrize(
    "bad_radius, message",
    [
        ([0.0, 1.0], "positive"),
        ([-1.0, 1.0], "positive"),
        ([1.0, np.nan], "finite"),
        ([[1.0, 2.0]], "one-dimensional"),
    ],
)
def test_conversions_reject_invalid_radii(
    conversion: AccelerationConversion,
    second_values: list[float],
    bad_radius: Any,
    message: str,
) -> None:
    with pytest.raises(ValueError, match=message):
        conversion(bad_radius, second_values)


@pytest.mark.parametrize(
    "bad_velocity, message",
    [
        ([-1.0], "non-negative"),
        ([np.nan], "finite"),
        ([np.inf], "finite"),
    ],
)
def test_velocity_to_acceleration_rejects_invalid_velocity(
    bad_velocity: list[float],
    message: str,
) -> None:
    with pytest.raises(ValueError, match=message):
        circular_velocity_to_acceleration_m_s2([1.0], bad_velocity)


def test_acceleration_to_velocity_rejects_negative_acceleration() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        acceleration_to_circular_velocity_kms([1.0], [-1.0e-10])


@pytest.mark.parametrize(
    "bad_acceleration, message",
    [
        ([], "must not be empty"),
        ([-1.0e-10], "non-negative"),
        ([np.nan], "finite"),
        ([np.inf], "finite"),
        ([[1.0e-10]], "one-dimensional"),
    ],
)
def test_validate_acceleration_rejects_invalid_values(
    bad_acceleration: Any,
    message: str,
) -> None:
    with pytest.raises(ValueError, match=message):
        validate_acceleration_m_s2(bad_acceleration)


def test_validate_acceleration_returns_independent_float_array() -> None:
    original = np.array([0.0, 1.0e-10])

    validated = validate_acceleration_m_s2(original)
    original[0] = 9.0

    assert validated.dtype == np.float64
    np.testing.assert_array_equal(validated, np.array([0.0, 1.0e-10]))


@pytest.mark.parametrize(
    "conversion, second_values",
    [
        (circular_velocity_to_acceleration_m_s2, [100.0]),
        (acceleration_to_circular_velocity_kms, [1.0e-10]),
    ],
)
def test_conversions_reject_incompatible_shapes(
    conversion: AccelerationConversion,
    second_values: list[float],
) -> None:
    with pytest.raises(ValueError, match="identical shapes"):
        conversion([1.0, 2.0], second_values)
