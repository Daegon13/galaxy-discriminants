"""Explicit unit-conversion constants used by the scientific core.

The project represents radii in kiloparsecs (kpc), circular velocities in
kilometres per second (km/s), and accelerations in metres per second squared
(m/s²). Keeping these constants local avoids an additional units dependency at
this stage of the prototype.
"""

KILOMETER_IN_METERS: float = 1_000.0
KPC_IN_METERS: float = 3.085_677_581_491_367e19
