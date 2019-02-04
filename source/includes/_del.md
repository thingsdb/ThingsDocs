## del

This function generates an [event](#events).

### Function
*thing*.`del(property)`

### Arguments
Argument | Type | Description
-------- | ---- | -----------
property | raw (required) | Name of the property to delete.

### Return value
Returns `nil` if successful. An `INDEX_ERROR` is returned
if the property does not exist or `BAD_REQUEST` in case the given property is
not a valid [name](#names).
