---
title: "Statements"
weight: 35
---

ThingsDB has support for the following statements:

Statement  | Description
---------- | -----------
[return](#return)     | Return a value and optionally define a *deep* value.
[if..else](#ifelse)   | Execute a code block when a condition evaluates to `true`. Optionally, execute a different code block when the conditions evaluates to `false`.
[for..in](#forin)     | Loop over an iterable object. The block of code inside the loop will be executed once for every item.
[break](#break)       | Break out a loop.
[continue](#continue) | Jump over one iteration in a loop.


## return

Every ThingsDB query will have a return value. If no `return` statement is used, then the *return value* will be the value of the last statement.
It is therefore not required to use the `return` statement unless you want to return with a value *before* the end of the code is reached. The `return` statement also accepts a second and third argument to specify a different [deep](../../collection-api/deep) level and optional [flags](#return-flags) together with `return`.


{{% notice note %}}
Starting with ThingsDB version 1.7.4, the `return` statement can be used without arguments. This makes `return;` equivalent to `return nil;`.
{{% /notice %}}

When the return statement is used without additional arguments,

Example usage of the *return* statement:

```thingsdb,json_response
for (i in range(5)) {
    if (i == 3) {
        return `Number {i}`;
    };
};
```

> Return value in JSON format

```json
"Number 3"
```

Example *return* with an explicit *deep* value:

```thingsdb,json_response
return {
    nested: {
        text: 'this is a thing with a second level'
    }
}, 2;  // use *deep* 2 to return 2 levels deep
```

> Return value in JSON format

```json
{
    "nested": {
        "text": "this is a thing with a second level"
    }
}
```

### return flags

Flag   | Description
------ | -----------
NO_IDS | Return things without ID's, even when the _things_ are stored.

> Example use of the `NO_IDS` flags:

```thingsdb,json_response
.my_thing = {
    text: "this is an example without #"
};

// Return "my_thing", 1 level deep, without ID (#)
return .my_thing, 1, NO_IDS;
```

> Return value in JSON format

```json
{
    "text": "this is an example without #"
}
```

## if..else

Use the `if` and optional `else` statement to executes a block of code if a specified condition is `true`. If the condition is `false`, another block of code can be executed.

Example *if..else*:

```thingsdb,json_response
size = 123;  // Just some example value

if (size < 10) {
    return 'small';
} else if (size < 100) {
    return 'medium';
} else {
    return 'large';
};
```

> Return value in JSON format

```json
"large"
```

## for..in

The `for..in` statement can be used to loop over an iterable value like a [thing](../../data-types/thing), [list](../../data-types/list) or [thing](../../data-types/set).

Loop over a list:

```thingsdb,json_response
arr = [];

// Note that the `index` is optional
for (item, index in ['laptop', 'bike', 'camera']) {
    arr.push(`Item '{item}' at index {index}`);
};

arr;
```

> Return value in JSON format

```json
[
    "Item 'laptop' at index 0",
    "Item 'bike' at index 1",
    "Item 'camera' at index 2"
]
```

Loop over a thing:

```thingsdb,json_response
store = {
    books: 80,
    bikes: 5,
    laptops: 3
};
arr = [];

// Note that the `value` is optional
for (key, value in store) {
    arr.push(`Number of '{key}' in stock: {value}`);
};

arr;  // The order might be different
```

> Example return value in JSON format

```json
[
    "Number of 'books' in stock: 80",
    "Number of 'bikes' in stock: 5",
    "Number of 'laptops' in stock: 3"
]
```

### break

Within a `for..in` statement, the `break` statement can be used to *break out* of the loop.

For example, the code below will *break out* the loop when `i` is equal to `3`.

```thingsdb,json_response
arr = [];

for (i in range(5)) {
    if (i == 3) {
        break;
    };
    arr.push(`Number {i}`);
};

arr;
```

> Return value in JSON format

```json
[
    "Number 0",
    "Number 1",
    "Number 2"
]
```

### continue

Within a `for..in` statement, the `continue` statement can be used to *jump over* one iteration in the loop.

For example, the code below will *jump over* one iteration when `i` is equal to `3`.

```thingsdb,json_response
arr = [];

for (i in range(5)) {
    if (i == 3) {
        continue;
    };
    arr.push(`Number {i}`);
};

arr;
```

> Return value in JSON format

```json
[
    "Number 0",
    "Number 1",
    "Number 2",
    "Number 4"
]
```