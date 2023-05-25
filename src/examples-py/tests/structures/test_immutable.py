"""
This test to learn immutable class.

You can't create a true Immutable with python.
But you can use Frozen instances of dataclass in a similar way.

References:
- https://peps.python.org/pep-0557/
- https://docs.python.org/3/library/dataclasses.html

"""


from dataclasses import FrozenInstanceError, dataclass, field
from typing import Any

import pytest


class TestImmutable(object):
    def test_imuutable_with_dataclass(self) -> None:
        """
        use @dataclass(frozen=True).
        """

        @dataclass(frozen=True)
        class Immutable(object):
            name: str
            price: float
            alias: str | None = None
            count: int = field(kw_only=True, default=0)
            attributes: dict[str, Any] = field(
                default_factory=lambda: ({"type-a": 100, "type-b": True, "type-c": "hogehoge"})
            )
            features: list[Any] = field(default_factory=list)

        instance = Immutable("Foo", 110.00, count=1)
        assert isinstance(instance, Immutable)
        assert instance.name == "Foo"
        assert instance.price == 110.00
        assert instance.alias is None
        assert instance.count == 1
        assert instance.attributes == {"type-a": 100, "type-b": True, "type-c": "hogehoge"}
        assert instance.features == []

        with pytest.raises(FrozenInstanceError):
            instance.name = "Bar"  # type: ignore[misc]
        with pytest.raises(FrozenInstanceError):
            instance.price = 110.00  # type: ignore[misc]
        with pytest.raises(FrozenInstanceError):
            instance.alias = "Bas"  # type: ignore[misc]
        with pytest.raises(FrozenInstanceError):
            instance.count = -1  # type: ignore[misc]

        # This is not immutable.
        instance.attributes["new-a"] = 10.0
        assert instance.attributes == {"type-a": 100, "type-b": True, "type-c": "hogehoge", "new-a": 10.0}

        with pytest.raises(FrozenInstanceError):
            instance.attributes = {"new-b": False}  # type: ignore[misc]

        # This is not immutable.
        instance.features.append("new entry.")
        assert instance.features == ["new entry."]

        with pytest.raises(FrozenInstanceError):
            instance.features = ["new list"]  # type: ignore[misc]
