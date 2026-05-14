"""Test Configuration Model."""

import pytest

from notebooks.domain.models.Configuration import EnvironmentConfiguration


@pytest.mark.unit
def test_environment_configuration_get() -> None:
    """Test Environment Configuration - Get."""
    config = EnvironmentConfiguration(config={"env": "production", "debug": False})
    assert config.get_config() == {"env": "production", "debug": False}


@pytest.mark.unit
def test_environment_configuration_set() -> None:
    """Test Environment Configuration - Set."""
    config = EnvironmentConfiguration(config={})
    config.set_config({"env": "development", "debug": True})
    assert config.get_config() == {"env": "development", "debug": True}
