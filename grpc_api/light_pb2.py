# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: light.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0blight.proto\x12\x05light\"I\n\x05Light\x12\n\n\x02id\x18\x01 \x01(\r\x12\n\n\x02on\x18\x02 \x01(\x08\x12\x0b\n\x03red\x18\x03 \x01(\r\x12\r\n\x05green\x18\x04 \x01(\r\x12\x0c\n\x04\x62lue\x18\x05 \x01(\r\"+\n\x0cLightRequest\x12\x1b\n\x05light\x18\x01 \x01(\x0b\x32\x0c.light.Light\"=\n\rLightResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x1b\n\x05light\x18\x02 \x01(\x0b\x32\x0c.light.Light\"\x17\n\tIndicator\x12\n\n\x02id\x18\x01 \x01(\r\"\x07\n\x05\x45mpty\"*\n\x0b\x43hatMessage\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0f\n\x07message\x18\x02 \x01(\t2\x99\x02\n\x0cLightService\x12\x34\n\x08GetLight\x12\x10.light.Indicator\x1a\x14.light.LightResponse\"\x00\x12/\n\x08SetLight\x12\x13.light.LightRequest\x1a\x0c.light.Empty\"\x00\x12\x33\n\tGetLights\x12\x0c.light.Empty\x1a\x14.light.LightResponse\"\x00\x30\x01\x12\x32\n\tSetLights\x12\x13.light.LightRequest\x1a\x0c.light.Empty\"\x00(\x01\x12\x39\n\x0b\x43heckLights\x12\x10.light.Indicator\x1a\x12.light.ChatMessage\"\x00(\x01\x30\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'light_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LIGHT._serialized_start=22
  _LIGHT._serialized_end=95
  _LIGHTREQUEST._serialized_start=97
  _LIGHTREQUEST._serialized_end=140
  _LIGHTRESPONSE._serialized_start=142
  _LIGHTRESPONSE._serialized_end=203
  _INDICATOR._serialized_start=205
  _INDICATOR._serialized_end=228
  _EMPTY._serialized_start=230
  _EMPTY._serialized_end=237
  _CHATMESSAGE._serialized_start=239
  _CHATMESSAGE._serialized_end=281
  _LIGHTSERVICE._serialized_start=284
  _LIGHTSERVICE._serialized_end=565
# @@protoc_insertion_point(module_scope)
