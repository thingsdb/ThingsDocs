---
title: "Errors"
weight: 249
chapter: false
---

ThingsDB uses the following error codes:

Error | Code | Meaning
------| ---- | -------
[operation_err](./operation_err) | -63 | Operation is not valid in the current context.
[num_arguments_err](./num_arguments_err) | -62 | Wrong number of arguments.
[type_err](./type_err) | -61 | Object of inappropriate type.
[value_err](./value_err) | -60 | Object has the right type but an inappropriate value.
[overflow_err](./overflow_err) | -59 | Integer is too large to fit a 64 bit signed integer.
[zero_div_err](./zero_div_err) | -58 | Trying a division or modulo by zero.
[max_quota_err](./max_quota_err) | -57 | Some quota limit is reached.
[auth_err](./auth_err)| -56 | Wrong credentials or a request while the connection is not authenticated.
[forbidden_err](./forbidden_err) | -55 | You lack the privileges to do the request.
[lookup_err](./lookup_err) | -54 | Requested resource not found or index out of range.
[bad_data_err](./bad_data_err) | -53 | Invalid data, for example an invalid data type used in a query.
[syntax_err](./syntax_err)| -52 | Syntax error in the query.
[node_err](./node_err) | -51 | At least one node has an issue while processing the request.
[assert_err](./assert_err)| -50 | [Assertion](../collection-api/assert) statement has failed.

## Internal errors

Error | Code | Meaning
------| ---- | -------
`RESULT_TOO_LARGE` | -6 | Result size limit is exceeded. See the [configuration page](../getting-started/configuration) to configure this limit.
`REQUEST_TIMEOUT` | -5 | Timeout during this request.
`REQUEST_CANCEL` | -4 | A request is cancelled.
`WRITE_UV` | -3 | Write to stream error.
`MEMORY` | -2 | Memory allocation error.
`INTERNAL` | -1 | General internal error.

## Custom errors

The range `-127 .. -100` is reserved by ThingsDB for custom error codes although technically this range can be extended from `-127` up to `-64`.
See [err(..)](../collection-api/err) and [alt_raise(..)](../collection-api/err) for more information on how to use custom error codes.
