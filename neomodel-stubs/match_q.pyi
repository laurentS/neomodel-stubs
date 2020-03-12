# Stubs for neomodel.match_q (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class QBase:
    default: str = ...
    children: Any = ...
    connector: Any = ...
    negated: Any = ...
    def __init__(self, children: Optional[Any] = ..., connector: Optional[Any] = ..., negated: bool = ...) -> None: ...
    def __deepcopy__(self, memodict: Any): ...
    def __len__(self): ...
    def __bool__(self): ...
    def __contains__(self, other: Any): ...
    def __eq__(self, other: Any): ...
    def __hash__(self): ...
    def add(self, data: Any, conn_type: Any, squash: bool = ...): ...
    def negate(self) -> None: ...

class Q(QBase):
    AND: str = ...
    OR: str = ...
    default: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __or__(self, other: Any): ...
    def __and__(self, other: Any): ...
    def __invert__(self): ...
