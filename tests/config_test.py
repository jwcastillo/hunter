from pathlib import Path

from hunter.config import load_config_from
from hunter.test_config import GraphiteTestConfig, CsvTestConfig


def test_load_graphite_tests():
    config = load_config_from(Path("tests/resources/sample_config.yaml"))
    tests = config.tests
    assert len(tests) == 5
    test = tests["dse68.write.rf1"]
    assert isinstance(test, GraphiteTestConfig)
    assert len(test.metrics) == 7
    print(test.metrics)
    assert test.prefix == "performance_regressions.daily.dse68.write.throughput.1-bmsmall-rf-1"
    assert test.metrics["throughput"].name == "throughput"
    assert test.metrics["throughput"].suffix is not None
    assert test.metrics["p50"].name == "p50"
    assert test.metrics["p50"].direction == -1
    assert test.metrics["p50"].scale == 1.0e-6
    assert test.metrics["p50"].suffix is not None


def test_load_csv_tests():
    config = load_config_from(Path("tests/resources/sample_config.yaml"))
    tests = config.tests
    assert len(tests) == 5
    test = tests["local_1"]
    assert isinstance(test, CsvTestConfig)
    assert len(test.metrics) == 2
    assert len(test.attributes) == 1
    assert test.file == "tests/resources/sample.csv"

    test = tests["local_2"]
    assert isinstance(test, CsvTestConfig)
    assert len(test.metrics) == 2
    assert test.metrics["m1"].column == "metric1"
    assert test.metrics["m1"].direction == 1
    assert test.metrics["m2"].column == "metric2"
    assert test.metrics["m2"].direction == -1
    assert len(test.attributes) == 1
    assert test.file == "tests/resources/sample.csv"


def test_load_test_groups():
    config = load_config_from(Path("tests/resources/sample_config.yaml"))
    groups = config.test_groups
    assert len(groups) == 1
    assert len(groups["dse68"]) == 3