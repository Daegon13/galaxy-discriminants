import numpy as np
import pytest

from galaxy_discriminants.data.mock import generate_mock_galaxy


def test_mock_galaxy_has_expected_shapes_and_positive_uncertainties() -> None:
    galaxy = generate_mock_galaxy(seed=7, n_points=12)

    assert galaxy.name.startswith("MOCK-")
    assert galaxy.radius_kpc.shape == (12,)
    assert galaxy.velocity_kms.shape == (12,)
    assert galaxy.velocity_error_kms.shape == (12,)
    assert galaxy.true_velocity_kms.shape == (12,)
    assert np.all(galaxy.velocity_error_kms > 0)
    assert np.all(np.diff(galaxy.radius_kpc) > 0)


def test_mock_generation_is_reproducible() -> None:
    first = generate_mock_galaxy(seed=123)
    second = generate_mock_galaxy(seed=123)

    np.testing.assert_array_equal(first.velocity_kms, second.velocity_kms)
    np.testing.assert_array_equal(first.velocity_error_kms, second.velocity_error_kms)


def test_mock_generation_rejects_too_few_points() -> None:
    with pytest.raises(ValueError, match="at least 3"):
        generate_mock_galaxy(n_points=2)
