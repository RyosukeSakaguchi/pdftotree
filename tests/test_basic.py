#!/usr/bin/env python
import pytest
import sys
from tests.context import pdftotree


def test_heuristic_completion():
    """Simply test that parse runs to completion without errors."""
    output = pdftotree.parse("tests/input/paleo.pdf")
    assert output is not None


@pytest.mark.skipif(sys.version_info > (2, 7), reason="Only runs on Python2.")
def test_ml_completion():
    """Simply test that ML-based parse runs without errors."""
    output = pdftotree.parse(
        "tests/input/paleo.pdf", model_path="tests/input/paleo_model.pkl")
    assert output is not None
