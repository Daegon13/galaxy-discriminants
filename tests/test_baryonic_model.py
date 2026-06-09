from typing import Any

import numpy as np
import pytest

from galaxy_discriminants.models import BaryonicRotationModel, ModelPrediction
from galaxy_discriminants.models.base import RotationCurveModel


def test_single_component_prediction_preserves_precomputed_velocity() -> None:
    radius = np.array([0.5, 1.0, 2.0])
    gas = np.array([10.0, 20.0, 30.0])
    model = BaryonicRotationModel(components={"gas": gas})

    prediction = model.predict(radius)

    assert isinstance(model, RotationCurveModel)
    assert isinstance(prediction, ModelPrediction)
    assert prediction.velocity_kms.shape == radius.shape
    np.testing.assert_array_equal(prediction.velocity_kms, gas)


def test_multiple_components_are_combined_in_quadrature() -> None:
    model = BaryonicRotationModel(
        components={
            "gas": np.array([3.0, 4.0]),
            "stellar_disk": np.array([4.0, 3.0]),
        }
    )

    prediction = model.predict(np.array([1.0, 2.0]))

    np.testing.assert_allclose(prediction.velocity_kms, np.array([5.0, 5.0]))
    assert prediction.model_name == "minimal baryonic/Newtonian model"
    assert model.name == prediction.model_name
    assert model.is_physical is True
    assert prediction.is_physical_model is True
    assert prediction.radius_unit == "kpc"
    assert prediction.velocity_unit == "km/s"


def test_model_accepts_numpy_arrays_and_copies_components() -> None:
    disk = np.array([40.0, 50.0])
    model = BaryonicRotationModel(components={"disk": disk})

    disk[0] = 999.0
    prediction = model.predict(np.array([1.0, 2.0]))

    np.testing.assert_array_equal(prediction.velocity_kms, np.array([40.0, 50.0]))
    stored_disk = np.asarray(model.components["disk"])
    assert stored_disk.flags.writeable is False


@pytest.mark.parametrize(
    "bad_radius, message",
    [
        ([0.0, 1.0], "positive"),
        ([1.0, np.nan], "finite"),
        ([2.0, 1.0], "strictly increasing"),
    ],
)
def test_model_rejects_invalid_radii(bad_radius: Any, message: str) -> None:
    model = BaryonicRotationModel(components={"gas": [10.0, 20.0]})

    with pytest.raises(ValueError, match=message):
        model.predict(bad_radius)


@pytest.mark.parametrize(
    "bad_velocity, message",
    [
        ([-1.0, 2.0], "non-negative"),
        ([1.0, np.inf], "finite"),
    ],
)
def test_model_rejects_invalid_component_velocities(
    bad_velocity: Any,
    message: str,
) -> None:
    with pytest.raises(ValueError, match=message):
        BaryonicRotationModel(components={"gas": bad_velocity})


def test_model_rejects_incompatible_component_shapes() -> None:
    with pytest.raises(ValueError, match="identical shapes"):
        BaryonicRotationModel(
            components={
                "gas": [10.0, 20.0],
                "bulge": [30.0],
            }
        )


def test_model_rejects_radius_component_shape_mismatch() -> None:
    model = BaryonicRotationModel(components={"gas": [10.0, 20.0]})

    with pytest.raises(ValueError, match="identical shapes"):
        model.predict([1.0, 2.0, 3.0])


def test_model_rejects_empty_components() -> None:
    with pytest.raises(ValueError, match="must not be empty"):
        BaryonicRotationModel(components={})
