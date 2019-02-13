## thing (function)

This function can be used to get a thing or things by id.

This function does *not* generate an [event](#events).

### Function
`thing(id1, id2, ..., idX)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
id1, id2, ..., idX | int (at least one required) | The thing(s) to return.

### Return value
Returns a [thing ](#thing) or an *array-of-things* based on given id's.
An `INDEX_ERROR` is returned in case at least one id is not found inside the collection.

<aside class="notice">
You can force an <i>array-of-things</i>, even with only one id. Just add an extra comma,
for example: <code>thing(666,);</code> and this will return an array with one thing: <code>[{"#": 666, ...}]</code>
</aside>
