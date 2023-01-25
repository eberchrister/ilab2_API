# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import light_pb2 as light__pb2


class LightServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetLight = channel.unary_unary(
                '/light.LightService/GetLight',
                request_serializer=light__pb2.Id.SerializeToString,
                response_deserializer=light__pb2.Light.FromString,
                )
        self.SetLight = channel.unary_unary(
                '/light.LightService/SetLight',
                request_serializer=light__pb2.Light.SerializeToString,
                response_deserializer=light__pb2.Light.FromString,
                )
        self.GetLights = channel.unary_stream(
                '/light.LightService/GetLights',
                request_serializer=light__pb2.Empty.SerializeToString,
                response_deserializer=light__pb2.Light.FromString,
                )
        self.SetLights = channel.stream_unary(
                '/light.LightService/SetLights',
                request_serializer=light__pb2.Light.SerializeToString,
                response_deserializer=light__pb2.Empty.FromString,
                )
        self.SetGetLights = channel.stream_stream(
                '/light.LightService/SetGetLights',
                request_serializer=light__pb2.Light.SerializeToString,
                response_deserializer=light__pb2.Light.FromString,
                )


class LightServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetLight(self, request, context):
        """unary
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetLight(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLights(self, request, context):
        """server streaming
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetLights(self, request_iterator, context):
        """client streaming
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetGetLights(self, request_iterator, context):
        """bidirectional streaming
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LightServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetLight': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLight,
                    request_deserializer=light__pb2.Id.FromString,
                    response_serializer=light__pb2.Light.SerializeToString,
            ),
            'SetLight': grpc.unary_unary_rpc_method_handler(
                    servicer.SetLight,
                    request_deserializer=light__pb2.Light.FromString,
                    response_serializer=light__pb2.Light.SerializeToString,
            ),
            'GetLights': grpc.unary_stream_rpc_method_handler(
                    servicer.GetLights,
                    request_deserializer=light__pb2.Empty.FromString,
                    response_serializer=light__pb2.Light.SerializeToString,
            ),
            'SetLights': grpc.stream_unary_rpc_method_handler(
                    servicer.SetLights,
                    request_deserializer=light__pb2.Light.FromString,
                    response_serializer=light__pb2.Empty.SerializeToString,
            ),
            'SetGetLights': grpc.stream_stream_rpc_method_handler(
                    servicer.SetGetLights,
                    request_deserializer=light__pb2.Light.FromString,
                    response_serializer=light__pb2.Light.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'light.LightService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LightService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetLight(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/light.LightService/GetLight',
            light__pb2.Id.SerializeToString,
            light__pb2.Light.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetLight(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/light.LightService/SetLight',
            light__pb2.Light.SerializeToString,
            light__pb2.Light.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLights(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/light.LightService/GetLights',
            light__pb2.Empty.SerializeToString,
            light__pb2.Light.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetLights(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/light.LightService/SetLights',
            light__pb2.Light.SerializeToString,
            light__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetGetLights(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/light.LightService/SetGetLights',
            light__pb2.Light.SerializeToString,
            light__pb2.Light.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)