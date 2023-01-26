# Author : Eber Christer 
''' The Python implementation of the gRPC light system client.'''

from concurrent import futures
import time

import grpc
import light_pb2, light_pb2_grpc
import sqlite3

def color_hex(r, g, b):
    r_hex = hex(r)[2:]
    g_hex = hex(g)[2:]
    b_hex = hex(b)[2:]

    if len(r_hex) == 1:
        r_hex = '0' + r_hex
    if len(g_hex) == 1:
        g_hex = '0' + g_hex
    if len(b_hex) == 1:
        b_hex = '0' + b_hex

    return '#' + r_hex + g_hex + b_hex

class LightServiceServicer(light_pb2_grpc.LightServiceServicer):

    def __init__(self) -> None:
        self.db = sqlite3.connect('light.db', check_same_thread=False).cursor()

    def GetLight(self, request, context):
        print('GetLight called with id: {}'.format(request.id))
        self.db.execute("SELECT * FROM light WHERE id = ?", (request.id,))
        light_response = self.db.fetchone()
        if light_response:
            return light_pb2.LightResponse(
                message = color_hex(light_response[1], light_response[2], light_response[3]),
                light = light_pb2.Light(
                    id = light_response[0],
                    red = light_response[1],
                    green = light_response[2],
                    blue = light_response[3],
                    on = bool(light_response[4])
                )
            )
        else:
            return light_pb2.LightResponse(message = 'Light not found', light = None)
    
    def SetLight(self, request, context):
        print('SetLight called with id: {}, rgb: {}, on: {}'.format(request.light.id, color_hex(request.light.red, request.light.green, request.light.blue), request.light.on))
        target_id = request.light.id
        target_red = request.light.red
        target_green = request.light.green
        target_blue = request.light.blue
        target_on = request.light.on

        self.db.execute("UPDATE light SET red = ?, green = ?, blue = ?, state = ? WHERE id = ?", (target_red, target_green, target_blue, int(target_on), target_id))
        self.db.connection.commit()

        # if light_pb2_grpc.LightServiceStub(grpc.insecure_channel('localhost:50051')).GetLight(light_pb2.Indicator(id=target_id)).message == 'Light not found':
        #     return light_pb2.LightResponse(message = 'Light not found', light = None)
        # return light_pb2.LightResponse(
        #     message = 'Light updated',
        #     light = light_pb2.Light(
        #         id = target_id,
        #         red = target_red,
        #         green = target_green,
        #         blue = target_blue,
        #         on = target_on
        #     )
        # )

        return light_pb2.Empty()

    def GetLights(self, request, context):
        # print('GetLights called')
        self.db.execute("SELECT * FROM light")
        light_response = self.db.fetchall()
        for light in light_response:
            yield light_pb2.LightResponse(
                message = color_hex(light[1], light[2], light[3]),
                light = light_pb2.Light(
                    id = light[0],
                    red = light[1],
                    green = light[2],
                    blue = light[3],
                    on = bool(light[4])
                )
            )
            time.sleep(0.1)

    def SetLights(self, request_iterator, context):
        print('SetLights called')
        for request in request_iterator:
            light = request.light
            target_id = light.id
            target_red = light.red
            target_green = light.green
            target_blue = light.blue
            target_on = light.on
            print('\tlight[{}] -> rgb ({}, {}, {}), on: {}'.format(target_id, target_red, target_green, target_blue, target_on))

            self.db.execute("UPDATE light SET red = ?, green = ?, blue = ?, state = ? WHERE id = ?", (target_red, target_green, target_blue, int(target_on), target_id))
            self.db.connection.commit()

        return light_pb2.Empty()

    def CheckLights(self, request_iterator, context):
        print('InteractiveLights called')
        for request in request_iterator:
            requested_id = request.id
            self.db.execute("SELECT * FROM light WHERE id = ?", (request.id,))
            light_response = self.db.fetchone()
            yield light_pb2.ChatMessage(
                id = requested_id,
                message = color_hex(light_response[1], light_response[2], light_response[3]),
            )
            time.sleep(0.2)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    light_pb2_grpc.add_LightServiceServicer_to_server(LightServiceServicer(), server)
    print('Starting server. Listening on port 50051.')
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()