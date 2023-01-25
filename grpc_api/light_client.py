import requests
from flask import Flask, session, render_template, g, session, jsonify, redirect, url_for, request
import grpc
import light_pb2
import light_pb2_grpc
import time


app = Flask(__name__)
app.secret_key = 'super secret'


channel = grpc.insecure_channel('localhost:50051')
stub = light_pb2_grpc.LightServiceStub(channel)
session = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    first, second, third = getStream()
    return render_template('index.html', first=first, second=second, third=third)

@app.route('/get/<id>', methods=['GET'])
def get(id):
    id_x = stub.GetLight(light_pb2.Id(id=int(id)))
    id_json = {'id': id_x.id, 'rgb': id_x.rgb, 'on': id_x.on}
    return jsonify(id_json)

@app.route('/set/<id>/<rgb>/<on>', methods=['GET'])
def set(id, rgb, on):
    print(id, rgb, on)
    stub.SetLight(light_pb2.Light(id=int(id), rgb=rgb, on=bool(on)))
    print(session)
    return "Light updated"

@app.route('/getStream')
def getStream():
    lights = stub.GetLights(light_pb2.Empty())
    lights_json = []
    for light in lights:
        # print(light, light.id, light.rgb, light.on)
        lights_json.append({'id': light.id, 'rgb': light.rgb, 'on': light.on})
    return lights_json

@app.route('/setStream')
def setStream():
    stub.SetLights(get_setStream_requests())
    print('setStream called')

def get_setStream_requests():
        command = input('Enter a command: id,rgb_hex,on-id,rgb_hex,on-id,rgb_hex,on, ... : ')
        command_split = command.split('-')
        # print(command_split)
        for light in command_split:
            # print(light)
            light_split = light.split(',')
            current_light = light_pb2.Light(id=int(light_split[0]), rgb=light_split[1], on=bool(light_split[2]))
            print('Light sent: id: {}, rgb: {}, on: {}'.format(current_light.id, current_light.rgb, current_light.on))
            yield current_light
            time.sleep(1)

@app.route('/setGetStream')
def setGetStream(): 
    pass

if __name__ == '__main__':
    app.run(debug=False, port=5001)

    # 1,FF0000,1-2,FF0000,1-3,FF0000,1-1,00FF00,1-2,00FF00,1-3,00FF00,1-1,0000FF,1-2,0000FF,1-3,0000FF,1-1,000000,1-2,000000,1-3,000000,1