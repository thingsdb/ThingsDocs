---
title: "typed"
weight: 162
---


A *typed* thing is a thing with pre-defined properties and/or methods with are defined by a *[Type](../../overview/type)*.
When creating a *typed* thing, all defined properties of the *[Type](../../overview/type)* are guaranteed to exist with a value matching the type definition.

Most, but not all, functions of a *thing* work on *typed things* as well. Next to the functions below, a *typed thing* may have [additional methods](../../overview/type/#methods) which are defined by the [Type](../../overview/type).


### Functions

Function | Description
------ | -----------
[assign](../thing/assign) | Copies properties from a typed thing.
[copy](../thing/copy) | Copy a typed thing as a new [thing](../thing). The Type is *not* preserved.
[dup](../thing/dup) | Duplicate a typed thing while preserving the Type.
[each](../thing/each) | Iterate over all properties of a typed thing.
[equals](../thing/equals) | Test if two things are equal.
[filter](../thing/filter) | Return a new [thing](../thing) with properties that pass a given test.
[get](../thing/get) | Return the value of a property on a typed thing by a given property name.
[has](../thing/has) | Determine if a typed thing has a given property.
[id](../thing/id) | Return `id` of the typed thing or `nil` when the typed thing is not stored.
[keys](../thing/keys) | Return a list with all the property names of a typed thing.
[len](../thing/len) | Return the number of items.
[map](../thing/map) | Return a [list](../list) with the results of calling a provided closure on every property.
[set](../thing/set) | Set a property of a typed thing to a new value.
[values](../thing/values) | Return a list with all the property values of a typed thing.
[wrap](../thing/wrap) | Wrap the *typed* thing with a [Type](../../overview/type).

{{% notice info %}}
The above functions correspond to those of a `thing`. For that reason, they are only listed under the data type `thing`.
{{% /notice %}}