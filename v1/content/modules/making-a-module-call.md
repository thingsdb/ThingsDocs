---
title: "Making a module call"
weight: 426
---

Modules extend ThingsDB with external functionality—such as making HTTP requests, sending emails, or interacting with third-party services. When you call a method on a module, ThingsDB executes the call asynchronously and returns a [future](../../data-types/future/).

This guide walks through installing a module, inspecting its exposed methods, passing arguments, and handling responses with `.then()` and `.fail()` callbacks.

---

## 1. Installing and inspecting a module

As an example, install the [`requests`](https://github.com/thingsdb/module-go-requests) module from the `@thingsdb` scope:

```thingsdb,syntax_only
new_module('requests', 'github.com/thingsdb/module-go-requests');
```

Once installed, inspect the module with [`module_info()`](../../thingsdb-api/module_info/) to see if configuration is required and which methods the module exposes:

```thingsdb,syntax_only
module_info('requests');
```

In the output, you will see the module's `schema` version along with its exposed methods. For example, the `get` method is defined with the following `argmap` and `defaults`:

```json
{
    "get": {
        "doc": "Make a GET request",
        "defaults": {
            "method": "GET"
        },
        "argmap": ["url", "*"]
    }
}
```

### Understanding `argmap` and `defaults`

* **`argmap` (`["url", "*"]`):** Defines the positional arguments accepted by the module method:
  1. The first argument (`"url"`) is required and is mapped to the `url` key in the payload sent to the module.
  2. The wildcard (`"*"`) represents an optional second argument that must be either `nil` (no extra options) or a `thing` containing additional options such as `headers` or query parameters.
* **`defaults` (`{"method": "GET"}`):** Automatically merged into the payload sent to the module, so you do not need to specify `"method"` yourself.

---

## 2. Calling a method and using callbacks

Because `get` defines two arguments in its `argmap` (`url` and `*`), **any arguments passed after those two** are forwarded directly to your `.then()` and `.fail()` callbacks.

```thingsdb,syntax_only
results = [];

// Arguments:
// 1. url ('https://api.infrasonar.com/healthy')
// 2. *   (nil, or a thing with extra options like {headers: {...}})
// 3+.    Extra arguments forwarded to .then() / .fail() callbacks
requests
    .get('https://api.infrasonar.com/healthy', nil, results)
    .then(|response, results| {
        // The first argument is always the module response,
        // followed by any extra arguments passed to the call.
        results.push(str(response.load().body));  // Adds "OK" to results
    })
    .fail(|error, results| {
        // The first argument is a ThingsDB error,
        // followed by any extra arguments passed to the call.
        results.push(error);
    });

results;
```

> **Note:** While collecting results into a local `results` array is not particularly useful on its own—since the query finishes before the asynchronous future resolves—it demonstrates how state and context arguments can be passed safely into `.then()` and `.fail()` callbacks.

### What the module receives

With `nil` passed as the second argument, ThingsDB builds and sends the following payload to the module:

```json
{
    "url": "https://api.infrasonar.com/healthy",
    "method": "GET"
}
```

If you instead pass a `thing` such as `{headers: {'Accept': 'text/plain'}}` as the second argument, its properties are merged into the payload:

```json
{
    "url": "https://api.infrasonar.com/healthy",
    "method": "GET",
    "headers": {
        "Accept": "text/plain"
    }
}
```

---

## 3. Returning a module future directly

Instead of attaching `.then()` or `.fail()` callbacks, you can return a module future directly as the result of your query so ThingsDB resolves it before sending the response back to the client:

```thingsdb,syntax_only
requests.get('https://api.infrasonar.com/healthy');
```

How the resolved value is returned to the client depends on the module's **`schema`** version (visible in `module_info()`):

| Module `schema` | Direct return value to client | Notes |
| :--- | :--- | :--- |
| **`schema: 2`** | `response` | Returns **only** the module's result. |
| **`schema: 1`** *(legacy / default)* | `[response, ...extra_args]` | Returns an array containing the module's result followed by any extra callback arguments. |

In both schema versions, `.then(|response, ...extra_args| ...)` and `.fail(|error, ...extra_args| ...)` continue to receive all extra arguments. If you use a `schema: 2` module and still want to return both the response and extra arguments to the client, return them explicitly from `.then()`:

```thingsdb,syntax_only
requests
    .get('https://api.infrasonar.com/healthy', nil, 'my-context')
    .then(|response, ctx| [response, ctx]);
```