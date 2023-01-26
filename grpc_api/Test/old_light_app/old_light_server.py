import grpc
import light_pb2
import light_pb2_grpc
import sqlite3
import time
from concurrent import futures

conn = sqlite3.connect('light.db', check_same_thread=False)  
cursor = conn.cursor()

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
    # Unary
    def GetLight(self, request, context):
        requested_id = request.id
        print('GetLight called with id: {}'.format(requested_id))
        cursor.execute("SELECT * FROM light WHERE id = ?", (requested_id,))
        light = cursor.fetchone()

        # print(light)
        if light:
            return light_pb2.Light(id=light[0], rgb=(color_hex(light[1], light[2], light[3])), on=bool(light[4]))
        else:
            return 'Light not found', 404

    def SetLight(self, request, context):
        request_id = int(request.id)
        request_rgb = str(request.rgb)
        request_on = int(request.on)

        red = int(request_rgb[0:2], 16)
        green = int(request_rgb[2:4], 16)
        blue = int(request_rgb[4:6], 16)

        print('SetLight called with id: {}, rgb: {}, on: {}'.format(request_id, request_rgb, request_on))
        # print('Red: {}, Green: {}, Blue: {}'.format(red, green, blue))


        cursor.execute("UPDATE light SET red = ?, green = ?, blue = ?, state = ? WHERE id = ?", (red, green, blue, request_on, request_id))
        conn.commit()

        # print('Light updated')
        return light_pb2.Light(id=int(request_id), rgb=('#'+request_rgb), on=bool(request_on))


    # Server streaming
    def GetLights(self, request, context):
        print('GetLights called')
        cursor.execute("SELECT * FROM light")
        lights = cursor.fetchall()
        for light in lights:
            yield light_pb2.Light(id=light[0], rgb=(color_hex(light[1], light[2], light[3])), on=bool(light[4]))
            time.sleep(secs=3)


    # Client streaming
    def SetLights(self, request_iterator, context):
        print('SetLights called')
        for request in request_iterator:
            request_id = int(request.id)
            request_rgb = str(request.rgb)
            request_on = int(request.on)

            red = int(request_rgb[0:2], 16)
            green = int(request_rgb[2:4], 16)
            blue = int(request_rgb[4:6], 16)

            print('SetLight called with id: {}, rgb: {}, on: {}'.format(request_id, request_rgb, request_on))
            cursor.execute("UPDATE light SET red = ?, green = ?, blue = ?, state = ? WHERE id = ?", (red, green, blue, request_on, request_id))
            conn.commit()

    # Bidirectional streaming
    def SetGetLights(self, request_iterator, context):
        pass

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    light_pb2_grpc.add_LightServiceServicer_to_server(LightServiceServicer(), server)
    print('Starting server. Listening on port 50051.')
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()