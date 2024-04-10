---
title: "thing"
weight: 158
---

A Thing in ThingsDB is a _key/value_ object where each key must be of type [str](../str) _(except for some [reserved properties](../../overview/properties))_ and values can be any type.
For as long as a thing is used as a variable and not _stored_ in a collection, a thing does not have an Id. Only when a _thing_ is attached and therefore stored in a collection, ThingsDB will assign an Id to the `#` property. This property is not accessible but can be read using the [id()](./id) function. _See [examples](#examples) below._

### Functions

Function | Description
------ | -----------
[assign](./assign) | Copies properties from a thing.
[clear](./clear) | Remove all properties from a thing.
[copy](./copy) | Copy a thing to a new thing. A Type is *not* preserved.
[del](./del) | Remove a property.
[dup](./dup) | Duplicate a thing while preserving the Type.
[each](./each) | Iterate over all properties of a thing.
[equals](./equals) | Test if two things are equal.
[filter](./filter) | Return a new `thing` with properties that pass a given test.
[get](./get) | Return the value of a property on a thing by a given property name.
[has](./has) | Determine if a thing has a given property.
[id](./id) | Return `id` of the thing or `nil` when the thing is not stored.
[keys](./keys) | Return a list with all the property names of a thing.
[len](./len) | Return the number of items.
[map](./map) | Return a [list](../list) with the results of calling a provided closure on every property.
[remove](./remove) | Remove properties that pass a given test and returns the removed *values* in a list.
[ren](./ren) | Rename a property.
[restrict](./restrict) | Set or remove a value restriction on a thing.
[restriction](./restriction) | Return the restriction of the thing or `nil` when the thing is not restricted.
[search](./search) | Search for a given thing within a thing.
[set](./set) | Create a new or overwrite an existing property on a thing.
[to_type](./to_type) | Converts a thing into a [typed](../typed) thing.
[values](./values) | Return a list with all the property values of a thing.
[vmap](./vmap) | Returns a new thing with equal keys but values as a result of a given closure.
[wrap](./wrap) | Wrap the *thing* with a [Type](../../overview/type).

### Examples

```thingsdb
// create a new thing
my_thing = {};

// keys following the naming rules can be created and accessed using the `.key` syntax
my_thing.color = 'blueish';

// Functions like `get` and `set` can also be used to create and read properties,
// and just as the bracket [..] notation they can be used to use keys which do not
// follow the naming convention, for example a key with spaces:
my_thing['with some spaces'] = 'almost any str is possible as key';

 // my_thing does not have an Id as we are using it as a variable
assert (my_thing.id() == nil);

// attach to the collection will generate an Id
.my_thing = my_thing;
assert (my_thing.id() != nil);
```

Properties can be set immediately at initialization. Its quite common to wite a query with query params where the query param is used as key/value pairs in a thing. In this case it is possible to use a short syntax.

```thingsdb
// this query is called with name='...'
// In this case writing "name: name," is not required and a "short" syntax can be used
my_thing = {
    name:,
    other: 'another key/value pair'
};
```
