---
title: "nse"
weight: 304
---

This function promises ThingsDB that your code has _no-side-effects_ and therefore does not require a [change](../../overview/changes).

Suppose you use the following code:
```thingsdb,should_pass
response = {};
response.text = "Some message";  // This enforces a change
response;  // Return the response
```

On the second code line, ThingsDB doesn't know if _response_ is a stored object or not. Therefore ThingsDB will create a change.
Although the code example above is very simple and in this case can be simply re-written to avoid a change, it is not always that simple.

Function `nse()` could be used to _promise_ ThingsDB that your code does not require a change.

```thingsdb,should_pass
nse();  // Promise we don'n need a change
response = {};
response.text = "Some message";
response;  // Return the response
```

{{% notice info %}}
This function can raise an _Operation error_ if there are _side-effects_ which can't be avoided. For example when a function really does require a change like `nse(); new_type('T');`. This is not the case when `nse()` is used after a change is already made, for example `.x = 1; nse();` will run and create a change as _nse_ is used after the change.
{{% /notice %}}

This function does *not* generate a [change](../../overview/changes).

### Function

`nse([statement])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
statement | any (optional) | Statement or block to wrap.

### Return value

Return value of the given statement or `nil`.

### Example

> This code shows an example usage for ***nse()***:

```thingsdb,json_response
// We don't make a change to the collection
nse();

response = {};
response.text = "Some message";  // This tells ThingsDB to create a change
response.changeId = change_id();  // This should be nil
response;  // Return the response
```

> Return value in JSON format

```json
{
    "text": "Some message",
    "changeId": null
}
```
