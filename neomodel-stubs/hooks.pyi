# Stubs for neomodel.hooks (Python 3)

from typing import Any, Callable, TypeVar

F = TypeVar("F", bound=Callable[..., Any])

def hooks(fn: F) -> F: ...
