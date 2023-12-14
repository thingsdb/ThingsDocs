---
title: "emit"
weight: 108
---


Emit an *event* to all clients which have joined this [room](..).
The event is a string value which you are free to choose. It is possible, but not required, to send extra arguments with the event.

This function does *not* generate a [change](../../../overview/changes).

Using events enables a user to write code like this example of a ChatRoom in the Python language:

```python
import asyncio
from thingsdb.util import event, Room
from thingsdb.client import Client

class ChatRoom(Room):

    @event('new-message')
    def on_new_message(self, msg):
        pass  # do something with the message

client = Client()

loop = asyncio.get_event_loop()
loop.run_until_complete(client.connect('localhost'))
loop.run_until_complete(client.authenticate('admin', 'pass'))

chat = ChatRoom(
    client,                     # ThingsDB Client() instance
    room='.chat.id();',         # The 'room' to join. This might be an Id or
                                # code to find the id.
    scope='//stuff')            # Collection Scope, defaults the the default
                                # scope of the client.

loop.run_forever()
```

### Function

*room*.`emit([deep [, flags]], event, ...)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
deep | int (optional) | Specify how [deep](../../../collection-api/return/#deep) the arguments must be send with the event. (defaults to the current *deep* value)
flags | int (optional) | Specify which flags to use; see [return-flags](../../../overview/statements/#return-flags)
event | str (required) | Event name to emit. *(name must have at least 1 and at most 255 characters)*
... | any (optional) | Arguments send together with the event.


### Return value

None

### Example

> This code shows an example using ***emit()***:

```thingsdb,json_response
.chat = room();
.chat.emit('new-message', 'Hello Everyone!');
```

> Return value in JSON format

```json
null
```
