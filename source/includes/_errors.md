# Errors

ThingsDB uses the following error codes:


Error | Code | Meaning
------| ---- | -------
`OVERFLOW_ERROR` | -96 | Integer is too large to fit a 64 bit signed integer.
`ZERO_DIV_ERROR` | -97 | Trying a division or module by zero.
`MAX_QUOTA_ERROR` | -98 | Your collection has quotas set and the limit is reached.
`AUTH_ERROR` | -99 | Wrong credentials or a request while the connection is not authenticated.
`FORBIDDEN` | -100 | You lack the privileges to do the request.
`INDEX_ERROR` | -101 | Index out of range or trying to access an invalid property.
`BAD_REQUEST` | -102 | Invalid data, for example an invalid data type used in a query.
`QUERY_ERROR` | -103 | Syntax error in the query.
`NODE_ERROR` | -104 | At least one node has an issue while processing the request.
`ASSERTION_ERROR` | -105 | [Assertion](#assert) statement has failed.
`INTERNAL_ERROR` | -127 | Node is probably out-of-memory or out-of-disk-space.
