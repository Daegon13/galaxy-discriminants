import numpy as np
import pytest

from galaxy_discriminants.models.placeholders import ConstantVelocityModel


def test_constant_velocity_model_preserves_input_shape() -> None:
    radius = np.array([0.5, 1.0, 2.0, 4.0])
    prediction = ConstantVelocityModel(velocity_kms=120.0).predict(radius)

    assert prediction.shape == radius.shape
    np.testing.assert_array_equal(prediction, np.full(radius.shape, 120.0))


def test_constant_velocity_model_rejects_negative_velocity() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        ConstantVelocityModel(velocity_kms=-1.0)
