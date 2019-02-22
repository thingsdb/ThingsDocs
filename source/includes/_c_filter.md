## filter

This function does *not* generate an [event](#events).

### Function
*iterable*.`filter(callback)`

### Arguments
Explanation of the *callback* argument:

Iterable | Callback | Description
-------- | -------- | -----------
array | item, index => ... | Iterate over all items in the array. Both item and index are optional.
thing | name, value => ... | Iterate over the thing properties. Both name and value are optional.


### Return value
A new array or thing with the elements that pass the test.
If no elements pass the test, an empty array or thing will be returned.
