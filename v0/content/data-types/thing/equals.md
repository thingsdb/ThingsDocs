---
title: "equals"
weight: 113
---

Determines if a [thing](..) is equal to another thing.

Comparing things is usually done with a strict compare, for example:

```thingsdb,syntax_only
{} == {};  // This is *false* because left and right are not the same object
```

Function *equals* can be used to perform a weak compare, for example:

```
{}.equals({});  // This is *true*, both objects have the same content.
```

{{% notice note %}}
By default the *equals* function will only compare values **one** level deep. An optional second
argument can be used to change this behavior. Any integer value
between `0` and `127` is allowed.
{{% /notice %}}

This function does *not* generate an [event](../../../overview/events).

### Function

*thing*.`equals(other, [deep])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
other | any (required) | Value to compare.
deep | int (required) | How *deep* to compare the values. Default is `1`.

### Return value

Returns `true` when the *other* thing has the same properties and values as the original thing, otherwise `false`.

### Example

> This code shows an example use case of ***equals()***:

```thingsdb,json_response
a = {
    name: 'Iris',
    sport: {
        name: 'Cycling'
    }
};

b = {
    name: 'Iris',
    sport: {
        name: 'Swimming'
    }
};

assert (a != b );           // a and b are not equal
assert (a.equals(b) );      // a and b are equal on the first "level"

a.equals(b, 2);             // return `false`, as sport is different
```

> Return value in JSON format

```json
false
```
