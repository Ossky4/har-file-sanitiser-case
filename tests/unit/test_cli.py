import argparse
import os

from har_sanitiser import cli


def test_cli_delegates_to_streaming_without_prereading_input(monkeypatch, tmp_path):
    """CLI should delegate directly to streaming sanitisation without pre-reading input HAR."""
    input_file = tmp_path / "input.har"
    output_file = tmp_path / "output.har"

    delegated_call = {}

    class DummySanitiser:
        def __init__(self, config=None):
            self.config = config
            self.metrics = {
                "input_size": 1024,
                "output_size": 512,
                "total_entries": 1,
                "skipped_entries": 0,
                "sensitive_data_found": {"token": 1},
            }

        def sanitise_har_streaming(self, in_file, out_file, use_parallel=True, num_processes=None):
            delegated_call["in_file"] = in_file
            delegated_call["out_file"] = out_file
            delegated_call["use_parallel"] = use_parallel
            delegated_call["num_processes"] = num_processes
            return 0.01

    monkeypatch.setattr(
        cli,
        "parse_args",
        lambda: argparse.Namespace(
            input_file=str(input_file),
            output_file=str(output_file),
            verbose=False,
            config=None,
            no_parallel=False,
            processes=4,
        ),
    )
    monkeypatch.setattr(cli, "HARSanitiser", DummySanitiser)

    real_open = open

    def guarded_open(file, mode="r", *args, **kwargs):
        if os.fspath(file) == str(input_file) and "r" in mode:
            raise AssertionError("CLI should not pre-read the input HAR before delegation")
        return real_open(file, mode, *args, **kwargs)

    monkeypatch.setattr("builtins.open", guarded_open)

    exit_code = cli.main()

    assert exit_code == 0
    assert delegated_call == {
        "in_file": str(input_file),
        "out_file": str(output_file),
        "use_parallel": True,
        "num_processes": 4,
    }
