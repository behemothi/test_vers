import pytest


@pytest.mark.integration
def test_integration_ok():
    assert "ok".upper() == "OK"
