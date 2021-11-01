from typing import Any, Callable, Type


def raises(err: Type[BaseException], lamda: Callable[[], Any]) -> bool:
    try:
        lamda()
        return False
    except err:
        return True


no_default = '__no__default__'
