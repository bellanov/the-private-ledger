"""Configuration Model."""

from abc import ABC, abstractmethod

type Config = dict


class Configuration(ABC):
    """Generic Configuration."""

    config: Config

    # Retrieve the Configuration
    @abstractmethod
    def get_config(self) -> Config: ...

    # Set the Configuration
    @abstractmethod
    def set_config(self, value: Config) -> None: ...


class EnvironmentConfiguration(Configuration):
    """Environment Configuration."""

    def __init__(self, config: Config) -> None:
        """Initialize the Configuration."""
        self.config = config

    def get_config(self) -> Config:
        """Retrieve the Configuration."""
        return self.config

    def set_config(self, value: Config) -> None:
        """Set the Configuration."""
        self.config = value
