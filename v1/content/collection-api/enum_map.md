---
title: "enum_map"
weight: 224
---

Returns a thing with key/value pairs for all the members of a given enum.

This function does *not* generate a [change](../../overview/changes).

### Function

`enum_map(enum)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
enum | str | The name of the enum to return as a thing.

### Return value

Returns a [thing](../../data-types/thing) with key/value pairs for all the members of the given enumerator.

### Example

> This code shows the output of ***enum_map()***:

```thingsdb,json_response
// Just a simple enum as an example
set_enum('Color', {
    RED: '#ff0000',
    GREEN: '#00ff00',
    BLUE: '#0000ff',
});

// Return enum as thing
enum_map('Color');
```

> Example return value in JSON format

```json
{
    "RED": "#ff0000",
    "GREEN": "#00ff00",
    "BLUE": "#0000ff"
}
```
