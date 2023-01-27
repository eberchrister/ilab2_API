from flask import Flask, request, jsonify
from strawberry.flask.views import GraphQLView
import strawberry
from query import Query
from mutation import Mutation

schema = strawberry.Schema(query=Query, mutation=Mutation)
app = Flask(__name__)

app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql_view", schema=schema, graphiql=True)
)

if __name__ == '__main__':
    app.run(debug=True)