# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/base/snapshots/v1beta1/snapshot.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="cosmos/base/snapshots/v1beta1/snapshot.proto",
    package="cosmos.base.snapshots.v1beta1",
    syntax="proto3",
    serialized_options=b"Z,github.com/cosmos/cosmos-sdk/snapshots/types",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n,cosmos/base/snapshots/v1beta1/snapshot.proto\x12\x1d\x63osmos.base.snapshots.v1beta1\x1a\x14gogoproto/gogo.proto"\x89\x01\n\x08Snapshot\x12\x0e\n\x06height\x18\x01 \x01(\x04\x12\x0e\n\x06\x66ormat\x18\x02 \x01(\r\x12\x0e\n\x06\x63hunks\x18\x03 \x01(\r\x12\x0c\n\x04hash\x18\x04 \x01(\x0c\x12?\n\x08metadata\x18\x05 \x01(\x0b\x32\'.cosmos.base.snapshots.v1beta1.MetadataB\x04\xc8\xde\x1f\x00" \n\x08Metadata\x12\x14\n\x0c\x63hunk_hashes\x18\x01 \x03(\x0c\x42.Z,github.com/cosmos/cosmos-sdk/snapshots/typesb\x06proto3',
    dependencies=[
        gogoproto_dot_gogo__pb2.DESCRIPTOR,
    ],
)


_SNAPSHOT = _descriptor.Descriptor(
    name="Snapshot",
    full_name="cosmos.base.snapshots.v1beta1.Snapshot",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="height",
            full_name="cosmos.base.snapshots.v1beta1.Snapshot.height",
            index=0,
            number=1,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="format",
            full_name="cosmos.base.snapshots.v1beta1.Snapshot.format",
            index=1,
            number=2,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="chunks",
            full_name="cosmos.base.snapshots.v1beta1.Snapshot.chunks",
            index=2,
            number=3,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="hash",
            full_name="cosmos.base.snapshots.v1beta1.Snapshot.hash",
            index=3,
            number=4,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="metadata",
            full_name="cosmos.base.snapshots.v1beta1.Snapshot.metadata",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\310\336\037\000",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=102,
    serialized_end=239,
)


_METADATA = _descriptor.Descriptor(
    name="Metadata",
    full_name="cosmos.base.snapshots.v1beta1.Metadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="chunk_hashes",
            full_name="cosmos.base.snapshots.v1beta1.Metadata.chunk_hashes",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=241,
    serialized_end=273,
)

_SNAPSHOT.fields_by_name["metadata"].message_type = _METADATA
DESCRIPTOR.message_types_by_name["Snapshot"] = _SNAPSHOT
DESCRIPTOR.message_types_by_name["Metadata"] = _METADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Snapshot = _reflection.GeneratedProtocolMessageType(
    "Snapshot",
    (_message.Message,),
    {
        "DESCRIPTOR": _SNAPSHOT,
        "__module__": "cosmos.base.snapshots.v1beta1.snapshot_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.base.snapshots.v1beta1.Snapshot)
    },
)
_sym_db.RegisterMessage(Snapshot)

Metadata = _reflection.GeneratedProtocolMessageType(
    "Metadata",
    (_message.Message,),
    {
        "DESCRIPTOR": _METADATA,
        "__module__": "cosmos.base.snapshots.v1beta1.snapshot_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.base.snapshots.v1beta1.Metadata)
    },
)
_sym_db.RegisterMessage(Metadata)


DESCRIPTOR._options = None
_SNAPSHOT.fields_by_name["metadata"]._options = None
# @@protoc_insertion_point(module_scope)
