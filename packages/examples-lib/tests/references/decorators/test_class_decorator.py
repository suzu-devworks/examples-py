"""This test is for learning class decorators.

The semantics and design goals of class decorators are the same as
for function decorators (PEP 318);
the only difference is that you're decorating a class instead of a function.

References:
    - https://peps.python.org/pep-3129/

"""

from typing import Any


def test_with_pep3129() -> None:
    """PEP 3129's class decorator."""

    def foo(cls: Any) -> Any:
        cls.foo_is = "FOO"
        return cls

    def bar(cls: Any) -> Any:
        cls.bar_is = "BAR"

        return cls

    class A:
        def __init__(self) -> None:
            self.param = "PARAM"

    a = foo(bar(A()))
    assert a.param == "PARAM"
    assert a.foo_is == "FOO"
    assert a.bar_is == "BAR"

    @foo
    @bar
    class B:
        def __init__(self) -> None:
            self.param = "PARAM"

    b = B()
    assert b.param == "PARAM"
    assert b.foo_is == "FOO"  # type: ignore[attr-defined]
    assert b.bar_is == "BAR"  # type: ignore[attr-defined]
