# Stubs for neomodel (Python 3)

from . import (cardinality, core, exceptions, match, match_q, properties,
               relationship, relationship_manager, util)

__author__: str
__email__: str
__license__: str
__version__: str

One = cardinality.One
OneOrMore = cardinality.OneOrMore
ZeroOrOne = cardinality.ZeroOrOne
ZeroOrMore = cardinality.ZeroOrMore

NodeBase = core.NodeBase
StructuredNode = core.StructuredNode
db = core.db
install_all_labels = core.install_all_labels
remove_all_labels = core.remove_all_labels

EITHER = match.EITHER
INCOMING = match.INCOMING
OUTGOING = match.OUTGOING
NodeSet = match.NodeSet
Traversal = match.Traversal

Q = match_q.Q

AliasProperty = properties.AliasProperty
ArrayProperty = properties.ArrayProperty
BooleanProperty = properties.BooleanProperty
DateProperty = properties.DateProperty
DateTimeProperty = properties.DateTimeProperty
DateTimeFormatProperty = properties.DateTimeFormatProperty
EmailProperty = properties.EmailProperty
FloatProperty = properties.FloatProperty
IntegerProperty = properties.IntegerProperty
JSONProperty = properties.JSONProperty
NormalizedProperty = properties.NormalizedProperty
RegexProperty = properties.RegexProperty
StringProperty = properties.StringProperty
UniqueIdProperty = properties.UniqueIdProperty

StructuredRel = relationship.StructuredRel

Relationship = relationship_manager.Relationship
RelationshipFrom = relationship_manager.RelationshipFrom
RelationshipTo = relationship_manager.RelationshipTo
RelationshipManager = relationship_manager.RelationshipManager
RelationshipDefinition = relationship_manager.RelationshipDefinition

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
