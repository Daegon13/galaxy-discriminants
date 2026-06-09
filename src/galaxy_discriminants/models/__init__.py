"""Rotation-curve model interfaces and non-scientific placeholders."""

from galaxy_discriminants.models.base import ModelPrediction, RotationCurveModel
from galaxy_discriminants.models.placeholders import (
    BurkertPlaceholderModel,
    ConstantVelocityModel,
    MondRARPlaceholderModel,
    NFWPlaceholderModel,
)

__all__ = [
    "BurkertPlaceholderModel",
    "ConstantVelocityModel",
    "ModelPrediction",
    "MondRARPlaceholderModel",
    "NFWPlaceholderModel",
    "RotationCurveModel",
]
