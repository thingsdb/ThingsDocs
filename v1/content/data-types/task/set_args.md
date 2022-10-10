---
title: "set_args"
weight: 147
---

Set task arguments.

If less than the required arguments are given, then the remaining arguments will
be set using `nil`. A [num_arguments_err()](../../../errors/num_arguments_err) is raised if the task too much arguments are used.

{{% notice warning %}}
When the task is created in the `@thingsdb` scope, only *(some)* immutable types like `int`, `float`, `str` etc. can be used as argument values.
{{% /notice %}}

This function generates a [change](../../../overview/changes).

### Function

*task*.`set_args(args)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
args | list (required) | List with task arguments.

### Return value

Returns `nil` when successful.

### Example

> This code will will be called every minute for 10 times and then the task will be removed.

```thingsdb,should_pass

task(
    datetime(),
    |task, x| {
        task.set_args([x+1]);
        if (x < 10) {
            log(`x = {x}`);
            task.again_in('seconds', 10);
            return nil;
        };
        log('Task `count x` is Done!');
    },
    [1]
);

```
