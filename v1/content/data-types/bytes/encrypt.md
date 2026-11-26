---
title: "encrypt"
weight: 47
---

Encrypts the bytes value using **AES-256-GCM** authenticated encryption.

A 256-bit encryption key is derived from the given `key` using **SHA-256**, and a fresh 12-byte random initialization vector (IV) is generated on each call. The resulting byte sequence contains a 1-byte version header, the 12-byte IV, the 16-byte GCM authentication tag, and the ciphertext.

This function does *not* generate a [change](../../../overview/changes).

### Function

*bytes*.`encrypt(key)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`key` | `str` or `bytes` | A non-empty secret passphrase or binary key used to encrypt the data.

### Return value

Returns the encrypted `bytes` value, which can be decrypted with [decrypt](../decrypt).

### Example

> This code encrypts a byte sequence and decrypts it back to a string:

```thingsdb,json_response
secret = bytes("sensitive payload").encrypt("my-secret-passphrase");
str(secret.decrypt("my-secret-passphrase"));
```

> Return value in JSON format

```json
"sensitive payload"
```