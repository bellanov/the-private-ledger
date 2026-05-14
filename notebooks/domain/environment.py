"""Environment Configuration.

Initialize the environment configuration using environment files defined locally.
"""

from dotenv import dotenv_values

from notebooks.domain.models.Configuration import EnvironmentConfiguration
from notebooks.domain.registry import registry

registry.register(
    ".env",
    EnvironmentConfiguration(
        config={
            # Define an environment file and load it into the configuration
            #
            # Example:
            #
            #   **dotenv_values(".env.secrets")
            #
            # Load shared development variables
            **dotenv_values(".env")
        }
    ),
)
