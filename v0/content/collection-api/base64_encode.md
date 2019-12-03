---
title: "base64_encode"
weight: 84
---

Encode a [str](../../data-types/str) or [bytes](../../data-types/bytes) value using Base64.

See [base64_decode](../base64_decode) for Base64 decoding.

This function does *not* generate an [event](../../overview/events).

### Function

`base64_encode(string)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
string | str/bytes | The value to encode.

### Return value
Encoded [str](../../data-types/str) value is returned.

### Example

> This code shows an example for *base64_encode*:

```thingsdb,json_response
encoded = base64_encode('base64 encoded string');

// result is of type str
assert( type(encoded) == 'str');

// return
encoded;
```

> Return value in JSON format

```json
"YmFzZTY0IGVuY29kZWQgc3RyaW5n"
```

