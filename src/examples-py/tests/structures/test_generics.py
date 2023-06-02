"""
This test to learn generic class.

References:
- https://docs.python.org/3/library/typing.html#user-defined-generics
- https://docs.python.org/3/reference/datamodel.html#emulating-generic-types

"""
import re
from typing import Any, Generic, TypeVar

import pytest


class TestGenerics(object):
    def test_basic_generics(self) -> None:
        """
        use typing.Generic
        """
        T = TypeVar("T")

        class MyGeneric(Generic[T]):
            def __init__(self, name: str, value: T) -> None:
                self.__name = name
                self.__value: T = value

                # Is it a bad pattern to keep type arguments by __class_getitem__ and do type checking here?
                # The Python library doesn't seem to do type checking.

                # types = self.__generic_params
                # self.__generic_params = None
                # if types is None:
                #     raise TypeError("Please specify a type argument.")
                # types = types if isinstance(types, tuple) else (types,)

                # if not isinstance(value, types[0]):
                #     raise TypeError("wrong type specified for value.")

            @classmethod
            def __class_getitem__(cls, params: type | tuple[type]) -> Any:
                # Keep parameters for type checking.
                # but. If the type parameter is not specified,
                # this will not be called and the previous value will remain.

                # cls.__generic_params = params
                return super().__class_getitem__(params)  # type: ignore[misc]

            @property
            def name(self) -> str:
                return self.__name

            @property
            def value(self) -> T:
                value: T = self.__value
                return value

        obj1 = MyGeneric[str]("string", "12345")
        assert isinstance(obj1.value, str)
        assert obj1.value == "12345"

        obj2 = MyGeneric[int]("integer", 12345)
        assert isinstance(obj2.value, int)
        assert obj2.value == 12345

        # TODO DON'T DO TYPE ASSERTION!
        with pytest.raises(TypeError) as e:
            MyGeneric[int]("string", "12345")  # type: ignore[arg-type]
            raise TypeError("DON'T DO TYPE ASSERTION!")
        assert str(e.value) == "DON'T DO TYPE ASSERTION!"

        with pytest.raises(TypeError) as e:
            MyGeneric[int, bool]("int, bool", None)  # type: ignore[misc]
        assert re.match("Too many arguments for <class '.+?'>; actual 2, expected 1", str(e.value))

        # TODO DON'T DO TYPE ASSERTION!
        with pytest.raises(TypeError) as e:
            MyGeneric("None", 10)
            raise TypeError("DON'T DO TYPE ASSERTION!")
        assert str(e.value) == "DON'T DO TYPE ASSERTION!"
