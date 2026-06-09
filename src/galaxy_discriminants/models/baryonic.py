"""Minimal baryonic/Newtonian model from precomputed velocity components."""

from dataclasses import dataclass
from types import MappingProxyType
from typing import Mapping

import numpy as np
from numpy.typing import ArrayLike

from galaxy_discriminants.models.base import (
    FloatArray,
    ModelPrediction,
    RotationCurveModel,
)
from galaxy_discriminants.validation import validate_radius_kpc, validate_velocity_kms


@dataclass(frozen=True)
class BaryonicRotationModel(RotationCurveModel):
    """Combine precomputed baryonic velocity components in quadrature.

    Every component must contain a velocity contribution in km/s at the same
    radii later passed to :meth:`predict`. This simplified physical baseline
    does not derive velocities from masses, photometry, luminosities, or a
    gravitational potential.
    """

    components: Mapping[str, ArrayLike]

    def __post_init__(self) -> None:
        """Validate and freeze named precomputed velocity components."""
        if not self.components:
            msg = "components must not be empty"
            raise ValueError(msg)

        validated_components: dict[str, FloatArray] = {}
        expected_shape: tuple[int, ...] | None = None
        for component_name, velocity_kms in self.components.items():
            if not isinstance(component_name, str) or not component_name.strip():
                msg = "component names must be non-empty strings"
                raise ValueError(msg)

            velocity = validate_velocity_kms(velocity_kms)
            if expected_shape is None:
                expected_shape = velocity.shape
            elif velocity.shape != expected_shape:
                msg = (
                    "all baryonic velocity components must have identical shapes; "
                    f"expected {expected_shape} but component "
                    f"{component_name!r} has {velocity.shape}"
                )
                raise ValueError(msg)

            velocity_copy = np.array(velocity, dtype=np.float64, copy=True)
            velocity_copy.flags.writeable = False
            validated_components[component_name] = velocity_copy

        object.__setattr__(
            self,
            "components",
            MappingProxyType(validated_components),
        )

    @property
    def name(self) -> str:
        """Return a human-readable label for the simplified baseline."""
        return "minimal baryonic/Newtonian model"

    @property
    def is_physical(self) -> bool:
        """Mark this controlled quadrature rule as a simplified physical model."""
        return True

    def predict(self, radius_kpc: ArrayLike) -> ModelPrediction:
        """Combine all precomputed velocity components at validated radii."""
        radius = validate_radius_kpc(radius_kpc)
        component_shape = np.asarray(next(iter(self.components.values()))).shape
        if radius.shape != component_shape:
            msg = (
                "radius_kpc and baryonic velocity components must have identical "
                f"shapes; received {radius.shape} and {component_shape}"
            )
            raise ValueError(msg)

        component_stack = np.stack(tuple(self.components.values()))
        velocity = np.hypot.reduce(component_stack, axis=0)
        return ModelPrediction(
            model_name=self.name,
            radius_kpc=radius,
            velocity_kms=velocity,
            is_physical_model=self.is_physical,
            notes=(
                "Baseline físico simplificado a partir de contribuciones de "
                "velocidad precomputadas; no deriva masas, luminosidades, "
                "fotometría ni potenciales gravitatorios."
            ),
        )
