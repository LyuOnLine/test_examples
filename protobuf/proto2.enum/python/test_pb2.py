# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='test.proto',
  package='test',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\ntest.proto\x12\x04test\"@\n\x0bTestMessage\x12 \n\x08testEnum\x18\x01 \x02(\x0e\x32\x0e.test.TestEnum\x12\x0f\n\x07testInt\x18\x02 \x02(\x05*,\n\x08TestEnum\x12\n\n\x06UNKOWN\x10\x00\x12\t\n\x05\x45NUM1\x10\x01\x12\t\n\x05\x45NUM2\x10\x02')
)

_TESTENUM = _descriptor.EnumDescriptor(
  name='TestEnum',
  full_name='test.TestEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENUM1', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENUM2', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=86,
  serialized_end=130,
)
_sym_db.RegisterEnumDescriptor(_TESTENUM)

TestEnum = enum_type_wrapper.EnumTypeWrapper(_TESTENUM)
UNKOWN = 0
ENUM1 = 1
ENUM2 = 2



_TESTMESSAGE = _descriptor.Descriptor(
  name='TestMessage',
  full_name='test.TestMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='testEnum', full_name='test.TestMessage.testEnum', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='testInt', full_name='test.TestMessage.testInt', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=84,
)

_TESTMESSAGE.fields_by_name['testEnum'].enum_type = _TESTENUM
DESCRIPTOR.message_types_by_name['TestMessage'] = _TESTMESSAGE
DESCRIPTOR.enum_types_by_name['TestEnum'] = _TESTENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TestMessage = _reflection.GeneratedProtocolMessageType('TestMessage', (_message.Message,), dict(
  DESCRIPTOR = _TESTMESSAGE,
  __module__ = 'test_pb2'
  # @@protoc_insertion_point(class_scope:test.TestMessage)
  ))
_sym_db.RegisterMessage(TestMessage)


# @@protoc_insertion_point(module_scope)