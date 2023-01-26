import grpc
import test_pb2
import test_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = test_pb2_grpc.NumberServiceStub(channel)
        response = stub.square(test_pb2.Number(value=int(input('Enter a number: '))))
        print("Square: " + str(response.value))

if __name__ == '__main__':
    run()