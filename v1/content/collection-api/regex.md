---
title: "regex"
weight: 305
---

Create a new regular expression.

This function can be used to create a regular expression from a given pattern with optional flags.

The syntax `/pattern/flags` can be translated to `regex(pattern, flags)` so the following is true:

```thingsdb,should_pass
assert( /^api_.*/i == regex("^api_.*", "i") );  // the same!
```

This function does *not* generate a [change](../../overview/changes).

### Function

`regex(pattern, [flags])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
pattern | str (required) | The pattern to use as a regular expression.
flags | str (optional) | Optional flags, see the [regex](../../data-types/regex#flags) for more information.


### Return value

A new regular expression.

### Example

> Returns a new regular expression from a pattern.

```thingsdb,should_pass
// match strings which start with "the ", case in-sensitive (`i` flag)
re = regex("^the\s", "i");

re.test("The Pretenders");
```

> Example return value in JSON format

```json
true
```
