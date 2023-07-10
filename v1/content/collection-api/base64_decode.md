---
title: "base64_decode"
weight: 197
---

Decode a Base64 encoded string.

See [base64_encode](../base64_encode) for Base64 encoding.

This function does *not* generate a [change](../../overview/changes).

### Function

`base64_decode(encoded)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
encoded | str/bytes | The string value to decode.

### Return value

Decoded [bytes](../../data-types/bytes) value is returned.

### Example

> This code shows an example for *base64_decode*:

```thingsdb,json_response
encoded = 'YmFzZTY0IGVuY29kZWQgc3RyaW5n';

// decode
data = base64_decode(encoded);

// result is of type bytes
assert(type(data) == 'bytes');

// return as string
str(data);
```

> Return value in JSON format

```json
"base64 encoded string"
```
