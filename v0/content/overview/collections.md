---
title: "Collections"
weight: 15
---

Each collection can be thought of as an *object* to which properties can be
assigned. We call such an object a *Thing*. To access something in the collection, all you need
is to start with a `.` (dot), followed by a function or property name. Another way to access
the collection is to use the collection ID. All things which are *stored* in
ThingsDB get an unique ID. Since the collection root is also a Thing, it has it's own
id.

> For example, to read the collection ID:

```thingsdb,should_pass
.id();  // This will return the collection ID
```

To store something inside the collection you only need to make sure the data is attached to the collection.

> For example:

```thingsdb,should_pass
// Saves a number `42`
.number = 42;

// Saves some text to property `txt`
.txt = 'Hello ThingsDB!';

// Saves a new `thing` to property `car`
.car = {
    brand: 'Foo',
    wheels: 4,
};

// The last value will be the return value, it may be just `nil`
nil;
```

Reading data from a collection works similar, just ask for the property.

>For example:

```thingsdb,syntax_only
.txt;  // Returns the value of property `txt`
```

> Result in JSON format:

```json
"Hello ThingsDB!"
```

To return multiple properties at once, it is often useful to put them in an array:

```thingsdb,syntax_only
[.txt, .number];  // Returns both property `txt` and `number`
```

> And the result in JSON format:

```json
[
    "Hello ThingsDB!",
    42
]
```

Stored *things* will get an ID (`#`) from ThingsDB.

> For example look at our `car` example:

```thingsdb,syntax_only
.car;  // Returns the value of property `car`
```

> Result in JSON format (The ID (`#`) might differ since it is auto generated by ThingsDB)

```json
{
    "#": 17,
    "brand": "Foo",
    "wheels": 4
}
```

See the [Collection API](../../collection-api) documentation for functions which can be used to manipulate ThingsDB data.