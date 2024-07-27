"""This test is for learning iterator class.

Supports a concept of iteration over containers.

References:
    - https://docs.python.org/3/library/stdtypes.html#iterator-types
    - https://docs.python.org/3/reference/datamodel.html#asynchronous-iterators

"""

import asyncio
from typing import Any, Self

import pytest


class TestIteratorClass:
    def test_basic_special_method_iterator(self) -> None:
        """Implement two methods
        `object.__iter__()` and
        `object.__next__()`.
        """

        class IteratorClass(object):
            def __init__(self, num: int, *args: Any, **kwargs: Any) -> None:
                self.__num = num
                self.__count: int = 0

            def __iter__(self) -> Self:
                # return return an object with __next__ method.
                return self

            def __next__(self) -> str:
                if self.__count < self.__num:
                    value = str(self.__count)
                    self.__count += 1
                    return value

                raise StopIteration()

            @property
            def status(self) -> int:
                return self.__count

        count = 0
        for _ in IteratorClass(3):
            count += 1
        assert count == 3

        values = list(IteratorClass(5))
        assert values == ["0", "1", "2", "3", "4"]

        values = [x for x in IteratorClass(5)]
        assert values == ["0", "1", "2", "3", "4"]

    @pytest.mark.asyncio
    async def test_async_special_method_iterator(self) -> None:
        """Implement two methods
        `object.__aiter__()` and
        `object.__anext__()`.
        """

        # def __aiter__(self):
        #     return self

        # async def __anext__(self):
        #     val = await self.readline()
        #     if val == b"":
        #         raise StopAsyncIteration
        #     return val

        class AsyncIterator(object):
            def __init__(self, num: int, *args: Any, **kwargs: Any) -> None:
                self.__num = num
                self.__count: int = 0

            def __aiter__(self) -> Self:
                # return return an object with __next__ method.
                return self

            async def __anext__(self) -> str:
                await asyncio.sleep(0)
                if self.__count < self.__num:
                    value = str(self.__count)
                    self.__count += 1
                    return value

                raise StopAsyncIteration()

            @property
            def status(self) -> int:
                return self.__count

        count = 0
        async for _ in AsyncIterator(3):
            await asyncio.sleep(0)
            count += 1
        assert count == 3

        # not work.
        # values = list(AsyncIterator(5))

        values = [item async for item in AsyncIterator(5)]
        assert values == ["0", "1", "2", "3", "4"]
