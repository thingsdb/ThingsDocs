## find

This function returns the value of the first element in the array or thing that satisfies the callback function.
Otherwise `nil` is returned.

This function does *not* generate an [event](#events).

### Function
*iterable*.`find(callback)`

### Arguments

Explanation of the *callback* argument:

Iterable | Callback | Description
-------- | -------- | -----------
array | item, index => ... | Iterate over items in the array. Both item and index are optional.
thing | name, value => ... | Iterate over thing properties. Both name and value are optional.

### Return value
The value of the first element in the array or thing that satisfies the provided testing function;
otherwise, `nil` is returned.
