import requests

url = "http://localhost:5000/graphql"
query = '''query{
    users{
        id
    }
}
'''

response = requests.post(url, json={'query': query})
print(response.json())