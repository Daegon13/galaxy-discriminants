import json
from pathlib import Path

from galaxy_discriminants.pipeline import run_mock_pipeline


def test_mock_pipeline_creates_expected_artifacts(tmp_path: Path) -> None:
    outputs = run_mock_pipeline(tmp_path, seed=99)

    assert outputs.data_path.is_file()
    assert outputs.metrics_path.is_file()
    assert outputs.figure_path.is_file()
    assert outputs.figure_path.stat().st_size > 0
    assert outputs.root_mean_square_error_kms >= 0

    metrics = json.loads(outputs.metrics_path.read_text(encoding="utf-8"))
    assert metrics["data_kind"] == "mock/synthetic"
    assert metrics["seed"] == 99
    assert metrics["model"] == "constant-velocity non-scientific placeholder"
