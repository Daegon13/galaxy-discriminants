"""Rotation-curve model interfaces and non-scientific placeholders."""

from galaxy_discriminants.models.base import RotationCurveModel
from galaxy_discriminants.models.placeholders import ConstantVelocityModel

__all__ = ["ConstantVelocityModel", "RotationCurveModel"]
