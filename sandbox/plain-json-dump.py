import json

plain = {
  "nodes": [
    {
      "id": 1,
      "name": "authToken",
      "request_url": "https://httpbin.org/post",
      "method": "POST",
      "request_body": {
        "username": "demo",
        "password": "demo123"
      },
      "request_headers": {},
      "query_params": {},
      "condition": "true"
    },
    {
      "id": 2,
      "name": "getUser",
      "request_url": "https://jsonplaceholder.typicode.com/users/1",
      "method": "GET",
      "request_body": {},
      "request_headers": {},
      "query_params": {},
      "condition": "true"
    },
    {
      "id": 3,
      "name": "getUserProfile",
      "request_url": "https://httpbin.org/get",
      "method": "GET",
      "request_body": {},
      "request_headers": {
        "Authorization": "Bearer {{authToken.json.token}}"
      },
      "query_params": {},
      "condition": "true"
    },
    {
      "id": 4,
      "name": "getInternalData",
      "request_url": "https://httpbin.org/basic-auth/demo/pass",
      "method": "GET",
      "request_body": {},
      "request_headers": {
        "Authorization": "Basic {{'demo:pass' | base64}}"
      },
      "query_params": {},
      "condition": "true"
    }
  ]
}

print(json.dumps(plain))
