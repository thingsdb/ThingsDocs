---
title: "decrypt"
weight: 46
---

Decrypts an encrypted bytes value created with [encrypt](../encrypt) using **AES-256-GCM** authenticated encryption.

A 256-bit decryption key is derived from the given `key` using **SHA-256**, and the embedded GCM authentication tag is verified before returning the plaintext. If the encrypted data is malformed or decrypted with an incorrect key, a [bad_data_err](../../../errors/bad_data_err) is raised.

This function does *not* generate a [change](../../../overview/changes).

### Function

*bytes*.`decrypt(key)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
`key` | `str` or `bytes` | The non-empty secret passphrase or binary key used when encrypting the data.

### Return value

Returns the decrypted `bytes` value.

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