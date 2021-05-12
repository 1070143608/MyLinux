# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: helloworld.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='helloworld.proto',
  package='helloworld',
  syntax='proto3',
  serialized_options=b'\n\033io.grpc.examples.helloworldB\017HelloWorldProtoP\001\242\002\003HLW',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10helloworld.proto\x12\nhelloworld\"u\n\x0cHelloRequest\x12/\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\x1f.helloworld.HelloRequest.Action\x12\x11\n\x04name\x18\x02 \x01(\tH\x00\x88\x01\x01\"\x18\n\x06\x41\x63tion\x12\x0e\n\nHelloWorld\x10\x00\x42\x07\n\x05_name\"\xd8\x01\n\nHelloReply\x12\x35\n\x06status\x18\x01 \x01(\x0e\x32 .helloworld.HelloReply.ErrorCodeH\x00\x88\x01\x01\x12\x13\n\x06result\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x15\n\x08\x65rr_code\x18\x03 \x01(\rH\x02\x88\x01\x01\x12\x14\n\x07\x65rr_msg\x18\x04 \x01(\tH\x03\x88\x01\x01\"\"\n\tErrorCode\x12\x0b\n\x07SUCCESS\x10\x00\x12\x08\n\x04\x46\x61il\x10\x01\x42\t\n\x07_statusB\t\n\x07_resultB\x0b\n\t_err_codeB\n\n\x08_err_msg2L\n\x07Greeter\x12\x41\n\x0bServiceCall\x12\x18.helloworld.HelloRequest\x1a\x16.helloworld.HelloReply\"\x00\x42\x36\n\x1bio.grpc.examples.helloworldB\x0fHelloWorldProtoP\x01\xa2\x02\x03HLWb\x06proto3'
)



_HELLOREQUEST_ACTION = _descriptor.EnumDescriptor(
  name='Action',
  full_name='helloworld.HelloRequest.Action',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HelloWorld', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=116,
  serialized_end=140,
)
_sym_db.RegisterEnumDescriptor(_HELLOREQUEST_ACTION)

_HELLOREPLY_ERRORCODE = _descriptor.EnumDescriptor(
  name='ErrorCode',
  full_name='helloworld.HelloReply.ErrorCode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Fail', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=287,
  serialized_end=321,
)
_sym_db.RegisterEnumDescriptor(_HELLOREPLY_ERRORCODE)


_HELLOREQUEST = _descriptor.Descriptor(
  name='HelloRequest',
  full_name='helloworld.HelloRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='helloworld.HelloRequest.action', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='helloworld.HelloRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _HELLOREQUEST_ACTION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_name', full_name='helloworld.HelloRequest._name',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=32,
  serialized_end=149,
)


_HELLOREPLY = _descriptor.Descriptor(
  name='HelloReply',
  full_name='helloworld.HelloReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='helloworld.HelloReply.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result', full_name='helloworld.HelloReply.result', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='err_code', full_name='helloworld.HelloReply.err_code', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='err_msg', full_name='helloworld.HelloReply.err_msg', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _HELLOREPLY_ERRORCODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_status', full_name='helloworld.HelloReply._status',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_result', full_name='helloworld.HelloReply._result',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_err_code', full_name='helloworld.HelloReply._err_code',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_err_msg', full_name='helloworld.HelloReply._err_msg',
      index=3, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=152,
  serialized_end=368,
)

_HELLOREQUEST.fields_by_name['action'].enum_type = _HELLOREQUEST_ACTION
_HELLOREQUEST_ACTION.containing_type = _HELLOREQUEST
_HELLOREQUEST.oneofs_by_name['_name'].fields.append(
  _HELLOREQUEST.fields_by_name['name'])
_HELLOREQUEST.fields_by_name['name'].containing_oneof = _HELLOREQUEST.oneofs_by_name['_name']
_HELLOREPLY.fields_by_name['status'].enum_type = _HELLOREPLY_ERRORCODE
_HELLOREPLY_ERRORCODE.containing_type = _HELLOREPLY
_HELLOREPLY.oneofs_by_name['_status'].fields.append(
  _HELLOREPLY.fields_by_name['status'])
_HELLOREPLY.fields_by_name['status'].containing_oneof = _HELLOREPLY.oneofs_by_name['_status']
_HELLOREPLY.oneofs_by_name['_result'].fields.append(
  _HELLOREPLY.fields_by_name['result'])
_HELLOREPLY.fields_by_name['result'].containing_oneof = _HELLOREPLY.oneofs_by_name['_result']
_HELLOREPLY.oneofs_by_name['_err_code'].fields.append(
  _HELLOREPLY.fields_by_name['err_code'])
_HELLOREPLY.fields_by_name['err_code'].containing_oneof = _HELLOREPLY.oneofs_by_name['_err_code']
_HELLOREPLY.oneofs_by_name['_err_msg'].fields.append(
  _HELLOREPLY.fields_by_name['err_msg'])
_HELLOREPLY.fields_by_name['err_msg'].containing_oneof = _HELLOREPLY.oneofs_by_name['_err_msg']
DESCRIPTOR.message_types_by_name['HelloRequest'] = _HELLOREQUEST
DESCRIPTOR.message_types_by_name['HelloReply'] = _HELLOREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREQUEST,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.HelloRequest)
  })
_sym_db.RegisterMessage(HelloRequest)

HelloReply = _reflection.GeneratedProtocolMessageType('HelloReply', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREPLY,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.HelloReply)
  })
_sym_db.RegisterMessage(HelloReply)


DESCRIPTOR._options = None

_GREETER = _descriptor.ServiceDescriptor(
  name='Greeter',
  full_name='helloworld.Greeter',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=370,
  serialized_end=446,
  methods=[
  _descriptor.MethodDescriptor(
    name='ServiceCall',
    full_name='helloworld.Greeter.ServiceCall',
    index=0,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLOREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GREETER)

DESCRIPTOR.services_by_name['Greeter'] = _GREETER

# @@protoc_insertion_point(module_scope)