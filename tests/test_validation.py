from typing import Any

import numpy as np
import pytest

from galaxy_discriminants.validation import (
    validate_radius_kpc,
    validate_rotation_curve_arrays,
    validate_velocity_kms,
)


def test_validate_radius_kpc_accepts_positive_strictly_increasing_array() -> None:
    radius = validate_radius_kpc([0.5, 1.0, 2.0])

    assert radius.dtype == np.float64
    np.testing.assert_array_equal(radius, np.array([0.5, 1.0, 2.0]))


@pytest.mark.parametrize(
    "bad_radius, message",
    [
        ([], "must not be empty"),
        ([1.0, np.nan], "finite"),
        ([0.0, 1.0], "positive"),
        ([1.0, 1.0], "strictly increasing"),
        ([[1.0, 2.0]], "one-dimensional"),
    ],
)
def test_validate_radius_kpc_rejects_invalid_arrays(
    bad_radius: Any,
    message: str,
) -> None:
    with pytest.raises(ValueError, match=message):
        validate_radius_kpc(bad_radius)


def test_validate_radius_kpc_can_allow_unordered_arrays_when_requested() -> None:
    radius = validate_radius_kpc([2.0, 1.0], require_strictly_increasing=False)

    np.testing.assert_array_equal(radius, np.array([2.0, 1.0]))


@pytest.mark.parametrize(
    "bad_velocity, message",
    [
        ([], "must not be empty"),
        ([1.0, np.inf], "finite"),
        ([-1.0, 1.0], "non-negative"),
        ([[100.0, 110.0]], "one-dimensional"),
    ],
)
def test_validate_velocity_kms_rejects_invalid_arrays(
    bad_velocity: Any,
    message: str,
) -> None:
    with pytest.raises(ValueError, match=message):
        validate_velocity_kms(bad_velocity)


def test_validate_rotation_curve_arrays_rejects_incompatible_shapes() -> None:
    with pytest.raises(ValueError, match="identical shapes"):
        validate_rotation_curve_arrays([1.0, 2.0], [100.0])
