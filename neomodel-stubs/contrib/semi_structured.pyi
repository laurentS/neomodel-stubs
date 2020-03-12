# Stubs for neomodel.contrib.semi_structured (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from neomodel.core import StructuredNode
from typing import Any, Optional

class SemiStructuredNode(StructuredNode):
    __abstract_node__: bool = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @classmethod
    def inflate(cls, node: Any): ...
    @classmethod
    def deflate(cls, node_props: Any, obj: Optional[Any] = ..., skip_empty: bool = ...): ...
