---
title: "HTTP API"
weight: 11
---


The ThingsDB HTTP API requires at least one node within your cluster to have the API port enabled, as it's disabled by default.
To activate it, edit the `http_api_port` setting in your ThingsDB [configuration file](https://github.com/thingsdb/ThingsDB/blob/main/thingsdb.example.conf)
or set the `THINGSDB_HTTP_API_PORT` environment variable. You can use a common port like `9210` for this purpose.

The API has support for both [MessagePack](https://msgpack.org) and [JSON](https://www.json.org) and can be used to perform queries and run procedures.

{{% notice tip %}}
Use **MessagePack** if possible since this is the data serialization protocol which is used by ThingsDB
internally and therefore is faster than JSON. It also allows for sending and receiving binary data and is usually more compact than JSON.
In most examples we use JSON just because it is more readable.
{{% /notice %}}

## Headers

The header field `Content-Type` is required and needs to be either `application/msgpack` or `application/json`.

## Query request

field | description
----- | -----------
`type` | Required and must be `query` for a query request.
`code` | Required string with the query code to preform.
`vars` | Optional and may contain a `map` where the `keys` are variable names and the `values` will be the variable values.

## Query example

> Example using *curl* with *token* authentication: (using a playground collection `Doc`)

```bash
curl --location --request POST 'https://playground.thingsdb.net//Doc' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer Fai6NmH7QYxA6WLYPdtgcy' \
--data-raw '{
	"type": "query",
	"code": ".greetings.choice();"
}'
```

{{% notice note %}}
[choice()](../../data-types/list/choice) returns a random item from the `.greetings` array)
{{% /notice %}}

> Possible response

```json
"Hi!"
```

Besides the preferred **token** authentication, the HTTP API has also support for **basic** authentication.

> Another *curl* example using *basic* authentication using user `Doc` with password `pass`:

```bash
curl --location --request POST 'https://playground.thingsdb.net//Doc' \
--header 'Content-Type: application/json' \
--user Doc:pass \
--data-raw '{
	"type": "query",
	"code": "1 + 1;"
}'
```

> Response:

```json
2
```

### Localhost

Make sure to enable the HTTP API if you want to use it. By default the HTTP API is disabled.

In this example we start _thingsdb_ with an environment variable to enable the HTTP API on port 9210:

```text
THINGSDB_HTTP_API_PORT=9210 /path/to/thingsdb --log-level info
```

The logging should now include something like this line:

```text
[I 2022-09-16 09:10:42] start listening for HTTP API requests on TCP port 9210
```

Test a HTTP API request to ThingsDB:

```bash
curl --location --request POST 'http://localhost:9210//stuff' \
--header 'Content-Type: application/json' \
--user admin:pass \
--data-raw '{
	"type": "query",
	"code": "1 + 1;"
}'
```

## Run request

field | description
----- | -----------
`type` | Required and must be `run` for a run request.
`name` | Name of the procedure to run.
`args` | Array or map with arguments for the procedure.

## Run example

The ThingsDB playground has a collection `Doc` with a [procedure](../../procedures-api) named `multiply` which accepts two arguments and returns the two arguments multiplied.

> If you want to create the `multiply` procedure yourself, this is the code:

```thingsdb,should_pass
new_procedure('multiply', |a, b| a*b);
```

> Example using the playground:

```bash
curl --location --request POST 'https://playground.thingsdb.net//Doc' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer Fai6NmH7QYxA6WLYPdtgcy' \
--data-raw '{
	"type": "run",
	"name": "multiply",
	"args": [6, 7]
}'
```

> Response

```json
42
```

{{% notice note %}}

Instead of providing the arguments as an array, they also could be given as a map, for example `{"a": 6, "b": 7}`.

{{% /notice %}}
