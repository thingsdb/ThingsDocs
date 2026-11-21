---
title: "Auto-conversion"
weight: 41
---

When working with external payloads (such as JSON or MessagePack), incoming data often uses generic primitive types instead of ThingsDB's richer types (like `datetime`, `regex`, `set`, enums, or nested typed instances).

To avoid manual mapping boilerplate, ThingsDB automatically converts compatible values to their target property definitions when initializing an instance from an existing `thing` or updating an instance with `.assign()`.

{{% notice info %}}
Automatic type conversion was introduced in ThingsDB **v1.11.2** and is not available in earlier versions.
{{% /notice %}}


---

## When Auto-conversion Applies

Auto-conversion **only** takes place in two situations:

1. **Initializing an instance from an existing `thing`:** `Type(thing)`
2. **Assigning properties via `.assign()`:** `instance.assign(thing)`

Direct literal instantiation (`Type{...}`) and standard property assignments (`instance.prop = val`) remain strictly typed and will raise a `type_err()` if the value does not already match the property definition:

```thingsdb,should_err
set_enum('Status', {
    Pending: 0,
    Complete: 1,
});

set_type('Task', {
    name: 'str',
    status: 'Status',
});

// Auto-conversion applies when initializing from a thing or using .assign()
task = Task({name: 'Build', status: 0});
task.assign({status: 1});

// Strict typing applies to literal initialization and direct property assignment
Task{name: 'Build', status: 0};  // type_err(): mismatch in type `Task`
task.status = 0;                 // type_err(): mismatch in type `Task`
```

---

## Supported Conversions

The table below lists all target property definitions that support automatic conversion:

| Target Type | Accepted Input | Conversion Rules & Format |
| :--- | :--- | :--- |
| `int` | `float` | Must represent an exact whole number (e.g., `3.0` -> `3`). Floats with a non-zero fractional part (e.g., `3.1`) raise a [value_err()](../../errors/value_err). Other types like [bool](../../data-types/bool) are not converted. |
| `float` | `int` | Converted directly to [float](../../data-types/float) (e.g., `6` -> `6.0`). |
| `regex` | `str` | Must be formatted as `"/expression/flags"`. |
| `closure` | `str` | Must be valid closure syntax, e.g., `"\|args\| body"`. |
| `uuid` | `str`, `bytes` | Must be a valid UUID string (e.g., `"550e8400-e29b-41d4-a716-446655440000"`) or a 16-byte [bytes](../../data-types/bytes) value (such as binary UUIDs from MessagePack). |
| `datetime` | `str` | Must be a valid ISO 8601 date/time string (e.g., `"2026-11-20T22:32:28Z"`). |
| `timeval` | `int`, `float` | Interpreted as a UNIX timestamp in seconds. |
| `enum` | `str`, _enum member type_ | All enum types are supported. If the input is a str, it is checked against member names first, and then against member values. |
| `error` | `str` | Converted to an [error](../../data-types/error) using the string as the error message and the default error code `-100`. |
| `array` (`[...]`) | `array` | Elements are recursively converted to match the array's item definition. |
| `set` (`{...}`) | `array` | Converted to a [set](../../data-types/set), with elements recursively converted to match the set's item definition. |
| `thing<T>` | `thing` | Values inside the [thing](../../data-types/thing) are recursively converted to match definition `T`. |
| *Custom Type* | `thing`, `int` | A [thing](../../data-types/thing) is recursively converted into a new instance of the target type. An [int](../../data-types/int) is resolved to an existing instance with that Id in the current collection. |

---

## Examples

### Nested Types and Collections

Auto-conversion works recursively across nested types, sets, arrays, and references to existing instances by Id:

```thingsdb,should_pass
set_enum('Status', {
    Pending: 0,
    Complete: 1,
});

set_type('User', {
    id: '#',
    name: 'str',
    email: 'email',
});

set_type('Task', {
    id: '#',
    name: 'str',
    status: 'Status',
    due: 'datetime?',
});

set_type('Job', {
    id: '#',
    title: 'str',
    user: '&User',
    tasks: '&{Task}',
});

.users = [
    User{name: 'Iris', email: 'iris@example.com'},
];

// Assume user Iris has Id #2
payload = {
    title: 'Release v2.0',
    user: 2,
    tasks: [
        {name: 'Run tests', status: 1, due: '2026-11-20T22:32:28Z'},
        {name: 'Deploy', status: 'Pending'},
    ],
};

// Automatically resolves user #2, converts tasks array to a set of Task instances,
// converts status values to Status enums, and parses the ISO string into a datetime.
job = Job(payload);
```

### Primitive and Scalar Conversions

This example shows how scalar types, closures, regular expressions, and typed arrays are converted—along with what happens when a value cannot be safely converted:

```thingsdb,should_err
set_type('Sample', {
    count: 'int',
    ratio: 'float',
    pattern: 'regex',
    callback: 'closure',
    created: 'timeval',
    updated: 'datetime',
    uid: 'uuid',
    raw_uid: 'uuid',
    scores: '[int]',
});

s = Sample({
    count: 5.0,                                          // -> int: 5
    ratio: 2,                                            // -> float: 2.0
    pattern: '/^item-[0-9]+$/i',                         // -> regex: /^item-[0-9]+$/i
    callback: '|x| x * 2',                               // -> closure: |x| x * 2
    created: 1795214029,                                 // -> timeval: 2026-11-20T22:33:49Z
    updated: '2026-11-20T22:33:49Z',                     // -> datetime: 2026-11-20T22:33:49Z
    uid: '550e8400-e29b-41d4-a716-446655440000',         // -> uuid: 550e8400-e29b-41d4-a716-446655440000
    raw_uid: base64_decode('VQ6EAOKbQdSnFkRmVUQAAA=='),  // -> uuid: 550e8400-e29b-41d4-a716-446655440000
    scores: [10.0, 20.0, 30.0],                          // -> [int]: [10, 20, 30]
});

// Inspect the converted types and values
[
    type(s.count),      // "int"
    type(s.ratio),      // "float"
    type(s.pattern),    // "regex"
    type(s.callback),   // "closure"
    type(s.created),    // "timeval"
    type(s.updated),    // "datetime"
    type(s.uid),        // "uuid"
    type(s.raw_uid),    // "uuid"
    s.scores,           // [10, 20, 30]
];

// Fractional floats are rejected to prevent silent data loss
Sample({count: 5.5});   // value_err(): cannot convert float with fractional part to integer
```