"""This test is for learning generic class.

References:
    - https://docs.python.org/3/library/typing.html#user-defined-generics
    - https://docs.python.org/3/reference/datamodel.html#emulating-generic-types

"""

import re
from typing import TypeVar

import pytest


def test_user_define_generics() -> None:
    """use typing.Generic"""
    from typing import Generic

    T = TypeVar("T")

    class GenericClass(Generic[T]):
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

        # def __class_getitem__(cls, params: Any) -> Any:
        #     # Keep parameters for type checking.
        #     # but. If the type parameter is not specified,
        #     # this will not be called and the previous value will remain.
        #     cls.__generic_params = params
        #     return super().__class_getitem__(params)

        @property
        def name(self) -> str:
            return self.__name

        @property
        def value(self) -> T:
            value: T = self.__value
            return value

    obj1 = GenericClass[str]("string", "12345")
    assert isinstance(obj1.value, str)
    assert obj1.value == "12345"

    obj2 = GenericClass[int]("integer", 12345)
    assert isinstance(obj2.value, int)
    assert obj2.value == 12345

    # TODO DON'T DO TYPE ASSERTION!
    with pytest.raises(TypeError) as e:
        GenericClass[int]("string", "12345")  # type: ignore[arg-type]
        raise TypeError("DON'T DO TYPE ASSERTION!")
    assert str(e.value) == "DON'T DO TYPE ASSERTION!"

    with pytest.raises(TypeError) as e:
        GenericClass[int, bool]("int, bool", None)  # type:ignore[misc]
    assert re.match("Too many arguments for <class '.+?'>; actual 2, expected 1", str(e.value))

    # TODO DON'T DO TYPE ASSERTION!
    with pytest.raises(TypeError) as e:
        GenericClass("None", 10)
        raise TypeError("DON'T DO TYPE ASSERTION!")
    assert str(e.value) == "DON'T DO TYPE ASSERTION!"
