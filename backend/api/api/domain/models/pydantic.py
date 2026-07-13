"""Pydantic Models."""

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class CamelCaseModel(BaseModel):
    """Base model with camelCase aliasing and ORM integration.

    Attributes:
        model_config: Configuration for the Pydantic model.
    """

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,  # Allows python to parse snake_case if needed
        from_attributes=True,  # Helps with ORM integration like SQLAlchemy
    )
