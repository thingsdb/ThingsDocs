---
title: "alt_raise"
weight: 206
---

This function will try a statement. If the statement is successful it will just return the result but in case of an error, it will re-raise the error using a given error code.
The following code below will illustrate how `alt_raise` works:

>Without an optional error message

```thingsdb,syntax_only
// the following code:
res = alt_raise(statement, error_code);

// is equivalent to:
res = try(statement);

if (is_err(res)) {
    raise(error_code, res.msg());
};
```

>With an error message

```thingsdb,syntax_only
// the following code:
res = alt_raise(statement, error_code, err_msg);

// is equivalent to:
res = try(statement);

if (is_err(res)) {
    raise(error_code, err_msg);
};
```

This function does *not* generate a [change](../../overview/changes).

### Function

`alt_raise(statement, code, [message])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
statement | any (required) | The statement to try.
code | int (required) | Integer error code between `-127` and `-50`.
message | str (optional) | Optional error message.

### Return value

The value for the specified *statement* when the *statement* is successful.

### Example

> Some examples on how ***alt_raise()*** can be used:

```thingsdb,should_err
set_type('Person', {
    name: 'str<3:20>'
});

alt_raise({
    // The code below will raise a value error since the name is not long enough
    Person{
        name: 'x'
    };
}, -100, "Type `Person` expects a name between 3 and 20 characters");
```
