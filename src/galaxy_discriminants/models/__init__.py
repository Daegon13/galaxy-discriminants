"""Rotation-curve model interfaces, baselines, and placeholders."""

from galaxy_discriminants.models.baryonic import BaryonicRotationModel
from galaxy_discriminants.models.base import ModelPrediction, RotationCurveModel
from galaxy_discriminants.models.placeholders import (
    BurkertPlaceholderModel,
    ConstantVelocityModel,
    MondRARPlaceholderModel,
    NFWPlaceholderModel,
)

__all__ = [
    "BaryonicRotationModel",
    "BurkertPlaceholderModel",
    "ConstantVelocityModel",
    "ModelPrediction",
    "MondRARPlaceholderModel",
    "NFWPlaceholderModel",
    "RotationCurveModel",
]
