# Stubs for neomodel.properties (Python 3)
import sys
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union

unicode = str

def display_for(key: Any): ...

class PropertyManager:
    def __init__(self, **kwargs: Any) -> None: ...
    @property
    def __properties__(self) -> Dict[str, Any]: ...
    @classmethod
    def deflate(
        cls, properties: Any, obj: Optional[Any] = ..., skip_empty: bool = ...
    ): ...
    @classmethod
    def defined_properties(
        cls, aliases: bool = ..., properties: bool = ..., rels: bool = ...
    ) -> Dict: ...
    # override __getattr__ to get the correct type for properties
    # source: https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html
    # (search "getattr")
    def __getattribute__(self, name: str) -> int: ...

def validator(fn: Any): ...

PropertyType = TypeVar("PropertyType")

class Property(Generic[PropertyType]):
    form_field_class: str = ...
    required: bool = ...
    unique_index: bool = ...
    index: bool = ...
    default: Optional[Union[PropertyType, Callable[..., PropertyType]]] = ...
    has_default: bool = ...
    db_property: str = ...
    label: Any = ...
    help_text: Any = ...
    def __init__(
        self,
        unique_index: bool = ...,
        index: bool = ...,
        required: bool = ...,
        default: Optional[Union[PropertyType, Callable[..., PropertyType]]] = ...,
        db_property: Optional[str] = ...,
        label: Optional[str] = ...,
        help_text: Optional[str] = ...,
        **kwargs: Any
    ) -> None: ...
    def default_value(self: "Property[PropertyType]") -> PropertyType: ...
    @property
    def is_indexed(self) -> bool: ...
    def __get__(*args: Any) -> PropertyType: ...

class NormalizedProperty(Property[PropertyType]):
    def inflate(self, value: PropertyType) -> PropertyType: ...
    def deflate(self, value: Any): ...
    def default_value(self) -> PropertyType: ...
    def normalize(self, value: Any): ...

if sys.version_info >= (3, 6):
    class NormalProperty(NormalizedProperty):
        def __init_subclass__(cls, **kwargs: Any) -> None: ...

else:
    class NormalProperty(NormalizedProperty):
        def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class RegexProperty(NormalizedProperty):
    form_field_class: str = ...
    expression: Any = ...
    def __init__(self, expression: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def normalize(self, value: Any): ...

class EmailProperty(RegexProperty):
    form_field_class: str = ...
    expression: str = ...

class StringProperty(NormalizedProperty[str]):
    choices: Any = ...
    form_field_class: str = ...
    def __init__(self, choices: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def normalize(self, value: str) -> str: ...
    def default_value(self) -> str: ...

class IntegerProperty(Property[int]):
    form_field_class: str = ...
    def inflate(self, value: Any) -> int: ...
    def deflate(self, value: Any) -> int: ...
    def default_value(self) -> int: ...

class ArrayProperty(Property[List]):
    base_property: Any = ...
    def __init__(self, base_property: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def inflate(self, value: Any): ...
    def deflate(self, value: Any): ...
    def default_value(self) -> List: ...

class FloatProperty(Property[float]):
    form_field_class: str = ...
    def inflate(self, value: Any) -> float: ...
    def deflate(self, value: Any) -> float: ...
    def default_value(self) -> float: ...

class BooleanProperty(Property[bool]):
    form_field_class: str = ...
    def inflate(self, value: Any) -> bool: ...
    def deflate(self, value: Any) -> bool: ...
    def default_value(self) -> bool: ...

class DateProperty(Property[date]):
    form_field_class: str = ...
    def inflate(self, value: Any): ...
    def deflate(self, value: Any): ...

class DateTimeProperty(Property[datetime]):
    form_field_class: str = ...
    def __init__(self, default_now: bool = ..., **kwargs: Any) -> None: ...
    def inflate(self, value: Any): ...
    def deflate(self, value: Any): ...

class JSONProperty(Property):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def inflate(self, value: Any): ...
    def deflate(self, value: Any): ...

class AliasProperty(property, Property):
    target: str = ...
    required: bool = ...
    has_default: bool = ...
    def __init__(self, to: str = ...) -> None: ...
    def aliased_to(self) -> str: ...
    def __get__(self, obj: Any, cls: Any): ...  # type: ignore
    def __set__(self, obj: Any, value: Any) -> None: ...
    @property
    def index(self) -> bool: ...
    @property
    def unique_index(self) -> bool: ...

class UniqueIdProperty(Property):
    def __init__(self, **kwargs: Any) -> None: ...
    def inflate(self, value: Any): ...
    def deflate(self, value: Any): ...
