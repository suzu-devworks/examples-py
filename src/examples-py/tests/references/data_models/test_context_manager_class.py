"""This test is for learning context manager class.

A context manager is an object that defines the runtime context to be established when executing a with statement.

References:
    - https://docs.python.org/ja/3/reference/datamodel.html#with-statement-context-managers
    - https://docs.python.org/ja/3/reference/datamodel.html#asynchronous-context-managers
    - https://docs.python.org/ja/3/library/contextlib.html

"""

import asyncio

import pytest


class TestContextManagerClass:
    class Resource(object):
        def __init__(self, *args, **kwargs) -> None:
            self.status = "INIT"

    def test_basic_special_method_context(self):
        """Implement two methods
        `object.__enter__()` and
        `object.__exit__()`.
        """

        class Context(object):
            def __init__(self, *args, **kwargs) -> None:
                self.__status = "INIT"

            def __enter__(self):
                self.__status = "ENTER"
                return self

            def __exit__(self, exc_type, exc_value, traceback) -> None:
                self.__status = "EXIT"

            @property
            def status(self):
                return self.__status

        context = Context()
        assert context.status == "INIT"

        with context:
            assert context.status == "ENTER"

        assert context.status == "EXIT"

    def test_inherited_manager_context(self):
        """`contextlib.AbstractContextManager` provides
        a default implementation of `object.__enter__()`.

        `object.__enter__()` provides a default implementation that returns self,
        while `object.__exit__()` is an abstract method,
        so in the end it doesn't make much difference to implement both.

        Probably for polymorphism purpose of type binding.
        """
        from contextlib import AbstractContextManager

        class Context(AbstractContextManager):
            def __init__(self, *args, **kwargs) -> None:
                self.__status = "INIT"

            # def __enter__(self) -> Self:
            #     self.__status = "ENTER"
            #     return super().__enter__()

            def __exit__(self, exc_type, exc_value, traceback) -> None:
                self.__status = "EXIT"

            @property
            def status(self) -> str:
                return self.__status

        with Context() as context:
            # assert context.status == "ENTER"
            assert context.status == "INIT"

        assert context.status == "EXIT"

    def test_contextmanager_decorator_context(self):
        """`@contextmanager` is function is a decorator that
        can be used to define a factory function
        for with statement context managers, without needing to
        create a class or `separate __enter__()` and `__exit__()` methods.
        """
        from contextlib import contextmanager

        def acquire_resource(*args, **kwds):
            return self.Resource()

        @contextmanager
        def managed_resource(*args, **kwds):
            # Code to acquire resource, e.g.:
            resource = acquire_resource(*args, **kwds)
            try:
                resource.status = "ENTER"
                yield resource
            finally:
                # Code to release resource, e.g.:
                # release_resource(resource)
                resource.status = "EXIT"

        with managed_resource() as context:
            assert context.status == "ENTER"

        assert context.status == "EXIT"

    @pytest.mark.asyncio
    async def test_async_special_method_context(self):
        """Implement two methods
        `object.__aenter__()` and
        `object.__aexit__()`.
        """

        class AsyncContext(object):
            def __init__(self, *args, **kwargs) -> None:
                self.__status = "INIT"

            def __await__(self):
                return self._awaitable.__await__()

            async def _awaitable():
                await asyncio.sleep(0)

            async def __aenter__(self):
                await asyncio.sleep(0)
                self.__status = "async ENTER"
                return self

            async def __aexit__(self, exc_type, exc_value, traceback):
                await asyncio.sleep(0)
                self.__status = "async EXIT"

            @property
            def status(self):
                return self.__status

        # sync context is not work.
        with pytest.raises(TypeError):
            with AsyncContext() as context:
                pass

        # async context is work.
        async with AsyncContext() as context:
            assert context.status == "async ENTER"

        assert context.status == "async EXIT"

    @pytest.mark.asyncio
    async def test_asynccontextmanager_decorator_context(self):
        from contextlib import asynccontextmanager

        async def acquire_resource_aync():
            await asyncio.sleep(0)
            return self.Resource()

        @asynccontextmanager
        async def managed_resource_async():
            # conn = await acquire_db_connection()
            resource = await acquire_resource_aync()
            try:
                # yield conn
                resource.status = "async ENTER"
                yield resource
            finally:
                # await release_db_connection(conn)
                resource.status = "async EXIT"

        async with managed_resource_async() as context:
            assert context.status == "async ENTER"

        assert context.status == "async EXIT"
