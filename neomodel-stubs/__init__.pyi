# Stubs for neomodel (Python 3)

from . import (cardinality, core, exceptions, properties, relationship,
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

# Exceptions
AttemptedCardinalityViolation = exceptions.AttemptedCardinalityViolation
CardinalityViolation = exceptions.CardinalityViolation
ClassAlreadyDefined = exceptions.ClassAlreadyDefined
ConstraintValidationFailed = exceptions.ConstraintValidationFailed
DeflateConflict = exceptions.DeflateConflict
DeflateError = exceptions.DeflateError
DoesNotExist = exceptions.DoesNotExist
InflateConflict = exceptions.InflateConflict
InflateError = exceptions.InflateError
ModelDefinitionMismatch = exceptions.ModelDefinitionMismatch
MultipleNodesReturned = exceptions.MultipleNodesReturned
NeomodelException = exceptions.NeomodelException
NotConnected = exceptions.NotConnected
RequiredProperty = exceptions.RequiredProperty
UniqueProperty = exceptions.UniqueProperty
