---
title: "Properties"
weight: 27
---

Properties are key/value pairs which are assigned to a `thing`. The collection itself is also a `thing` to which properties can be assigned.
For example: `.answer = 42;` creates a property `answer` with value `42` and the property will be assigned to the collection.

The `key` of a property must be of type [string](../../data-types/str). If the key is *not* a valid [name](../names), then the property can be set by using
the square bracket `[..]` notation or the [set(..)](../../data-types/thing/set) / [get(..)](../../data-types/thing/get) functions can be used.

There are 16, single character keys that are reserved for ThingsDB and cannot be used as key strings:

key | description
--- | -----------
` ` *(space)* | *unused*
`!` | Reserved for errors.
`"` | Reserved for timeval.
`#` | Reserved for thing ID's.
`$` | Reserved for sets.
`%` | Reserved for enumerator members.
`&` | Reserved for wrapped things.
`'` | Reserved for datetime.
`(` | *unused*
`)` | *unused*
`*` | Reserved for regular expressions.
`+` | *unused*
`,` | *unused*
`-` | *unused*
`.` | Reserved for type.
`/` | Reserved for closures.

### Example


```thingsdb,json_response
x = {};

// Character `!` is reserved and cannot be used as key
assert(is_err(try({
    x['!'] = nil;
})));

// Note that it is fine to use the `!` in any other combination as key
// For example, the following key is perfectly valid:
x['!!'] = nil;

x;
```

> Return value in JSON format

```json
{
    "!!": null
}
```