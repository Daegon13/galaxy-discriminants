"""Non-scientific placeholders used to exercise the model infrastructure."""

from dataclasses import dataclass

import numpy as np
from numpy.typing import ArrayLike

from galaxy_discriminants.models.base import ModelPrediction, RotationCurveModel
from galaxy_discriminants.validation import validate_radius_kpc


@dataclass(frozen=True)
class ConstantVelocityModel(RotationCurveModel):
    """Return one constant speed; this is not a physical galaxy model."""

    velocity_kms: float

    @property
    def name(self) -> str:
        """Return an explicit non-scientific model label."""
        return "constant-velocity non-scientific placeholder"

    @property
    def is_physical(self) -> bool:
        """Mark this implementation as non-physical."""
        return False

    def __post_init__(self) -> None:
        if not np.isfinite(self.velocity_kms) or self.velocity_kms < 0:
            msg = "velocity_kms must be finite and non-negative"
            raise ValueError(msg)

    def predict(self, radius_kpc: ArrayLike) -> ModelPrediction:
        """Return a validated, explicitly non-scientific prediction."""
        radius = validate_radius_kpc(radius_kpc)
        velocity = np.full(radius.shape, self.velocity_kms, dtype=np.float64)
        return ModelPrediction(
            model_name=self.name,
            radius_kpc=radius,
            velocity_kms=velocity,
            is_physical_model=self.is_physical,
            notes="Placeholder constante para pruebas de software; sin física real.",
        )


class FuturePhysicalModelStub(RotationCurveModel):
    """Base stub that reserves a model-family name without inventing physics."""

    name = "future physical model (pending verification)"
    is_physical = False

    def predict(self, radius_kpc: ArrayLike) -> ModelPrediction:
        """Reject prediction until a scientifically reviewed implementation exists."""
        validate_radius_kpc(radius_kpc)
        msg = (
            f"{self.name} is not implemented in v0.2a; "
            "physical formulas are pending verification"
        )
        raise NotImplementedError(msg)


class MondRARPlaceholderModel(FuturePhysicalModelStub):
    """Nominal MOND/RAR stub with no physical implementation."""

    name = "MOND/RAR placeholder"


class NFWPlaceholderModel(FuturePhysicalModelStub):
    """Nominal NFW stub with no physical implementation."""

    name = "NFW placeholder"


class BurkertPlaceholderModel(FuturePhysicalModelStub):
    """Nominal Burkert stub with no physical implementation."""

    name = "Burkert placeholder"
