"""Executable v0.1 pipeline using only synthetic data and a placeholder model."""

import csv
import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from galaxy_discriminants.data.mock import generate_mock_galaxy
from galaxy_discriminants.models.placeholders import ConstantVelocityModel
from galaxy_discriminants.visualization.rotation_curves import plot_mock_rotation_curve


@dataclass(frozen=True)
class PipelineOutputs:
    """Paths and basic software diagnostics produced by the mock pipeline."""

    data_path: Path
    metrics_path: Path
    figure_path: Path
    root_mean_square_error_kms: float


def run_mock_pipeline(
    output_dir: str | Path = "outputs",
    *,
    seed: int = 42,
) -> PipelineOutputs:
    """Run the deterministic v0.1 demonstration and write its artifacts."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    galaxy = generate_mock_galaxy(seed=seed)
    model = ConstantVelocityModel(velocity_kms=float(np.mean(galaxy.velocity_kms)))
    prediction = model.predict(galaxy.radius_kpc)
    predicted_velocity_kms = prediction.velocity_kms
    rmse = float(np.sqrt(np.mean((galaxy.velocity_kms - predicted_velocity_kms) ** 2)))

    data_path = output_dir / "mock_rotation_curve.csv"
    with data_path.open("w", newline="", encoding="utf-8") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(
            [
                "radius_kpc",
                "synthetic_velocity_kms",
                "synthetic_velocity_error_kms",
                "placeholder_prediction_kms",
            ]
        )
        writer.writerows(
            zip(
                galaxy.radius_kpc,
                galaxy.velocity_kms,
                galaxy.velocity_error_kms,
                predicted_velocity_kms,
                strict=True,
            )
        )

    metrics_path = output_dir / "mock_pipeline_summary.json"
    metrics = {
        "data_kind": "mock/synthetic",
        "galaxy_name": galaxy.name,
        "model": prediction.model_name,
        "n_points": len(galaxy.radius_kpc),
        "root_mean_square_error_kms": rmse,
        "seed": seed,
    }
    metrics_path.write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")

    figure_path = plot_mock_rotation_curve(
        galaxy,
        predicted_velocity_kms,
        output_dir / "mock_rotation_curve.png",
    )
    return PipelineOutputs(data_path, metrics_path, figure_path, rmse)


def main() -> None:
    """Run the mock pipeline from the command line."""
    outputs = run_mock_pipeline()
    print("Mock pipeline completed (synthetic data only).")
    print(f"Data: {outputs.data_path}")
    print(f"Summary: {outputs.metrics_path}")
    print(f"Figure: {outputs.figure_path}")


if __name__ == "__main__":
    main()
