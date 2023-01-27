# iLab2 - API Development

Development of different API architectures in python - REST API, gRPC, GraphQL
## Extra Libraries
- [Flask] - lightweight web application framework
- [gRPCio] - allows development of gRPC in python

## REST API
In this project, a **REST API** is to be developed for a reminder web-app. This reminder web-app is designed in such a way that its content can only be modified through API calls to the backend.

The `reminder_backend.py` creates an SQLite database called `reminder.db` with a default entry if it doesn't exist yet. 

---
The following are the implemented REST API endpoints: <br />
`[GET] localhost:8080/api/v1/histories` <br />
--> get all log entries from the database <br />
`[GET] localhost:8080/api/v1/reminders` <br />
--> get all tasks from the reminder <br />
`[GET] localhost:8080/api/v1/reminders/<id>` <br />
--> get specific task from the reminder <br />
`[PUT] localhost:8080/api/v1/reminders/<id>` <br />
--> updates a specific task from the reminder <br />
`[POST] localhost:8080/api/v1/reminders` <br />
--> posts a new task to the reminder <br />
`[DELETE] localhost:8080/api/v1/reminders/<id>` <br />
--> deletes a specific task from the reminder <br />

---
To run the front-end:
```sh
flask --app reminder_frontend run --port 5000
```
To run the back-end:
```sh
flask --app reminder_backend run --port 8080
```
To see the visualization:
```sh
http://localhost:5000
```

## gRPC
In this project, a **gRPC API** is to be developed to facilitate the communication between a python gRPC client with a python gRPC server to control the RGB-lights in a fictional light system.

### gRPC protobuf
To establish this connection, a `light.proto` file has to be created first. This proto file serves as an interface that can be used by different programming languages to communicate with each other. We define the file as follows:
```protobuf
syntax = "proto3";

package light; 

// Service for controlling lights
service LightService {
    // unary
    rpc GetLight (Indicator) returns (LightResponse) {}
    rpc SetLight (LightRequest) returns (Empty) {}

    // server --> client streaming
    rpc GetLights (Empty) returns (stream LightResponse) {}
    
    // client --> server streaming
    rpc SetLights (stream LightRequest) returns (Empty) {}

    // client <--> server streaming
    rpc CheckLights (stream Indicator) returns (stream ChatMessage) {}
}

// Message for a light object
message Light {
    uint32 id = 1;
    bool on = 2;
    uint32 red = 3;
    uint32 green = 4;
    uint32 blue = 5;
}

// Message for a light request
message LightRequest {
    Light light = 1;
}

// Message for a light response
message LightResponse {
    string message = 1;
    Light light = 2;
}

// Message for an indicator
message Indicator {
    uint32 id = 1;
}

// Empty message
message Empty {}

// Chat message 
message ChatMessage {
    uint32 id = 1;
    string message = 2;
}
```
We can think of the `message` keyword as a C-struct that defines a new class, containing fields of pre-defined or user-defined datatypes. Similarly, the `service` and `rpc` keyword can be thought of as a Java abstract class that has to be implemented later by the gRPC server. Another keyword that is important is the `stream` keyword. This shows that a datatype is sequentially being fed into or out of the function. Depending of the direction of the stream, a special python return `yield` has to be used.

running the following command in the terminal
``` sh
python3 -m grpc_tools.protoc -I./protos protos/light.proto --python_out=. --grpc_python_out=.
```
automatically generates two new files - `light_pb2_grpc.py` and `light_pb2.py`. These files contain the actual mapping between the client's programming language with the server's programming language and handles the marshalling between them. However, in our case it's all in python. with  `light_pb2`, we're able to create and initialize the structs (messages) specified by the proto file and with `light_pb2_grpc`, we're able to create and initialize the interface/template (service) on the server.

---
### gRPC client-server
gRPC client can be executed with the following command: 
```sh
flask --app light_client run --port 5001
```
gRPC server can be executed with the following command: 
```sh
python3 light_server.py
```
To see the visualization:
```sh
http://localhost:5001
```

---
An important concept of gRPC client is the creation of stubs in order to call the remote functions. In our case, it's something like this: 

```python
channel = grpc.insecure_channel(server_url)
stub = light_pb2_grpc.LightServiceStub(channel)
target_id = light_pb2.Indicator(id=id)
light = stub.GetLight(target_id)
```

The above function retrieves the light object with the specified ID through unary gRPC call. 

Other implementations of gRPC includes : server to client streaming, client to server streaming, as well as bidirectional streaming.

Here is an example of a **server-to-client streaming** with  `GetLights()`: 
``` python
#server-side
class LightServiceServicer(light_pb2_grpc.LightServiceServicer):
    # some code here
    def GetLights(self, request, context):
            self.db.execute("SELECT * FROM light")
            query_results = self.db.fetchall()
            for result in query_results:
                yield light_pb2.LightResponse(id=<id>, light=<light>)
                time.sleep(0.1)
    # some more code here
```
Disregarding the <id> and the <light> field that has to be initialized, this function returns a stream of `LightResponse` objects back to the client per 0.1 seconds.

Similary, the **client-to-server streaming** works the same way. 
``` python
# client-side
def set_lights_requests():
    lights_iterable = [<light>]
    for light in light_iterable:
        yield light
        time.sleep(1)

stub.SetLights(set_lights_requests)
```
This sends a sequence of **LightRequests** to the server. It sends each LightRequest object once per 1 second, and will set the state of the specified light objects in the database.

For Bi-directional streaming, both the client and the server will implement these object streaming. This is useful in applications where a chat-like communication is happening between the client and the server.

---
In order to run the functions in the client-side without implementing an event-listener on the frontend, we have designed the functions to be accessible through 
`curl` calls.

``` sh
curl localhost:5001/getLight/1
curl localhost:5001/getLight/2
curl localhost:5001/getLight/3

curl localhost:5001/setLight/1-255-0-0-1
curl localhost:5001/setLight/2-0-255-0-1
curl localhost:5001/setLight/2-0-0-255-1

curl localhost:5001/getLights

curl localhost:5001/setLights/1,255,0,0,1-1,255,0,0,0-2,255,0,0,1-2,255,0,0,0-3,255,0,0,1-3,255,0,0,0-1,255,90,90,1-2,90,255,90,1-3,90,90,255,1

curl localhost:5001/checkLights/1,2,1,2,2,3,3,3,3,3,1
```


[//]: # 
   [flask]: <https://flask.palletsprojects.com/en/2.2.x/>
   [grpcio]: <https://grpc.io/docs/languages/python/quickstart/>
   
