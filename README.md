# iLab2 - API Development

Development of different API architectures in python - REST API, gRPC, GraphQL
## Extra Libraries
- [Flask] - lightweight web application framework
- [gRPCio] - allows development of gRPC in python
- [Strawberry] - allows the hosting of graphql server 
- [requests] - simple HTTP requesting

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

# GraphQL
In this project, a **GraphQL** server for a fictional NFT server for **cryptofish**. This project is a good example to visualize the advantages of GraphQL over conventional REST API standards. GraphQL is designed in such a way that the client is able to ask or *query* all the data needed to the server and receives all of that even if the resources being requested reside in separate microservices, API endpoints, as well as databases. This allows the user to be able to obtain all the necessary information about the Cryptofish he owns and is available.

## Setting up GraphQL server
### Schema development
GraphQL servers use a schema to describe the structure of the stored data. It describes which data can be queried and mutated by the clients. Think of it as a database where each *type objects* refer to a database table. There are two main ways to design a schema : *schema-first* and *code-first*. 

The schema-first approach offers more readability with a sacrifice of flexibility `schema.graphql`, whereas the code-first approach offers more flexibility `schema.py`. Strawberry makes use exclusively of the latter and focuses more on the **resolver** development. The `object-types` for the schema looks like the following: 
**schema-first**: 
``` graphql
type SomeObject {
    id : ID!
    name : String
}

type Query {
    obtaineObject : SomeObject
}

type Mutation {
    changeObject : SomeObject
}
```
**code-first**: 
``` python
import strawberry

@strawberry.type
class SomeObject:
    id : strawberry.ID
    name : str | None
    
@strawberry.type
class Query:
    obtaine_object : SomeObject

@strawberry.type
class Mutation:
    change_object : SomeObject
```

The `!` means non-nullable. In Strawberry, all fields are non-nullable to begin with, so if a null value is allowed, `| None` must be added. It is importent to node that there are 4 types of schema items :  
`object-type` --> user-defined queryable object
`query-type` --> obtains resources by resolving the functions for it
`mutation-type` --> updates resources by resolving the functions for it
`subscription-type` --> stream resources from the server (not implemented here)
### Resolver development
In order to carry out a query or mutation, resolver functions have to be developed in order to perform the specific requests. Taking the example schema from above, a function has to be developed in order for the query to be able to perform the `obtain_object` query. This can be done two ways: 
``` python
def perform_obtain_object(self, object_id: strawberry.ID) -> SomeObject:
    # obtain data from resource-pool
    return SomeObject(id=object_id, name="Jack")

@strawberry.type
class Query:
    obtain_object: SomeObject = strawberry.field(resolver=perform_obtain_object)
```
or 
``` python
@strawberry.type
class Query:
    @strawberry.field
    def obtain_object(self, object_id: strawberry.ID) -> SomeObject:
        # obtain data from resource-pool
        SomeObject(id=object_id, name='Jack')
```
Mutations are implemented analogously to the Queries.
### Deploying Strawberry server
To deploy the Strawberry server, the following line has to be added in the python file. For example `schema.py`
``` python
schema = strawberry.Schema(query=Query)
```
then, the server can be executed by:
``` sh
strawberry server schema
```
which will output the following:
``` sh
Running strawberry on http://0.0.0.0:8000/graphql 🍓
```

By going to that address, we will be taken to an interactive GUI where queries can be made there. For example, running the query : 
``` graphql
{
    obtain_object (userid:5) {
        id
        name
    }
}
```
will return:
``` graphql
{
  "data": {
    "user": {
      "id": "2",
      "name": "Jack"
    }
  }
}
```
This can be carried out using curl command:
```curl
curl \
-X POST \
-H "Content-Type: application/json" \
--data '{"query": "{obtain_object(userid:1){id name}}"}' \
http://localhost:8000/graphql`
```


[//]: # 
   [flask]: <https://flask.palletsprojects.com/en/2.2.x/>
   [grpcio]: <https://grpc.io/docs/languages/python/quickstart/>
   [requests]: <https://requests.readthedocs.io/en/latest/>
   [strawberry]: <https://strawberry.rocks/>
   
