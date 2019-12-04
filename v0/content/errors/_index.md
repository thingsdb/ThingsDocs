---
title: "Errors"
weight: 174
chapter: true
---

# Errors

ThingsDB uses the following error codes:

Error | Code | Meaning
------| ---- | -------
[operation_err](./operation_err) | -63 | Operation is not valid in the current context.
[num_arguments_err](./num_arguments_err) | -62 | Wrong number of arguments.
[type_err](./type_err) | -61 | Object of inappropriate type.
[value_err](./value_err) | -60 | Object has the right type but an inappropriate value.
[overflow_err](./overflow_err) | -59 | Integer is too large to fit a 64 bit signed integer.
[zero_div_err](./zero_div_err) | -58 | Trying a division or module by zero.
[max_quota_err](./max_quota_err) | -57 | Your collection has quotas set and the limit is reached.
[auth_err](./auth_err)| -56 | Wrong credentials or a request while the connection is not authenticated.
[forbidden_err](./forbidden_err) | -55 | You lack the privileges to do the request.
[lookup_err](./lookup_err) | -54 | Requested resource not found or index out of range.
[bad_data_err](./bad_data_err) | -53 | Invalid data, for example an invalid data type used in a query.
[syntax_err](./syntax_err)| -52 | Syntax error in the query.
[node_err](./node_err) | -51 | At least one node has an issue while processing the request.
[assert_err](./assert_err)| -50 | [Assertion](../collection-api/assert) statement has failed.
