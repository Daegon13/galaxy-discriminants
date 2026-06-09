import numpy as np
import pytest

from galaxy_discriminants.models.placeholders import (
    BurkertPlaceholderModel,
    ConstantVelocityModel,
    MondRARPlaceholderModel,
    NFWPlaceholderModel,
)


def test_constant_velocity_model_preserves_input_shape() -> None:
    radius = np.array([0.5, 1.0, 2.0, 4.0])
    prediction = ConstantVelocityModel(velocity_kms=120.0).predict(radius)

    assert prediction.velocity_kms.shape == radius.shape
    assert prediction.is_physical_model is False
    np.testing.assert_array_equal(
        prediction.velocity_kms,
        np.full(radius.shape, 120.0),
    )


def test_constant_velocity_model_rejects_negative_velocity() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        ConstantVelocityModel(velocity_kms=-1.0)


@pytest.mark.parametrize(
    "model",
    [
        MondRARPlaceholderModel(),
        NFWPlaceholderModel(),
        BurkertPlaceholderModel(),
    ],
)
def test_future_physical_placeholders_raise_not_implemented(
    model: MondRARPlaceholderModel | NFWPlaceholderModel | BurkertPlaceholderModel,
) -> None:
    with pytest.raises(NotImplementedError, match="pending verification"):
        model.predict(np.array([0.5, 1.0, 2.0]))


def test_future_physical_placeholders_still_validate_radius() -> None:
    with pytest.raises(ValueError, match="positive"):
        NFWPlaceholderModel().predict(np.array([0.0, 1.0]))
