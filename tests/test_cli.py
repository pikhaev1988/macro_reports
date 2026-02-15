import pytest
from main import REPORTS


def test_unknown_report():
    assert "unknown" not in REPORTS
