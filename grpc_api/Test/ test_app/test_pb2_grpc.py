# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import test_pb2 as test__pb2


class NumberServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.square = channel.unary_unary(
                '/NumberService/square',
                request_serializer=test__pb2.Number.SerializeToString,
                response_deserializer=test__pb2.Number.FromString,
                )
        self.sum = channel.unary_unary(
                '/NumberService/sum',
                request_serializer=test__pb2.NumberList.SerializeToString,
                response_deserializer=test__pb2.Number.FromString,
                )
        self.sixtyNine = channel.unary_unary(
                '/NumberService/sixtyNine',
                request_serializer=test__pb2.Empty.SerializeToString,
                response_deserializer=test__pb2.Number.FromString,
                )


class NumberServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def square(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sum(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sixtyNine(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NumberServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'square': grpc.unary_unary_rpc_method_handler(
                    servicer.square,
                    request_deserializer=test__pb2.Number.FromString,
                    response_serializer=test__pb2.Number.SerializeToString,
            ),
            'sum': grpc.unary_unary_rpc_method_handler(
                    servicer.sum,
                    request_deserializer=test__pb2.NumberList.FromString,
                    response_serializer=test__pb2.Number.SerializeToString,
            ),
            'sixtyNine': grpc.unary_unary_rpc_method_handler(
                    servicer.sixtyNine,
                    request_deserializer=test__pb2.Empty.FromString,
                    response_serializer=test__pb2.Number.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'NumberService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NumberService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def square(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NumberService/square',
            test__pb2.Number.SerializeToString,
            test__pb2.Number.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def sum(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NumberService/sum',
            test__pb2.NumberList.SerializeToString,
            test__pb2.Number.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def sixtyNine(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NumberService/sixtyNine',
            test__pb2.Empty.SerializeToString,
            test__pb2.Number.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)