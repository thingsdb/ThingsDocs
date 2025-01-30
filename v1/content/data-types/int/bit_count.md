---
title: "bit_count"
weight: 68
---

Return the number of ones in the binary representation of the absolute value of the integer.

This function does *not* generate a [change](../../../overview/changes).

### Function

*int*.`bit_count()`

### Arguments

None

### Return value

Return the number of ones in the binary representation of the absolute value of the integer.

### Example

> This code creates a room, gives the room a name and uses the _name()_ function to return the name.

```thingsdb,json_response
(42).bit_count();  // Returns 3, binary representation: 0b101010
```

> Return value in JSON format

```json
3
```
