"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import authzed.api.v1.permission_service_pb2
import collections.abc
import grpc
import grpc.aio
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class PermissionsServiceStub:
    """PermissionsService implements a set of RPCs that perform operations on
    relationships and permissions.
    """

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    ReadRelationships: grpc.UnaryStreamMultiCallable[
        authzed.api.v1.permission_service_pb2.ReadRelationshipsRequest,
        authzed.api.v1.permission_service_pb2.ReadRelationshipsResponse,
    ]
    """ReadRelationships reads a set of the relationships matching one or more
    filters.
    """

    WriteRelationships: grpc.UnaryUnaryMultiCallable[
        authzed.api.v1.permission_service_pb2.WriteRelationshipsRequest,
        authzed.api.v1.permission_service_pb2.WriteRelationshipsResponse,
    ]
    """WriteRelationships atomically writes and/or deletes a set of specified
    relationships. An optional set of preconditions can be provided that must
    be satisfied for the operation to commit.
    """

    DeleteRelationships: grpc.UnaryUnaryMultiCallable[
        authzed.api.v1.permission_service_pb2.DeleteRelationshipsRequest,
        authzed.api.v1.permission_service_pb2.DeleteRelationshipsResponse,
    ]
    """DeleteRelationships atomically bulk deletes all relationships matching the
    provided filter. If no relationships match, none will be deleted and the
    operation will succeed. An optional set of preconditions can be provided that must
    be satisfied for the operation to commit.
    """

    CheckPermission: grpc.UnaryUnaryMultiCallable[
        authzed.api.v1.permission_service_pb2.CheckPermissionRequest,
        authzed.api.v1.permission_service_pb2.CheckPermissionResponse,
    ]
    """CheckPermission determines for a given resource whether a subject computes
    to having a permission or is a direct member of a particular relation.
    """

    CheckBulkPermissions: grpc.UnaryUnaryMultiCallable[
        authzed.api.v1.permission_service_pb2.CheckBulkPermissionsRequest,
        authzed.api.v1.permission_service_pb2.CheckBulkPermissionsResponse,
    ]
    """CheckBulkPermissions evaluates the given list of permission checks
    and returns the list of results.
    """

    ExpandPermissionTree: grpc.UnaryUnaryMultiCallable[
        authzed.api.v1.permission_service_pb2.ExpandPermissionTreeRequest,
        authzed.api.v1.permission_service_pb2.ExpandPermissionTreeResponse,
    ]
    """ExpandPermissionTree reveals the graph structure for a resource's
    permission or relation. This RPC does not recurse infinitely deep and may
    require multiple calls to fully unnest a deeply nested graph.
    """

    LookupResources: grpc.UnaryStreamMultiCallable[
        authzed.api.v1.permission_service_pb2.LookupResourcesRequest,
        authzed.api.v1.permission_service_pb2.LookupResourcesResponse,
    ]
    """LookupResources returns all the resources of a given type that a subject
    can access whether via a computed permission or relation membership.
    """

    LookupSubjects: grpc.UnaryStreamMultiCallable[
        authzed.api.v1.permission_service_pb2.LookupSubjectsRequest,
        authzed.api.v1.permission_service_pb2.LookupSubjectsResponse,
    ]
    """LookupSubjects returns all the subjects of a given type that
    have access whether via a computed permission or relation membership.
    """

class PermissionsServiceAsyncStub:
    """PermissionsService implements a set of RPCs that perform operations on
    relationships and permissions.
    """

    ReadRelationships: grpc.aio.UnaryStreamMultiCallable[
        authzed.api.v1.permission_service_pb2.ReadRelationshipsRequest,
        authzed.api.v1.permission_service_pb2.ReadRelationshipsResponse,
    ]
    """ReadRelationships reads a set of the relationships matching one or more
    filters.
    """

    WriteRelationships: grpc.aio.UnaryUnaryMultiCallable[
        authzed.api.v1.permission_service_pb2.WriteRelationshipsRequest,
        authzed.api.v1.permission_service_pb2.WriteRelationshipsResponse,
    ]
    """WriteRelationships atomically writes and/or deletes a set of specified
    relationships. An optional set of preconditions can be provided that must
    be satisfied for the operation to commit.
    """

    DeleteRelationships: grpc.aio.UnaryUnaryMultiCallable[
        authzed.api.v1.permission_service_pb2.DeleteRelationshipsRequest,
        authzed.api.v1.permission_service_pb2.DeleteRelationshipsResponse,
    ]
    """DeleteRelationships atomically bulk deletes all relationships matching the
    provided filter. If no relationships match, none will be deleted and the
    operation will succeed. An optional set of preconditions can be provided that must
    be satisfied for the operation to commit.
    """

    CheckPermission: grpc.aio.UnaryUnaryMultiCallable[
        authzed.api.v1.permission_service_pb2.CheckPermissionRequest,
        authzed.api.v1.permission_service_pb2.CheckPermissionResponse,
    ]
    """CheckPermission determines for a given resource whether a subject computes
    to having a permission or is a direct member of a particular relation.
    """

    CheckBulkPermissions: grpc.aio.UnaryUnaryMultiCallable[
        authzed.api.v1.permission_service_pb2.CheckBulkPermissionsRequest,
        authzed.api.v1.permission_service_pb2.CheckBulkPermissionsResponse,
    ]
    """CheckBulkPermissions evaluates the given list of permission checks
    and returns the list of results.
    """

    ExpandPermissionTree: grpc.aio.UnaryUnaryMultiCallable[
        authzed.api.v1.permission_service_pb2.ExpandPermissionTreeRequest,
        authzed.api.v1.permission_service_pb2.ExpandPermissionTreeResponse,
    ]
    """ExpandPermissionTree reveals the graph structure for a resource's
    permission or relation. This RPC does not recurse infinitely deep and may
    require multiple calls to fully unnest a deeply nested graph.
    """

    LookupResources: grpc.aio.UnaryStreamMultiCallable[
        authzed.api.v1.permission_service_pb2.LookupResourcesRequest,
        authzed.api.v1.permission_service_pb2.LookupResourcesResponse,
    ]
    """LookupResources returns all the resources of a given type that a subject
    can access whether via a computed permission or relation membership.
    """

    LookupSubjects: grpc.aio.UnaryStreamMultiCallable[
        authzed.api.v1.permission_service_pb2.LookupSubjectsRequest,
        authzed.api.v1.permission_service_pb2.LookupSubjectsResponse,
    ]
    """LookupSubjects returns all the subjects of a given type that
    have access whether via a computed permission or relation membership.
    """

class PermissionsServiceServicer(metaclass=abc.ABCMeta):
    """PermissionsService implements a set of RPCs that perform operations on
    relationships and permissions.
    """

    @abc.abstractmethod
    def ReadRelationships(
        self,
        request: authzed.api.v1.permission_service_pb2.ReadRelationshipsRequest,
        context: _ServicerContext,
    ) -> typing.Union[collections.abc.Iterator[authzed.api.v1.permission_service_pb2.ReadRelationshipsResponse], collections.abc.AsyncIterator[authzed.api.v1.permission_service_pb2.ReadRelationshipsResponse]]:
        """ReadRelationships reads a set of the relationships matching one or more
        filters.
        """

    @abc.abstractmethod
    def WriteRelationships(
        self,
        request: authzed.api.v1.permission_service_pb2.WriteRelationshipsRequest,
        context: _ServicerContext,
    ) -> typing.Union[authzed.api.v1.permission_service_pb2.WriteRelationshipsResponse, collections.abc.Awaitable[authzed.api.v1.permission_service_pb2.WriteRelationshipsResponse]]:
        """WriteRelationships atomically writes and/or deletes a set of specified
        relationships. An optional set of preconditions can be provided that must
        be satisfied for the operation to commit.
        """

    @abc.abstractmethod
    def DeleteRelationships(
        self,
        request: authzed.api.v1.permission_service_pb2.DeleteRelationshipsRequest,
        context: _ServicerContext,
    ) -> typing.Union[authzed.api.v1.permission_service_pb2.DeleteRelationshipsResponse, collections.abc.Awaitable[authzed.api.v1.permission_service_pb2.DeleteRelationshipsResponse]]:
        """DeleteRelationships atomically bulk deletes all relationships matching the
        provided filter. If no relationships match, none will be deleted and the
        operation will succeed. An optional set of preconditions can be provided that must
        be satisfied for the operation to commit.
        """

    @abc.abstractmethod
    def CheckPermission(
        self,
        request: authzed.api.v1.permission_service_pb2.CheckPermissionRequest,
        context: _ServicerContext,
    ) -> typing.Union[authzed.api.v1.permission_service_pb2.CheckPermissionResponse, collections.abc.Awaitable[authzed.api.v1.permission_service_pb2.CheckPermissionResponse]]:
        """CheckPermission determines for a given resource whether a subject computes
        to having a permission or is a direct member of a particular relation.
        """

    @abc.abstractmethod
    def CheckBulkPermissions(
        self,
        request: authzed.api.v1.permission_service_pb2.CheckBulkPermissionsRequest,
        context: _ServicerContext,
    ) -> typing.Union[authzed.api.v1.permission_service_pb2.CheckBulkPermissionsResponse, collections.abc.Awaitable[authzed.api.v1.permission_service_pb2.CheckBulkPermissionsResponse]]:
        """CheckBulkPermissions evaluates the given list of permission checks
        and returns the list of results.
        """

    @abc.abstractmethod
    def ExpandPermissionTree(
        self,
        request: authzed.api.v1.permission_service_pb2.ExpandPermissionTreeRequest,
        context: _ServicerContext,
    ) -> typing.Union[authzed.api.v1.permission_service_pb2.ExpandPermissionTreeResponse, collections.abc.Awaitable[authzed.api.v1.permission_service_pb2.ExpandPermissionTreeResponse]]:
        """ExpandPermissionTree reveals the graph structure for a resource's
        permission or relation. This RPC does not recurse infinitely deep and may
        require multiple calls to fully unnest a deeply nested graph.
        """

    @abc.abstractmethod
    def LookupResources(
        self,
        request: authzed.api.v1.permission_service_pb2.LookupResourcesRequest,
        context: _ServicerContext,
    ) -> typing.Union[collections.abc.Iterator[authzed.api.v1.permission_service_pb2.LookupResourcesResponse], collections.abc.AsyncIterator[authzed.api.v1.permission_service_pb2.LookupResourcesResponse]]:
        """LookupResources returns all the resources of a given type that a subject
        can access whether via a computed permission or relation membership.
        """

    @abc.abstractmethod
    def LookupSubjects(
        self,
        request: authzed.api.v1.permission_service_pb2.LookupSubjectsRequest,
        context: _ServicerContext,
    ) -> typing.Union[collections.abc.Iterator[authzed.api.v1.permission_service_pb2.LookupSubjectsResponse], collections.abc.AsyncIterator[authzed.api.v1.permission_service_pb2.LookupSubjectsResponse]]:
        """LookupSubjects returns all the subjects of a given type that
        have access whether via a computed permission or relation membership.
        """

def add_PermissionsServiceServicer_to_server(servicer: PermissionsServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
