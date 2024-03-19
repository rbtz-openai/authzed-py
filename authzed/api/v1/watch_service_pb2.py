# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: authzed/api/v1/watch_service.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from validate import validate_pb2 as validate_dot_validate__pb2
from authzed.api.v1 import core_pb2 as authzed_dot_api_dot_v1_dot_core__pb2
from authzed.api.v1 import permission_service_pb2 as authzed_dot_api_dot_v1_dot_permission__service__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"authzed/api/v1/watch_service.proto\x12\x0e\x61uthzed.api.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17validate/validate.proto\x1a\x19\x61uthzed/api/v1/core.proto\x1a\'authzed/api/v1/permission_service.proto\"\xca\x02\n\x0cWatchRequest\x12\x83\x01\n\x15optional_object_types\x18\x01 \x03(\tBO\xfa\x42L\x92\x01I\x08\x00\"ErC(\x80\x01\x32>^([a-z][a-z0-9_]{1,62}[a-z0-9]/)*[a-z][a-z0-9_]{1,62}[a-z0-9]$R\x13optionalObjectTypes\x12L\n\x15optional_start_cursor\x18\x02 \x01(\x0b\x32\x18.authzed.api.v1.ZedTokenR\x13optionalStartCursor\x12\x66\n\x1doptional_relationship_filters\x18\x03 \x03(\x0b\x32\".authzed.api.v1.RelationshipFilterR\x1boptionalRelationshipFilters\"\x90\x01\n\rWatchResponse\x12<\n\x07updates\x18\x01 \x03(\x0b\x32\".authzed.api.v1.RelationshipUpdateR\x07updates\x12\x41\n\x0f\x63hanges_through\x18\x02 \x01(\x0b\x32\x18.authzed.api.v1.ZedTokenR\x0e\x63hangesThrough2l\n\x0cWatchService\x12\\\n\x05Watch\x12\x1c.authzed.api.v1.WatchRequest\x1a\x1d.authzed.api.v1.WatchResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\"\t/v1/watch:\x01*0\x01\x42H\n\x12\x63om.authzed.api.v1Z2github.com/authzed/authzed-go/proto/authzed/api/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'authzed.api.v1.watch_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\022com.authzed.api.v1Z2github.com/authzed/authzed-go/proto/authzed/api/v1'
  _globals['_WATCHREQUEST'].fields_by_name['optional_object_types']._options = None
  _globals['_WATCHREQUEST'].fields_by_name['optional_object_types']._serialized_options = b'\372BL\222\001I\010\000\"ErC(\200\0012>^([a-z][a-z0-9_]{1,62}[a-z0-9]/)*[a-z][a-z0-9_]{1,62}[a-z0-9]$'
  _globals['_WATCHSERVICE'].methods_by_name['Watch']._options = None
  _globals['_WATCHSERVICE'].methods_by_name['Watch']._serialized_options = b'\202\323\344\223\002\016\"\t/v1/watch:\001*'
  _globals['_WATCHREQUEST']._serialized_start=178
  _globals['_WATCHREQUEST']._serialized_end=508
  _globals['_WATCHRESPONSE']._serialized_start=511
  _globals['_WATCHRESPONSE']._serialized_end=655
  _globals['_WATCHSERVICE']._serialized_start=657
  _globals['_WATCHSERVICE']._serialized_end=765
# @@protoc_insertion_point(module_scope)
