---
title: "error"
date: 2019-10-14T09:41:45+02:00
weight: 4
---

When an error occurs within a method, an object can be returned. The object, called an error, contains information about the error, including its type and a message.

### Methods

Method | Description
------ | -----------
[len](./len) | Returns the length of the error message.

### Related functions

Method | Description
------ | -----------
[err](../../collection-api/err) | Initialize a new error.
[raise](../../collection-api/raise) | Raise an error.
[try](../../collection-api/try) | Try a statement and catch if an error is raised.


### Build-in errors
See [errors](../../errors) for a list of all the build-in error type.