# Stubs for neomodel.relationship (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .core import db
from .hooks import hooks
from .properties import Property, PropertyManager
from .util import deprecated
from typing import Any

class RelationshipMeta(type):
    def __new__(mcs: Any, name: Any, bases: Any, dct: Any): ...

StructuredRelBase: Any

class StructuredRel(StructuredRelBase):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def save(self): ...
    def delete(self) -> None: ...
    def start_node(self): ...
    def end_node(self): ...
    @classmethod
    def inflate(cls, rel: Any): ...