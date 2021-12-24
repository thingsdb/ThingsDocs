---
title: "future"
weight: 55
---

Futures are mainly used for modules, but they can also be used to run some code at some later time.
A future does not require a *change*. If the future is followed with a `then` or `else` closure, then the
code inside this closure will generate it's own event if required.

For example, the code below will always create a *change*, no matter what the value of `x` is. This is because ThingsDB
has to know if a *change* is required before it knows the value of `x`.

```thingsdb,syntax_only
if (x > 10, {
    .answers.push(x);
});
```

When using a future we could optimize the code:

```thingsdb,syntax_only
if (x > 10, {
    future(nil, x).then(|_, x| {
        .answers.push(x);  // This will still require a *change*, but the event
                           // is only created when x > 10.
    });
});
```

Instead of using the `future(nil, ..).then(|_, ..| ..)` construction, a future accepts a closure as first argument to be used as a shortcut. So the above can be written as:

```thingsdb,syntax_only
if (x > 10, {
    future(|x| {
        .answers.push(x);  // This will still require a *change*, but the event
                           // is only created when x > 10.
    });
});
```


### Modules

When a future is used to call a [module](../../modules), the first argument of the future will be the request for the module and must be a thing containing at least a `module` property.

For example, the code below will trigger the [module](../../modules) `DEMO`. The module would receive `{module: "DEMO"}` as request.

```thingsdb,syntax_only
future({
    module: 'DEMO'
});
```

Besides the required `module` property, a property `deep` will be understood and will tell ThingsDB how [deep](../../collection-api/deep) the request must be packed. The default *deep* value is one (`1`).

For example:

```thingsdb,syntax_only
// Deep must be at least 2, otherwise the items are not packed for the module request
future({
    module: 'DEMO',
    deep: 2,
    items: [{
        name: 'item1'
    }, {
        name: 'item2'
    }]
});
```

Data from a module is returned to ThingsDB as [mpdata](../../data-types/mpdata) by default. For example:

```thingsdb,syntax_only
// Suppose we have a DEMO module which accepts a message and returns with a reply message:
future({
    module: 'DEMO',
    message: 'This is a test'
}).then(|reply| type(reply));  // type reply will be `mpdata`, not `str` !!
```

The above is fine if we want the result, in this case the `reply`, back to our client. If we on the other hand want to do
something with the `reply` message, we can either choose to call [.load()](../../data-types/mpdata/load) on the `reply` value but
a better option would be to set the `load` property to `true` in the request, for example:

```thingsdb,syntax_only
// Suppose we have a DEMO module which accepts a message and returns with a reply message:
future({
    module: 'DEMO',
    load: true,
    message: 'This is a test'
}).then(|reply| type(reply));  // now `reply` is of type `str`
```

### Functions

Function | Description
------ | -----------
[then](./then) | Accepts a closure which will be executed when the future was successful.
[else](./else) | Accepts a closure which will be executed when the future has failed.

### Related functions

Function | Description
------ | -----------
[future](../../collection-api/future) | Create a new future.
[is_future](../../collection-api/is_future) | Test if a given value is of type future.
