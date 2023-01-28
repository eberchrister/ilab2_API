# Author : Eber Christer 
''' The Python implementation of the gRPC light system client.'''

from flask import Flask, session, render_template, jsonify, redirect, url_for

import grpc
import light_pb2, light_pb2_grpc
import time

app = Flask(__name__)
app.secret_key = 'super secret'

channel = grpc.insecure_channel('localhost:50051')
stub = light_pb2_grpc.LightServiceStub(channel)

@app.route('/')
def index():
    first,second,third = light_get_lights()
    if not first['on']:
        first['rgb'] = '#000000'
    if not second['on']:
        second['rgb'] = '#000000'
    if not third['on']:
        third['rgb'] = '#000000'
    return render_template('index.html', first=first, second=second, third=third)

# unary call client --> server
@app.route('/getLight/<id>')
def light_get_light(id):
    target_id = light_pb2.Indicator(id=int(id))
    response = stub.GetLight(target_id)
    return {'id': response.light.id, 'rgb': process_response(response, id), 'on': response.light.on}
    

@app.route('/setLight/<command>')
def light_set_light(command):
    id,red,green,blue,on = command.split('-')
    target_light = light_pb2.LightRequest(light = light_pb2.Light(id=int(id), red=int(red), green=int(green), blue=int(blue), on=bool(int(on)%2)))
    stub.SetLight(target_light)
    return 'Light set\n'

# ----------------------------------------------------------------------------------------- #

# streaming call server --> client
@app.route('/getLights')
def light_get_lights():
    hex = []
    for response in stub.GetLights(light_pb2.Empty()):
        process_response(response, response.light.id)
        hex.append({'id': response.light.id, 'rgb': response.message, 'on': response.light.on})
    return hex

# ----------------------------------------------------------------------------------------- #

# streaming call client --> server
@app.route('/setLights/<commands>')
def light_set_lights(commands):
    stub.SetLights(set_lights_requests(commands))
    return 'Lights set\n'

# ----------------------------------------------------------------------------------------- #

# bi-directional streaming call client --> server --> client
@app.route('/checkLights/<id_list>')
def light_check_lights(id_list):
    responses = stub.CheckLights(interactive_requests(id_list))
    for response in responses:
        print('Light[{}] - Current Color: {}'.format(response.id, response.message))
    return redirect(url_for('index'))

# ----------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------- #

# Helper function to process the response from the server
def interactive_requests(id_list):
    check_id_iterable = []
    check_ids = id_list.split(',')
    for id in check_ids:
        check_id_iterable.append(light_pb2.Indicator(id=int(id)))
    
    for id in check_id_iterable:
        yield id
        time.sleep(0.2)

def set_lights_requests(commands):
    command_split = commands.split('-')
    light_iterable = []
    for light in command_split:
        light_split = light.split(',')
        current_light = light_pb2.LightRequest(light=light_pb2.Light(id=int(light_split[0]), red=int(light_split[1]), green=int(light_split[2]), blue=int(light_split[3]), on=bool(int(light_split[4])%2)))
        light_iterable.append(current_light)

    for l in light_iterable:
        print(l)
        yield l
        time.sleep(1)
    

def process_response(response, id):
    if response.message == 'Light not found':
        print('Light[{}] not found'.format(id))
    else:
        # print('Light[{}] - Message: {}'.format(response.light.id, response.message))
        # print('\tRGB ({},{},{})'.format(response.light.red, response.light.green, response.light.blue))
        # print('\tOn: {}'.format(response.light.on))
        return response.message


if __name__ == '__main__':
    app.run(debug=False, port=5001)