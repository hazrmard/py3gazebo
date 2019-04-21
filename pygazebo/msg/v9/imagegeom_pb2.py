# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: imagegeom.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='imagegeom.proto',
  package='gazebo.msgs',
  syntax='proto2',
  serialized_pb=_b('\n\x0fimagegeom.proto\x12\x0bgazebo.msgs\"d\n\tImageGeom\x12\x0b\n\x03uri\x18\x01 \x02(\t\x12\r\n\x05scale\x18\x02 \x01(\x01\x12\x16\n\tthreshold\x18\x03 \x01(\x05:\x03\x32\x35\x35\x12\x0e\n\x06height\x18\x04 \x01(\x01\x12\x13\n\x0bgranularity\x18\x05 \x01(\x05')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_IMAGEGEOM = _descriptor.Descriptor(
  name='ImageGeom',
  full_name='gazebo.msgs.ImageGeom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uri', full_name='gazebo.msgs.ImageGeom.uri', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scale', full_name='gazebo.msgs.ImageGeom.scale', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='threshold', full_name='gazebo.msgs.ImageGeom.threshold', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=255,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height', full_name='gazebo.msgs.ImageGeom.height', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='granularity', full_name='gazebo.msgs.ImageGeom.granularity', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=132,
)

DESCRIPTOR.message_types_by_name['ImageGeom'] = _IMAGEGEOM

ImageGeom = _reflection.GeneratedProtocolMessageType('ImageGeom', (_message.Message,), dict(
  DESCRIPTOR = _IMAGEGEOM,
  __module__ = 'imagegeom_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.ImageGeom)
  ))
_sym_db.RegisterMessage(ImageGeom)


# @@protoc_insertion_point(module_scope)