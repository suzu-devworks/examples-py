"""This test is for learning decorators for functions and methods.

Gof's Decorator pattern aims to "add new functionality and behavior to existing objects dynamically."

Decorators in Python are discussed in his PEP318 and PEP3129,
and extend their functionality by writing them into functions,
methods, and classes as syntactic sugar described in @metadata.

References:
    - https://peps.python.org/pep-0318/

"""  # noqa E501

# spell-checker:words Gof

from functools import wraps

import pytest


class TestDecorator(object):
    def test_without_arguments_not_return_wrapper(self):
        """Pattern of without arguments and not return a wrapper function.

        This is the pattern from Example 1 of PEP318.
        This pattern is almost impractical.
        """

        def on_exit(f):
            import atexit

            atexit.register(f)
            return f

        @on_exit
        def func():
            print("Exit on called.")

        # Called at normal program exit, e.g. when sys.exit() is called,
        # or when the main module completes execution.

        # `@atexit.register` is just a decorator.

    def test_without_arguments_return_wrapper(self):
        """Pattern of without arguments and return a wrapper function.

        This is the pattern from Example 2 of PEP318.
        The basic pattern, whether or not there is a return value, doesn't seem to matter.
        """

        def singleton(cls):
            instances = {}

            def get_instance():
                if cls not in instances:
                    instances[cls] = cls()
                return instances[cls]

            return get_instance

        @singleton
        class MyClass:
            pass

        object1 = MyClass()
        object2 = MyClass()
        assert object1 == object2
        assert object1 is object2

    def test_with_arguments_not_return_wrapper(self):
        """Pattern of with arguments and not return a wrapper function.

        This is the pattern from Example 3 of PEP318.
        The app/Flask.route function of flask seems to use this pattern.
        """

        def attrs(**kwds):
            def decorate(f):
                for k in kwds:
                    setattr(f, k, kwds[k])
                return f

            return decorate

        # spell-checker:words Rossum
        @attrs(versionadded="2.2", author="Guido van Rossum")
        def do_method(f):
            pass

        assert do_method.versionadded == "2.2"
        assert do_method.author == "Guido van Rossum"

    def test_with_arguments_return_wrapper(self):
        """Pattern of with arguments and return a wrapper function.

        This is the pattern from Example 4 of PEP318.
        """

        def accepts(*types):
            def check_accepts(f):
                # spell-checker:disable next lines
                # py2: assert len(types) == f.func_code.co_argcount
                from inspect import signature

                sig = signature(f)
                assert len(types) == len(sig.parameters)

                def new_f(*args, **kwds):
                    for a, t in zip(args, types):
                        assert isinstance(a, t), "arg %r does not match %s" % (a, t)
                    return f(*args, **kwds)

                # py2: new_f.func_name = f.func_name
                new_f.__name__ = f.__name__
                return new_f

            return check_accepts

        def returns(rtype):
            def check_returns(f):
                def new_f(*args, **kwds):
                    result = f(*args, **kwds)
                    assert isinstance(result, rtype), "return value %r does not match %s" % (result, rtype)
                    return result

                # py2: new_f.func_name = f.func_name
                new_f.__name__ = f.__name__
                return new_f

            return check_returns

        @accepts(int, (int, float))
        @returns((int, float))
        def func(arg1, arg2):
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

    def test_order_of_decorators_and_order_of_execution(self):
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

        def dec1(f):
            def wapper(*args, **kwds):
                result = f(*args, **kwds)
                return f"[dec1 {result} ]"

            return wapper

        def dec2(f):
            def wapper(*args, **kwds):
                result = f(*args, **kwds)
                return f"<dec2 {result} >"

            return wapper

        @dec2
        @dec1
        def func1():
            return "This is func1."

        @dec1
        @dec2
        def func2():
            return "This is func2."

        assert func1() == "<dec2 [dec1 This is func1. ] >"
        assert func2() == "[dec1 <dec2 This is func2. > ]"

    def test_use_functools_wraps(self):
        """`@wraps` is updates the wrapper function to look like the wrapped function."""

        def wrap(f):
            def wapper(*args, **kwds):
                pass

            return wapper

        def wrap_name(f):
            def wapper(*args, **kwds):
                pass

            wapper.__name__ = f.__name__
            return wapper

        def wrap_functools(f):
            @wraps(f)
            def wapper(*args, **kwds):
                result = f(*args, **kwds)
                return f"[ {result} ]"

            return wapper

        @wrap
        def func1():
            pass

        assert func1.__name__ == "wapper"

        @wrap_name
        def func2():
            pass

        assert func2.__name__ == "func2"

        @wrap_functools
        def func3():
            pass

        assert func3.__name__ == "func3"
