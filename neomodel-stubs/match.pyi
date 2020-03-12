# Stubs for neomodel.match (Python 3)
#

from typing import Any, Generic, List, Optional

from .core import NodeBase, StructuredNode

OUTGOING: Any
INCOMING: Any
EITHER: Any
basestring = str
OPERATOR_TABLE: Any

def _rel_helper(
    lhs,
    hrs,
    ident,
    relation_type: Optional[str],
    direction,
    relation_properties,
    **kwargs
) -> str: ...
def install_traversals(cls, node_set: Any) -> None: ...
def process_filter_args(cls, kwargs: Any): ...
def process_has_args(cls, kwargs: Any): ...

class QueryBuilder:
    node_set: Any = ...
    def __init__(self, node_set: Any) -> None: ...
    def build_ast(self): ...
    def build_source(self, source: Any): ...
    def create_ident(self): ...
    def build_order_by(self, ident: Any, source: Any) -> None: ...
    def build_traversal(self, traversal: Any): ...
    def build_node(self, node: Any): ...
    def build_label(self, ident: Any, cls: Any): ...
    def build_additional_match(self, ident: Any, node_set: Any) -> None: ...
    def build_where_stmt(
        self,
        ident: Any,
        filters: Any,
        q_filters: Optional[Any] = ...,
        source_class: Optional[Any] = ...,
    ) -> None: ...
    def build_query(self): ...

T = TypeVar("T")

class BaseSet(Generic[T]):
    query_cls: QueryBuilder = ...
    def all(self, lazy: bool = ...) -> List[T]: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def __nonzero__(self) -> bool: ...
    def __contains__(self, obj: Any): ...
    limit: Any = ...
    skip: Any = ...
    def __getitem__(self, key: Any) -> T: ...

class NodeSet(BaseSet[T]):
    source: T = ...
    source_class: Any = ...
    filters: Any = ...
    q_filters: Any = ...
    must_match: Any = ...
    dont_match: Any = ...
    def __init__(self, source: T) -> None: ...
    def get(self: "NodeSet[Type[T]]", lazy: bool = ..., **kwargs: Any) -> T: ...
    def get_or_none(self, **kwargs: Any) -> Optional[T]: ...
    def first(self, **kwargs: Any) -> NodeBase[T]: ...
    def first_or_none(self, **kwargs: Any): ...
    def filter(self, *args: Any, **kwargs: Any): ...
    def exclude(self, *args: Any, **kwargs: Any): ...
    def has(self, **kwargs: Any): ...
    def order_by(self, *props: Any): ...

class Traversal(BaseSet):
    source: Any = ...
    source_class: Any = ...
    definition: Any = ...
    target_class: Any = ...
    name: Any = ...
    filters: Any = ...
    def __init__(self, source: Any, name: Any, definition: Any) -> None: ...
    def match(self, **kwargs: Any): ...
