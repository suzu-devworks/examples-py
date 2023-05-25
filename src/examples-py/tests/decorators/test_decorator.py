"""
This test to learn decorators for functions and methods.

Gof's Decorator pattern aims to "add new functionality and behavior to existing objects dynamically."

Decorators in Python are discussed in his PEP318 and PEP3129,
and extend their functionality by writing them into functions,
methods, and classes as syntactic sugar described in @metadata.

References:
- https://peps.python.org/pep-0318/

"""  # noqa E501
from functools import wraps
from typing import Any, Callable, TypeAlias, TypeVar

import pytest
from typing_extensions import ParamSpec

P = ParamSpec("P")
F = TypeVar("F", bound=Callable[..., Any])

SomeTypes: TypeAlias = type | tuple[type, ...]


class TestDecorator(object):
    def test_without_arguments_not_return_wrapper(self) -> None:
        """
        Pattern of without arguments and not return a wrapper function.

        This is the pattern from Example 1 of PEP318.
        This pattern is almost impractical.
        """

        def onexit(f: F) -> F:
            import atexit

            atexit.register(f)
            return f

        @onexit
        def func() -> None:
            print("Exit on called.")

        # Called at normal program exit, e.g. when sys.exit() is called,
        # or when the main module completes execution.

        # `@atexit.register` is just a decorator.

    def test_without_arguments_return_wrapper(self) -> None:
        """
        Pattern of without arguments and return a wrapper function.

        This is the pattern from Example 2 of PEP318.
        The basic pattern, whether or not there is a return value, doesn't seem to matter.
        """

        def singleton(cls: type) -> Callable[[], Any]:
            instances: dict[type, Any] = {}

            def getinstance() -> Any:
                if cls not in instances:
                    instances[cls] = cls()
                return instances[cls]

            return getinstance

        @singleton
        class MyClass:
            pass

        object1 = MyClass()
        object2 = MyClass()
        assert object1 == object2
        assert object1 is object2

    def test_with_arguments_not_return_wrapper(self) -> None:
        """
        Pattern of with arguments and not return a wrapper function.

        This is the pattern from Example 3 of PEP318.
        The app/Flask.route function of flask seems to use this pattern.
        """

        def attrs(**kwds: Any) -> Callable[[F], F]:
            def decorate(f: F) -> F:
                for k in kwds:
                    setattr(f, k, kwds[k])
                return f

            return decorate

        @attrs(versionadded="2.2", author="Guido van Rossum")
        def mymethod() -> None:
            pass

        assert mymethod.versionadded == "2.2"  # type: ignore[attr-defined]
        assert mymethod.author == "Guido van Rossum"  # type: ignore[attr-defined]

    def test_with_arguments_return_wrapper(self) -> None:
        """
        Pattern of with arguments and return a wrapper function.

        This is the pattern from Example 4 of PEP318.
        """

        def accepts(*types: SomeTypes) -> Callable[[Callable[P, Any]], Callable[P, Any]]:
            def check_accepts(f: Callable[P, Any]) -> Callable[P, Any]:
                # py2: assert len(types) == f.func_code.co_argcount
                from inspect import signature

                sig = signature(f)
                assert len(types) == len(sig.parameters)

                def new_f(*args: P.args, **kwds: P.kwargs) -> Any:
                    for a, t in zip(args, types):
                        assert isinstance(a, t), "arg %r does not match %s" % (a, t)
                    return f(*args, **kwds)

                # py2: new_f.func_name = f.func_name
                new_f.__name__ = f.__name__
                return new_f

            return check_accepts

        def returns(rtype: SomeTypes) -> Callable[[Callable[P, Any]], Callable[P, Any]]:
            def check_returns(f: Callable[P, Any]) -> Callable[P, Any]:
                def new_f(*args: P.args, **kwds: P.kwargs) -> Any:
                    result = f(*args, **kwds)
                    assert isinstance(result, rtype), "return value %r does not match %s" % (result, rtype)
                    return result

                # py2: new_f.func_name = f.func_name
                new_f.__name__ = f.__name__
                return new_f

            return check_returns

        @accepts(int, (int, float))
        @returns((int, float))
        def func(arg1: Any, arg2: Any) -> Any:
            return arg1 * arg2

        assert func(10, 10) == 100
        assert func(10, 0.25) == 2.5

        with pytest.raises(AssertionError) as ex:
            func(0.1, 0.1)

        assert str(ex.value) == (
            "arg 0.1 does not match <class 'int'>\n"
            + "assert False\n"
            + " +  where False = isinstance(0.1, <class 'int'>)"
        )

    def test_order_of_decorators_and_order_of_execution(self) -> None:
        """
        ```py
        @dec2
        @dec1
        def func(arg1, arg2, ...):
            pass
        ```

        This is equivalent to:

        ```py
        def func(arg1, arg2, ...):
            pass
        func = dec2(dec1(func))
        ```
        """

        def dec1(f: Callable[P, Any]) -> Callable[P, str]:
            def wrapper(*args: P.args, **kwds: P.kwargs) -> str:
                result = f(*args, **kwds)
                return f"[dec1 {result} ]"

            return wrapper

        def dec2(f: Callable[P, Any]) -> Callable[P, str]:
            def wrapper(*args: P.args, **kwds: P.kwargs) -> str:
                result = f(*args, **kwds)
                return f"<dec2 {result} >"

            return wrapper

        @dec2
        @dec1
        def func1() -> str:
            return "This is func1."

        @dec1
        @dec2
        def func2() -> str:
            return "This is func2."

        assert func1() == "<dec2 [dec1 This is func1. ] >"
        assert func2() == "[dec1 <dec2 This is func2. > ]"

    def test_use_functools_wraps(self) -> None:
        """
        @wraps is updates the wrapper function to look like the wrapped function.
        """

        def wrap(f: Callable[..., Any]) -> Callable[P, None]:
            def wrapper(*args: P.args, **kwds: P.kwargs) -> None:
                pass

            return wrapper

        def wrap_name(f: Callable[..., Any]) -> Callable[P, None]:
            def wrapper(*args: P.args, **kwds: P.kwargs) -> None:
                pass

            wrapper.__name__ = f.__name__
            return wrapper

        def wrap_functools(f: Callable[P, Any]) -> Callable[P, str]:
            @wraps(f)
            def wrapper(*args: P.args, **kwds: P.kwargs) -> str:
                result = f(*args, **kwds)
                return f"[ {result} ]"

            return wrapper

        @wrap
        def func1() -> None:
            pass

        assert func1.__name__ == "wrapper"

        @wrap_name
        def func2() -> None:
            pass

        assert func2.__name__ == "func2"

        @wrap_functools
        def func3() -> None:
            pass

        assert func3.__name__ == "func3"
