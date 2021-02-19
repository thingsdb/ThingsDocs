---
title: "new_collection"
weight: 256
---

Create a new collection.

This function generates an [event](../../overview/events).

### Function

`new_collection(name)`

### Arguments

Argument | Type | Description
--------- | ----------- | -----------
name | str (required) | Name of the new collection.

{{% notice note %}}
The user who has created the collection will automatically receive full
access rights to the new collection.
Use `grant` to give other users access to the collection.
{{% /notice %}}

### Return value

Returns the new collection `id` if successful. A [lookup_err()](../../errors/lookup_err) is raised
if the collection already exists.

### Example

> This code will create a collection *"awesome_things"*:

```thingsdb,should_pass,@t
// Creates a new collection
new_collection('awesome_things');
```

> Example return value in JSON format (the new collection id)

```json
31415
```
