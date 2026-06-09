import numpy as np
import pytest

from galaxy_discriminants.models import ConstantVelocityModel, ModelPrediction
from galaxy_discriminants.models.base import RotationCurveModel


def test_constant_velocity_model_implements_common_interface() -> None:
    model = ConstantVelocityModel(velocity_kms=120.0)

    assert isinstance(model, RotationCurveModel)
    assert model.name == "constant-velocity non-scientific placeholder"
    assert model.is_physical is False

    prediction = model.predict(np.array([0.5, 1.0, 2.0]))

    assert isinstance(prediction, ModelPrediction)
    assert prediction.model_name == model.name
    assert prediction.is_physical_model is False
    assert prediction.radius_unit == "kpc"
    assert prediction.velocity_unit == "km/s"
    np.testing.assert_array_equal(prediction.velocity_kms, np.full(3, 120.0))


def test_model_prediction_validates_units_and_shapes() -> None:
    with pytest.raises(ValueError, match="identical shapes"):
        ModelPrediction(
            model_name="bad prediction",
            radius_kpc=np.array([1.0, 2.0]),
            velocity_kms=np.array([100.0]),
            is_physical_model=False,
        )

    with pytest.raises(ValueError, match="radius_unit"):
        ModelPrediction(
            model_name="bad unit",
            radius_kpc=np.array([1.0]),
            velocity_kms=np.array([100.0]),
            is_physical_model=False,
            radius_unit="m",
        )


def test_model_prediction_copies_arrays_and_makes_them_read_only() -> None:
    radius = np.array([1.0, 2.0])
    velocity = np.array([100.0, 110.0])
    prediction = ModelPrediction(
        model_name="immutable prediction",
        radius_kpc=radius,
        velocity_kms=velocity,
        is_physical_model=False,
    )

    radius[0] = 9.0
    assert prediction.radius_kpc[0] == 1.0
    assert prediction.radius_kpc.flags.writeable is False
    assert prediction.velocity_kms.flags.writeable is False

    with pytest.raises(ValueError, match="read-only"):
        prediction.velocity_kms[0] = 99.0
