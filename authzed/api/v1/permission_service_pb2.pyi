"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import authzed.api.v1.core_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Consistency(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MINIMIZE_LATENCY_FIELD_NUMBER: builtins.int
    AT_LEAST_AS_FRESH_FIELD_NUMBER: builtins.int
    AT_EXACT_SNAPSHOT_FIELD_NUMBER: builtins.int
    FULLY_CONSISTENT_FIELD_NUMBER: builtins.int
    minimize_latency: builtins.bool = ...
    fully_consistent: builtins.bool = ...

    @property
    def at_least_as_fresh(self) -> authzed.api.v1.core_pb2.ZedToken: ...

    @property
    def at_exact_snapshot(self) -> authzed.api.v1.core_pb2.ZedToken: ...

    def __init__(self,
        *,
        minimize_latency : builtins.bool = ...,
        at_least_as_fresh : typing.Optional[authzed.api.v1.core_pb2.ZedToken] = ...,
        at_exact_snapshot : typing.Optional[authzed.api.v1.core_pb2.ZedToken] = ...,
        fully_consistent : builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"at_exact_snapshot",b"at_exact_snapshot",u"at_least_as_fresh",b"at_least_as_fresh",u"fully_consistent",b"fully_consistent",u"minimize_latency",b"minimize_latency",u"requirement",b"requirement"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"at_exact_snapshot",b"at_exact_snapshot",u"at_least_as_fresh",b"at_least_as_fresh",u"fully_consistent",b"fully_consistent",u"minimize_latency",b"minimize_latency",u"requirement",b"requirement"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"requirement",b"requirement"]) -> typing.Optional[typing_extensions.Literal["minimize_latency","at_least_as_fresh","at_exact_snapshot","fully_consistent"]]: ...
global___Consistency = Consistency

class RelationshipFilter(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_TYPE_FIELD_NUMBER: builtins.int
    OPTIONAL_RESOURCE_ID_FIELD_NUMBER: builtins.int
    OPTIONAL_RELATION_FIELD_NUMBER: builtins.int
    OPTIONAL_SUBJECT_FILTER_FIELD_NUMBER: builtins.int
    resource_type: typing.Text = ...
    optional_resource_id: typing.Text = ...
    optional_relation: typing.Text = ...

    @property
    def optional_subject_filter(self) -> global___SubjectFilter: ...

    def __init__(self,
        *,
        resource_type : typing.Text = ...,
        optional_resource_id : typing.Text = ...,
        optional_relation : typing.Text = ...,
        optional_subject_filter : typing.Optional[global___SubjectFilter] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"optional_subject_filter",b"optional_subject_filter"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"optional_relation",b"optional_relation",u"optional_resource_id",b"optional_resource_id",u"optional_subject_filter",b"optional_subject_filter",u"resource_type",b"resource_type"]) -> None: ...
global___RelationshipFilter = RelationshipFilter

class SubjectFilter(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class RelationFilter(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        RELATION_FIELD_NUMBER: builtins.int
        relation: typing.Text = ...

        def __init__(self,
            *,
            relation : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"relation",b"relation"]) -> None: ...

    SUBJECT_TYPE_FIELD_NUMBER: builtins.int
    OPTIONAL_SUBJECT_ID_FIELD_NUMBER: builtins.int
    OPTIONAL_RELATION_FIELD_NUMBER: builtins.int
    subject_type: typing.Text = ...
    optional_subject_id: typing.Text = ...

    @property
    def optional_relation(self) -> global___SubjectFilter.RelationFilter: ...

    def __init__(self,
        *,
        subject_type : typing.Text = ...,
        optional_subject_id : typing.Text = ...,
        optional_relation : typing.Optional[global___SubjectFilter.RelationFilter] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"optional_relation",b"optional_relation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"optional_relation",b"optional_relation",u"optional_subject_id",b"optional_subject_id",u"subject_type",b"subject_type"]) -> None: ...
global___SubjectFilter = SubjectFilter

class ReadRelationshipsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CONSISTENCY_FIELD_NUMBER: builtins.int
    RELATIONSHIP_FILTER_FIELD_NUMBER: builtins.int

    @property
    def consistency(self) -> global___Consistency: ...

    @property
    def relationship_filter(self) -> global___RelationshipFilter: ...

    def __init__(self,
        *,
        consistency : typing.Optional[global___Consistency] = ...,
        relationship_filter : typing.Optional[global___RelationshipFilter] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"consistency",b"consistency",u"relationship_filter",b"relationship_filter"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"consistency",b"consistency",u"relationship_filter",b"relationship_filter"]) -> None: ...
global___ReadRelationshipsRequest = ReadRelationshipsRequest

class ReadRelationshipsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    READ_AT_FIELD_NUMBER: builtins.int
    RELATIONSHIP_FIELD_NUMBER: builtins.int

    @property
    def read_at(self) -> authzed.api.v1.core_pb2.ZedToken: ...

    @property
    def relationship(self) -> authzed.api.v1.core_pb2.Relationship: ...

    def __init__(self,
        *,
        read_at : typing.Optional[authzed.api.v1.core_pb2.ZedToken] = ...,
        relationship : typing.Optional[authzed.api.v1.core_pb2.Relationship] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"read_at",b"read_at",u"relationship",b"relationship"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"read_at",b"read_at",u"relationship",b"relationship"]) -> None: ...
global___ReadRelationshipsResponse = ReadRelationshipsResponse

class Precondition(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Operation(metaclass=_Operation):
        V = typing.NewType('V', builtins.int)

    OPERATION_UNSPECIFIED = Precondition.Operation.V(0)
    OPERATION_MUST_NOT_MATCH = Precondition.Operation.V(1)
    OPERATION_MUST_MATCH = Precondition.Operation.V(2)

    class _Operation(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Operation.V], builtins.type):  # type: ignore
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        OPERATION_UNSPECIFIED = Precondition.Operation.V(0)
        OPERATION_MUST_NOT_MATCH = Precondition.Operation.V(1)
        OPERATION_MUST_MATCH = Precondition.Operation.V(2)

    OPERATION_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    operation: global___Precondition.Operation.V = ...

    @property
    def filter(self) -> global___RelationshipFilter: ...

    def __init__(self,
        *,
        operation : global___Precondition.Operation.V = ...,
        filter : typing.Optional[global___RelationshipFilter] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"filter",b"filter"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"filter",b"filter",u"operation",b"operation"]) -> None: ...
global___Precondition = Precondition

class WriteRelationshipsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    UPDATES_FIELD_NUMBER: builtins.int
    OPTIONAL_PRECONDITIONS_FIELD_NUMBER: builtins.int

    @property
    def updates(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[authzed.api.v1.core_pb2.RelationshipUpdate]: ...

    @property
    def optional_preconditions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Precondition]: ...

    def __init__(self,
        *,
        updates : typing.Optional[typing.Iterable[authzed.api.v1.core_pb2.RelationshipUpdate]] = ...,
        optional_preconditions : typing.Optional[typing.Iterable[global___Precondition]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"optional_preconditions",b"optional_preconditions",u"updates",b"updates"]) -> None: ...
global___WriteRelationshipsRequest = WriteRelationshipsRequest

class WriteRelationshipsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    WRITTEN_AT_FIELD_NUMBER: builtins.int

    @property
    def written_at(self) -> authzed.api.v1.core_pb2.ZedToken: ...

    def __init__(self,
        *,
        written_at : typing.Optional[authzed.api.v1.core_pb2.ZedToken] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"written_at",b"written_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"written_at",b"written_at"]) -> None: ...
global___WriteRelationshipsResponse = WriteRelationshipsResponse

class DeleteRelationshipsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RELATIONSHIP_FILTER_FIELD_NUMBER: builtins.int
    OPTIONAL_PRECONDITIONS_FIELD_NUMBER: builtins.int

    @property
    def relationship_filter(self) -> global___RelationshipFilter: ...

    @property
    def optional_preconditions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Precondition]: ...

    def __init__(self,
        *,
        relationship_filter : typing.Optional[global___RelationshipFilter] = ...,
        optional_preconditions : typing.Optional[typing.Iterable[global___Precondition]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"relationship_filter",b"relationship_filter"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"optional_preconditions",b"optional_preconditions",u"relationship_filter",b"relationship_filter"]) -> None: ...
global___DeleteRelationshipsRequest = DeleteRelationshipsRequest

class DeleteRelationshipsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DELETED_AT_FIELD_NUMBER: builtins.int

    @property
    def deleted_at(self) -> authzed.api.v1.core_pb2.ZedToken: ...

    def __init__(self,
        *,
        deleted_at : typing.Optional[authzed.api.v1.core_pb2.ZedToken] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"deleted_at",b"deleted_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"deleted_at",b"deleted_at"]) -> None: ...
global___DeleteRelationshipsResponse = DeleteRelationshipsResponse

class CheckPermissionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CONSISTENCY_FIELD_NUMBER: builtins.int
    RESOURCE_FIELD_NUMBER: builtins.int
    PERMISSION_FIELD_NUMBER: builtins.int
    SUBJECT_FIELD_NUMBER: builtins.int
    permission: typing.Text = ...

    @property
    def consistency(self) -> global___Consistency: ...

    @property
    def resource(self) -> authzed.api.v1.core_pb2.ObjectReference: ...

    @property
    def subject(self) -> authzed.api.v1.core_pb2.SubjectReference: ...

    def __init__(self,
        *,
        consistency : typing.Optional[global___Consistency] = ...,
        resource : typing.Optional[authzed.api.v1.core_pb2.ObjectReference] = ...,
        permission : typing.Text = ...,
        subject : typing.Optional[authzed.api.v1.core_pb2.SubjectReference] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"consistency",b"consistency",u"resource",b"resource",u"subject",b"subject"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"consistency",b"consistency",u"permission",b"permission",u"resource",b"resource",u"subject",b"subject"]) -> None: ...
global___CheckPermissionRequest = CheckPermissionRequest

class CheckPermissionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Permissionship(metaclass=_Permissionship):
        V = typing.NewType('V', builtins.int)

    PERMISSIONSHIP_UNSPECIFIED = CheckPermissionResponse.Permissionship.V(0)
    PERMISSIONSHIP_NO_PERMISSION = CheckPermissionResponse.Permissionship.V(1)
    PERMISSIONSHIP_HAS_PERMISSION = CheckPermissionResponse.Permissionship.V(2)

    class _Permissionship(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Permissionship.V], builtins.type):  # type: ignore
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        PERMISSIONSHIP_UNSPECIFIED = CheckPermissionResponse.Permissionship.V(0)
        PERMISSIONSHIP_NO_PERMISSION = CheckPermissionResponse.Permissionship.V(1)
        PERMISSIONSHIP_HAS_PERMISSION = CheckPermissionResponse.Permissionship.V(2)

    CHECKED_AT_FIELD_NUMBER: builtins.int
    PERMISSIONSHIP_FIELD_NUMBER: builtins.int
    permissionship: global___CheckPermissionResponse.Permissionship.V = ...

    @property
    def checked_at(self) -> authzed.api.v1.core_pb2.ZedToken: ...

    def __init__(self,
        *,
        checked_at : typing.Optional[authzed.api.v1.core_pb2.ZedToken] = ...,
        permissionship : global___CheckPermissionResponse.Permissionship.V = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"checked_at",b"checked_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"checked_at",b"checked_at",u"permissionship",b"permissionship"]) -> None: ...
global___CheckPermissionResponse = CheckPermissionResponse

class ExpandPermissionTreeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CONSISTENCY_FIELD_NUMBER: builtins.int
    RESOURCE_FIELD_NUMBER: builtins.int
    PERMISSION_FIELD_NUMBER: builtins.int
    permission: typing.Text = ...

    @property
    def consistency(self) -> global___Consistency: ...

    @property
    def resource(self) -> authzed.api.v1.core_pb2.ObjectReference: ...

    def __init__(self,
        *,
        consistency : typing.Optional[global___Consistency] = ...,
        resource : typing.Optional[authzed.api.v1.core_pb2.ObjectReference] = ...,
        permission : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"consistency",b"consistency",u"resource",b"resource"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"consistency",b"consistency",u"permission",b"permission",u"resource",b"resource"]) -> None: ...
global___ExpandPermissionTreeRequest = ExpandPermissionTreeRequest

class ExpandPermissionTreeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    EXPANDED_AT_FIELD_NUMBER: builtins.int
    TREE_ROOT_FIELD_NUMBER: builtins.int

    @property
    def expanded_at(self) -> authzed.api.v1.core_pb2.ZedToken: ...

    @property
    def tree_root(self) -> authzed.api.v1.core_pb2.PermissionRelationshipTree: ...

    def __init__(self,
        *,
        expanded_at : typing.Optional[authzed.api.v1.core_pb2.ZedToken] = ...,
        tree_root : typing.Optional[authzed.api.v1.core_pb2.PermissionRelationshipTree] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"expanded_at",b"expanded_at",u"tree_root",b"tree_root"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"expanded_at",b"expanded_at",u"tree_root",b"tree_root"]) -> None: ...
global___ExpandPermissionTreeResponse = ExpandPermissionTreeResponse

class LookupResourcesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CONSISTENCY_FIELD_NUMBER: builtins.int
    RESOURCE_OBJECT_TYPE_FIELD_NUMBER: builtins.int
    PERMISSION_FIELD_NUMBER: builtins.int
    SUBJECT_FIELD_NUMBER: builtins.int
    resource_object_type: typing.Text = ...
    permission: typing.Text = ...

    @property
    def consistency(self) -> global___Consistency: ...

    @property
    def subject(self) -> authzed.api.v1.core_pb2.SubjectReference: ...

    def __init__(self,
        *,
        consistency : typing.Optional[global___Consistency] = ...,
        resource_object_type : typing.Text = ...,
        permission : typing.Text = ...,
        subject : typing.Optional[authzed.api.v1.core_pb2.SubjectReference] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"consistency",b"consistency",u"subject",b"subject"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"consistency",b"consistency",u"permission",b"permission",u"resource_object_type",b"resource_object_type",u"subject",b"subject"]) -> None: ...
global___LookupResourcesRequest = LookupResourcesRequest

class LookupResourcesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    LOOKED_UP_AT_FIELD_NUMBER: builtins.int
    RESOURCE_OBJECT_ID_FIELD_NUMBER: builtins.int
    resource_object_id: typing.Text = ...

    @property
    def looked_up_at(self) -> authzed.api.v1.core_pb2.ZedToken: ...

    def __init__(self,
        *,
        looked_up_at : typing.Optional[authzed.api.v1.core_pb2.ZedToken] = ...,
        resource_object_id : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"looked_up_at",b"looked_up_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"looked_up_at",b"looked_up_at",u"resource_object_id",b"resource_object_id"]) -> None: ...
global___LookupResourcesResponse = LookupResourcesResponse
