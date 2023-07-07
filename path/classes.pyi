from typing import Any, Callable, Optional


class ClassProperty(property):
    def __get__(self, cls: Any, owner: Optional[type] = ...) -> Any:
        ...


class multimethod:
    def __init__(self, func: Callable[..., Any]):
        ...

    def __get__(self, instance: Any, owner: Optional[type]) -> Any:
        ...
