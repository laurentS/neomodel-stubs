# Stubs for neomodel (Python 3)

from . import (cardinality, core, properties, relationship,
               relationship_manager, util)

__email__: str
__license__: str

One = cardinality.One
OneOrMore = cardinality.OneOrMore
ZeroOrOne = cardinality.ZeroOrOne

NodeBase = core.NodeBase
StructuredNode = core.StructuredNode
db = core.db
install_all_labels = core.install_all_labels
remove_all_labels = core.remove_all_labels

ArrayProperty = properties.ArrayProperty
BooleanProperty = properties.BooleanProperty
DateProperty = properties.DateProperty
DateTimeProperty = properties.DateTimeProperty
FloatProperty = properties.FloatProperty
IntegerProperty = properties.IntegerProperty
StringProperty = properties.StringProperty
UniqueIdProperty = properties.UniqueIdProperty

StructuredRel = relationship.StructuredRel

RelationshipFrom = relationship_manager.RelationshipFrom
RelationshipTo = relationship_manager.RelationshipTo

change_neo4j_password = util.change_neo4j_password
clear_neo4j_database = util.clear_neo4j_database
