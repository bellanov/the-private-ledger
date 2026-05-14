"""Registry Model."""

from abc import ABC, abstractmethod
from typing import Any

type Service = Any


class Registry(ABC):
    """Generic Registry."""

    services: dict[str, Service]

    # Retrieve an Item
    @abstractmethod
    def get_service(self, key: str) -> Service: ...

    # Register an Item
    @abstractmethod
    def register(self, key: str, value: Service) -> None: ...


class ServiceRegistry(Registry):
    """Service Registry."""

    def __init__(self) -> None:
        """Initialize the Registry."""
        self.services = {}

    def get_service(self, key: str) -> Service:
        """Retrieve a Service."""
        return self.services.get(key)

    def register(self, key: str, value: Service) -> None:
        """Register a Service."""
        self.services[key] = value
