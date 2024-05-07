"""This test is for learning immutable class.

You can't create a true Immutable with python.
But you can use Frozen instances of dataclass in a similar way.

References:
    - https://peps.python.org/pep-0557/
    - https://docs.python.org/3/library/dataclasses.html

"""

from dataclasses import FrozenInstanceError, dataclass, field
from typing import Any

import pytest


class TestImmutableClass:
    def test_immutable_with_dataclass(self) -> None:
        """use `@dataclass(frozen=True)`."""

        @dataclass(frozen=True)
        class ImmutableClass:
            name: str
            price: float
            alias: str | None = None
            count: int = field(kw_only=True, default=0)
            attributes: dict[str, Any] = field(
                default_factory=lambda: ({"type-a": 100, "type-b": True, "type-c": "hello immutable"})
            )
            features: list[Any] = field(default_factory=list)

        instance = ImmutableClass("Foo", 110.00, count=1)
        assert isinstance(instance, ImmutableClass)
        assert instance.name == "Foo"
        assert instance.price == 110.00
        assert instance.alias is None
        assert instance.count == 1
        assert instance.attributes == {
            "type-a": 100,
            "type-b": True,
            "type-c": "hello immutable",
        }
        assert instance.features == []

        with pytest.raises(FrozenInstanceError):
            instance.name = "Bar"  # type: ignore[misc]
        with pytest.raises(FrozenInstanceError):
            instance.price = 110.00  # type: ignore[misc]
        with pytest.raises(FrozenInstanceError):
            instance.alias = "Bas"  # type: ignore[misc]
        with pytest.raises(FrozenInstanceError):
            instance.count = -1  # type: ignore[misc]

        # References such as dictionaries are not immutable.
        instance.attributes["add new entry"] = 10.0
        assert instance.attributes == {
            "type-a": 100,
            "type-b": True,
            "type-c": "hello immutable",
            "add new entry": 10.0,
        }

        with pytest.raises(FrozenInstanceError):
            instance.attributes = {"replace new dictionary": False}  # type: ignore[misc]

        # list is also a reference so it is not immutable.
        instance.features.append("append new entry")
        assert instance.features == ["append new entry"]

        with pytest.raises(FrozenInstanceError):
            instance.features = ["replace new list"]  # type: ignore[misc]
