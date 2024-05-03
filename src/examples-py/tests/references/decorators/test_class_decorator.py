"""This test is for learning class decorators.

The semantics and design goals of class decorators are the same as
for function decorators (PEP 318);
the only difference is that you're decorating a class instead of a function.

References:
    - https://peps.python.org/pep-3129/

"""


class TestClassDecorator(object):
    def test_with_pep3129(self):
        """PEP 3129's class decorator."""

        def foo(cls):
            cls.foo_is = "FOO"
            return cls

        def bar(cls):
            cls.bar_is = "BAR"

            return cls

        class A:
            def __init__(self):
                self.param = "PARAM"

        a = foo(bar(A()))
        assert a.param == "PARAM"
        assert a.foo_is == "FOO"
        assert a.bar_is == "BAR"

        @foo
        @bar
        class B:
            def __init__(self):
                self.param = "PARAM"

        b = B()
        assert b.param == "PARAM"
        assert b.foo_is == "FOO"
        assert b.bar_is == "BAR"
