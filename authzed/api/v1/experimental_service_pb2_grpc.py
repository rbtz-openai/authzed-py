# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from authzed.api.v1 import experimental_service_pb2 as authzed_dot_api_dot_v1_dot_experimental__service__pb2


class ExperimentalServiceStub(object):
    """ExperimentalService exposes a number of APIs that are currently being
    prototyped and tested for future inclusion in the stable API.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.BulkImportRelationships = channel.stream_unary(
                '/authzed.api.v1.ExperimentalService/BulkImportRelationships',
                request_serializer=authzed_dot_api_dot_v1_dot_experimental__service__pb2.BulkImportRelationshipsRequest.SerializeToString,
                response_deserializer=authzed_dot_api_dot_v1_dot_experimental__service__pb2.BulkImportRelationshipsResponse.FromString,
                )
        self.BulkExportRelationships = channel.unary_stream(
                '/authzed.api.v1.ExperimentalService/BulkExportRelationships',
                request_serializer=authzed_dot_api_dot_v1_dot_experimental__service__pb2.BulkExportRelationshipsRequest.SerializeToString,
                response_deserializer=authzed_dot_api_dot_v1_dot_experimental__service__pb2.BulkExportRelationshipsResponse.FromString,
                )
        self.BulkCheckPermission = channel.unary_unary(
                '/authzed.api.v1.ExperimentalService/BulkCheckPermission',
                request_serializer=authzed_dot_api_dot_v1_dot_experimental__service__pb2.BulkCheckPermissionRequest.SerializeToString,
                response_deserializer=authzed_dot_api_dot_v1_dot_experimental__service__pb2.BulkCheckPermissionResponse.FromString,
                )
        self.ExperimentalReflectSchema = channel.unary_unary(
                '/authzed.api.v1.ExperimentalService/ExperimentalReflectSchema',
                request_serializer=authzed_dot_api_dot_v1_dot_experimental__service__pb2.ExperimentalReflectSchemaRequest.SerializeToString,
                response_deserializer=authzed_dot_api_dot_v1_dot_experimental__service__pb2.ExperimentalReflectSchemaResponse.FromString,
                )
        self.ExperimentalComputablePermissions = channel.unary_unary(
                '/authzed.api.v1.ExperimentalService/ExperimentalComputablePermissions',
                request_serializer=authzed_dot_api_dot_v1_dot_experimental__service__pb2.ExperimentalComputablePermissionsRequest.SerializeToString,
                response_deserializer=authzed_dot_api_dot_v1_dot_experimental__service__pb2.ExperimentalComputablePermissionsResponse.FromString,
                )
        self.ExperimentalDependentRelations = channel.unary_unary(
                '/authzed.api.v1.ExperimentalService/ExperimentalDependentRelations',
                request_serializer=authzed_dot_api_dot_v1_dot_experimental__service__pb2.ExperimentalDependentRelationsRequest.SerializeToString,
                response_deserializer=authzed_dot_api_dot_v1_dot_experimental__service__pb2.ExperimentalDependentRelationsResponse.FromString,
                )
        self.ExperimentalDiffSchema = channel.unary_unary(
                '/authzed.api.v1.ExperimentalService/ExperimentalDiffSchema',
                request_serializer=authzed_dot_api_dot_v1_dot_experimental__service__pb2.ExperimentalDiffSchemaRequest.SerializeToString,
                response_deserializer=authzed_dot_api_dot_v1_dot_experimental__service__pb2.ExperimentalDiffSchemaResponse.FromString,
                )


class ExperimentalServiceServicer(object):
    """ExperimentalService exposes a number of APIs that are currently being
    prototyped and tested for future inclusion in the stable API.
    """

    def BulkImportRelationships(self, request_iterator, context):
        """BulkImportRelationships is a faster path to writing a large number of
        relationships at once. It is both batched and streaming. For maximum
        performance, the caller should attempt to write relationships in as close
        to relationship sort order as possible: (resource.object_type,
        resource.object_id, relation, subject.object.object_type,
        subject.object.object_id, subject.optional_relation)

        EXPERIMENTAL
        https://github.com/authzed/spicedb/issues/1303
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BulkExportRelationships(self, request, context):
        """BulkExportRelationships is the fastest path available to exporting
        relationships from the server. It is resumable, and will return results
        in an order determined by the server.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BulkCheckPermission(self, request, context):
        """NOTE: BulkCheckPermission has been promoted to the stable API as "CheckBulkPermission" and the
        API will be removed from experimental in a future release.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExperimentalReflectSchema(self, request, context):
        """EXPERIMENTAL: ReflectSchema is an API that allows clients to reflect the schema stored in
        SpiceDB. This is useful for clients that need to introspect the schema of a SpiceDB instance.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExperimentalComputablePermissions(self, request, context):
        """EXPERIMENTAL: ComputablePermissions is an API that allows clients to request the set of
        permissions that compute based off a relation. For example, if a schema has a relation
        `viewer` and a permission `view` defined as `permission view = viewer + editor`, then the
        computable permissions for the relation `viewer` will include `view`.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExperimentalDependentRelations(self, request, context):
        """EXPERIMENTAL: DependentRelations is an API that allows clients to request the set of
        relations and permissions that used to compute a permission, recursively. It is the
        inverse of the ComputablePermissions API.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExperimentalDiffSchema(self, request, context):
        """EXPERIMENTAL: DiffSchema is an API that allows clients to request the difference between the
        specified schema and the schema stored in SpiceDB. This is useful for clients that need to
        introspect the schema of a SpiceDB instance.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ExperimentalServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'BulkImportRelationships': grpc.stream_unary_rpc_method_handler(
                    servicer.BulkImportRelationships,
                    request_deserializer=authzed_dot_api_dot_v1_dot_experimental__service__pb2.BulkImportRelationshipsRequest.FromString,
                    response_serializer=authzed_dot_api_dot_v1_dot_experimental__service__pb2.BulkImportRelationshipsResponse.SerializeToString,
            ),
            'BulkExportRelationships': grpc.unary_stream_rpc_method_handler(
                    servicer.BulkExportRelationships,
                    request_deserializer=authzed_dot_api_dot_v1_dot_experimental__service__pb2.BulkExportRelationshipsRequest.FromString,
                    response_serializer=authzed_dot_api_dot_v1_dot_experimental__service__pb2.BulkExportRelationshipsResponse.SerializeToString,
            ),
            'BulkCheckPermission': grpc.unary_unary_rpc_method_handler(
                    servicer.BulkCheckPermission,
                    request_deserializer=authzed_dot_api_dot_v1_dot_experimental__service__pb2.BulkCheckPermissionRequest.FromString,
                    response_serializer=authzed_dot_api_dot_v1_dot_experimental__service__pb2.BulkCheckPermissionResponse.SerializeToString,
            ),
            'ExperimentalReflectSchema': grpc.unary_unary_rpc_method_handler(
                    servicer.ExperimentalReflectSchema,
                    request_deserializer=authzed_dot_api_dot_v1_dot_experimental__service__pb2.ExperimentalReflectSchemaRequest.FromString,
                    response_serializer=authzed_dot_api_dot_v1_dot_experimental__service__pb2.ExperimentalReflectSchemaResponse.SerializeToString,
            ),
            'ExperimentalComputablePermissions': grpc.unary_unary_rpc_method_handler(
                    servicer.ExperimentalComputablePermissions,
                    request_deserializer=authzed_dot_api_dot_v1_dot_experimental__service__pb2.ExperimentalComputablePermissionsRequest.FromString,
                    response_serializer=authzed_dot_api_dot_v1_dot_experimental__service__pb2.ExperimentalComputablePermissionsResponse.SerializeToString,
            ),
            'ExperimentalDependentRelations': grpc.unary_unary_rpc_method_handler(
                    servicer.ExperimentalDependentRelations,
                    request_deserializer=authzed_dot_api_dot_v1_dot_experimental__service__pb2.ExperimentalDependentRelationsRequest.FromString,
                    response_serializer=authzed_dot_api_dot_v1_dot_experimental__service__pb2.ExperimentalDependentRelationsResponse.SerializeToString,
            ),
            'ExperimentalDiffSchema': grpc.unary_unary_rpc_method_handler(
                    servicer.ExperimentalDiffSchema,
                    request_deserializer=authzed_dot_api_dot_v1_dot_experimental__service__pb2.ExperimentalDiffSchemaRequest.FromString,
                    response_serializer=authzed_dot_api_dot_v1_dot_experimental__service__pb2.ExperimentalDiffSchemaResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'authzed.api.v1.ExperimentalService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ExperimentalService(object):
    """ExperimentalService exposes a number of APIs that are currently being
    prototyped and tested for future inclusion in the stable API.
    """

    @staticmethod
    def BulkImportRelationships(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/authzed.api.v1.ExperimentalService/BulkImportRelationships',
            authzed_dot_api_dot_v1_dot_experimental__service__pb2.BulkImportRelationshipsRequest.SerializeToString,
            authzed_dot_api_dot_v1_dot_experimental__service__pb2.BulkImportRelationshipsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BulkExportRelationships(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/authzed.api.v1.ExperimentalService/BulkExportRelationships',
            authzed_dot_api_dot_v1_dot_experimental__service__pb2.BulkExportRelationshipsRequest.SerializeToString,
            authzed_dot_api_dot_v1_dot_experimental__service__pb2.BulkExportRelationshipsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BulkCheckPermission(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/authzed.api.v1.ExperimentalService/BulkCheckPermission',
            authzed_dot_api_dot_v1_dot_experimental__service__pb2.BulkCheckPermissionRequest.SerializeToString,
            authzed_dot_api_dot_v1_dot_experimental__service__pb2.BulkCheckPermissionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExperimentalReflectSchema(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/authzed.api.v1.ExperimentalService/ExperimentalReflectSchema',
            authzed_dot_api_dot_v1_dot_experimental__service__pb2.ExperimentalReflectSchemaRequest.SerializeToString,
            authzed_dot_api_dot_v1_dot_experimental__service__pb2.ExperimentalReflectSchemaResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExperimentalComputablePermissions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/authzed.api.v1.ExperimentalService/ExperimentalComputablePermissions',
            authzed_dot_api_dot_v1_dot_experimental__service__pb2.ExperimentalComputablePermissionsRequest.SerializeToString,
            authzed_dot_api_dot_v1_dot_experimental__service__pb2.ExperimentalComputablePermissionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExperimentalDependentRelations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/authzed.api.v1.ExperimentalService/ExperimentalDependentRelations',
            authzed_dot_api_dot_v1_dot_experimental__service__pb2.ExperimentalDependentRelationsRequest.SerializeToString,
            authzed_dot_api_dot_v1_dot_experimental__service__pb2.ExperimentalDependentRelationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExperimentalDiffSchema(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/authzed.api.v1.ExperimentalService/ExperimentalDiffSchema',
            authzed_dot_api_dot_v1_dot_experimental__service__pb2.ExperimentalDiffSchemaRequest.SerializeToString,
            authzed_dot_api_dot_v1_dot_experimental__service__pb2.ExperimentalDiffSchemaResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
