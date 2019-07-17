# Errors

ThingsDB uses the following error codes:

Error | Code | Meaning
------| ---- | -------
[overflow_err](#overflow_err) | -59 | Integer is too large to fit a 64 bit signed integer.
[zero_div_err](#zero_div_err) | -58 | Trying a division or module by zero.
[max_quota_err](#max_quota_err) | -57 | Your collection has quotas set and the limit is reached.
[auth_err](#auth_err)| -56 | Wrong credentials or a request while the connection is not authenticated.
[forbidden_err](#forbidden_err) | -55 | You lack the privileges to do the request.
[index_err](#index_err) | -54 | Index out of range or trying to access an invalid property.
[bad_data_err](#bda_data_err) | -53 | Invalid data, for example an invalid data type used in a query.
[syntax_err](#syntax_err)| -52 | Syntax error in the query.
[node_err](#node_err) | -51 | At least one node has an issue while processing the request.
[assert_err](#assert_err)| -50 | [Assertion](#assert) statement has failed.
