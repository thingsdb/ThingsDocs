## map

Iterate over items in an [array](#array) or over all properties on a [thing](#thing).

This function does *not* generate an [event](#events).

### Function
*iterable*.`map(callback)`

### Arguments

Explanation of the *callback* argument:

Iterable | Callback | Description
-------- | -------- | -----------
array | item, index => ... | Iterate over all items in the array. Both item and index are optional.
thing | name, value => ... | Iterate over the thing properties. Both name and value are optional.

### Return value
A new array with each element being the result of the callback function.
