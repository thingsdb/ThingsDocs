---
title: "all"
weight: 261
---

Run a given callback on all the instances of a given Type.

{{% notice note %}}
This function should be used for migration purposes and *not* for common queries as the function is rather slow.
When calling this action, ThingsDB requires to loop over all the things in the collection, including the things which are marked for garbage collection.
{{% /notice %}}

### Action

`mod_type(type, 'all', callback)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
type | str | Name of the Type to iterate over.
`'all'` | str | Passing this argument will result in a *iterate-all* action.
callback | closure | The closure will be called on each instance.

### Return value

The value `nil`.

### Example

> This code shows the return value for the action ***all***:

```thingsdb,json_response
// Create type `Player`
set_type('Player', {
    score: 'int',
});

// Create a player with score "10"
player = Player{score: 10};

// Update all the current scores times 10
mod_type('Player', 'all', |p| p.score *= 10);

player;
```

> Return value in JSON format

```json
{
    "score": 100
}
```
