# API Docs

## Internal API Endpoints
##### These endpoints are made for internal use in the bot only. As such user tokens will not work on these endpoints.

### `POST /logs`
#### Create a new log entry

Schema:
```json
{
    "text":"string"
}
```

Response:
```json
{
    "status":"ok",
    "id":"string"
}
```

### `GET /logs/{logid:string}`
#### Get a log entry. This endpoint returns a plaintext response made to be viewed in browsers.

---

## Public API Endpoints
##### These endpoints are made for external (and sometimes internal) use. Unless explicitly marked otherwise they require an `X-Api-Token` header to be passed with the request with your application token in it.

### `GET /`
#### This endpoint exists to show that the API is online. It takes no authentication.

Response:
```json
{
    "status":"ok"
}
```