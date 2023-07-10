---
title: "enum_info"
weight: 208
---

Returns information about a given [enumeration type](../../data-types/enum).

Value | Description
------- | -----------
`enum_id` | Internal enum Id *(can be used to identify Enums in collection events)*.
`created_at` | [Time Stamp](https://wikipedia.org/wiki/Unix_time) when the enum is created.
`default` | Default member of this enumerator. The default member is used when implicitly creating a value of this enumerator type. See [mod_enum(..)](../mod_enum/def) to change the deafult member.
`modified_at` | [Time Stamp](https://wikipedia.org/wiki/Unix_time) when the enum is last modified or `nil` if never modified.
`name` | Enum's name.
`members` | Array with arrays containing two strings, the name and value.
`methods` | Object with methods where the key is the method name and the value an object containing information about the closure.

This function does *not* generate a [change](../../overview/changes).

### Function

`enum_info(enum)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
enum | str | The name of the enum for which the information has to be returned.

### Return value

Returns [mpdata](../../data-types/mpdata) about the enumeration type.

### Example

> This code shows the output of ***enum_info()***:

```thingsdb,should_pass
// Just a simple enum as an example
set_enum('Color', {
    RED: '#ff0000',
    GREEN: '#00ff00',
    BLUE: '#0000ff',
    fmt: |this| `Color: {this.name()} Hex: {this}`
});

// Return enum info
enum_info('Color');
```

> Example return value in JSON format

```json
{
    "created_at": 1687890073,
    "default": "RED",
    "enum_id": 0,
    "members": [
        [
            "RED",
            "#ff0000"
        ],
        [
            "GREEN",
            "#00ff00"
        ],
        [
            "BLUE",
            "#0000ff"
        ]
    ],
    "methods": {
        "fmt": {
            "arguments": [
                "this"
            ],
            "definition": "|this| `Color: {this.name()} Hex: {this}`",
            "doc": "",
            "with_side_effects": false
        }
    },
    "modified_at": null,
    "name": "Color"
}
```
