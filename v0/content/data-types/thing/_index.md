---
title: "thing"
weight: 113
---

### Functions

Function | Description
------ | -----------
[assign](./assign) | Copies properties from a thing.
[copy](./copy) | Copy a thing to a new thing. A Type is *not* preserved.
[del](./del) | Remove a property.
[dup](./dup) | Duplicate a thing while preserving the Type.
[each](./each) | Iterate over all properties of a thing.
[emit](./emit) | Emit an event to all watchers of a thing.
[equals](./equals) | Test if two things are equal.
[filter](./filter) | Return a new `thing` with properties that pass a given test.
[get](./get) | Return the value of a property on a thing by a given property name.
[has](./has) | Determine if a thing has a given property.
[id](./id) | Return the `id`.
[keys](./keys) | Return a list with all the property names of a thing.
[len](./len) | Return the number of items.
[map](./map) | Return a [list](../list) with the results of calling a provided closure on every property.
[set](./set) | Create a new property on a thing.
[unwatch](./unwatch) | Stop watching the `thing` for mutations.
[values](./values) | Return a list with all the property values of a thing.
[watch](./watch) | Watch the `thing` for mutations.
[wrap](./wrap) | Wrap the `thing` with a [Type](../type).
