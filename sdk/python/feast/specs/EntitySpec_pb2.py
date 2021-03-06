# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/specs/EntitySpec.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='feast/specs/EntitySpec.proto',
  package='feast.specs',
  syntax='proto3',
  serialized_options=_b('\n\013feast.specsB\017EntitySpecProtoZ6github.com/gojek/feast/protos/generated/go/feast/specs'),
  serialized_pb=_b('\n\x1c\x66\x65\x61st/specs/EntitySpec.proto\x12\x0b\x66\x65\x61st.specs\"=\n\nEntitySpec\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0c\n\x04tags\x18\x03 \x03(\tBV\n\x0b\x66\x65\x61st.specsB\x0f\x45ntitySpecProtoZ6github.com/gojek/feast/protos/generated/go/feast/specsb\x06proto3')
)




_ENTITYSPEC = _descriptor.Descriptor(
  name='EntitySpec',
  full_name='feast.specs.EntitySpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='feast.specs.EntitySpec.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='feast.specs.EntitySpec.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='feast.specs.EntitySpec.tags', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=106,
)

DESCRIPTOR.message_types_by_name['EntitySpec'] = _ENTITYSPEC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EntitySpec = _reflection.GeneratedProtocolMessageType('EntitySpec', (_message.Message,), dict(
  DESCRIPTOR = _ENTITYSPEC,
  __module__ = 'feast.specs.EntitySpec_pb2'
  # @@protoc_insertion_point(class_scope:feast.specs.EntitySpec)
  ))
_sym_db.RegisterMessage(EntitySpec)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
