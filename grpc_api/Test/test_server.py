import grpc 
import test_pb2_grpc
import test_pb2
from concurrent import futures

class NumerServiceServicer(test_pb2_grpc.NumberServiceServicer):
    def square(self, request, context):
        squared = request.value * request.value
        result = test_pb2.Number(value=squared)
        return result


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    test_pb2_grpc.add_NumberServiceServicer_to_server(NumerServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()