---
title: "emit"
weight: 109
---

Emit an event to all watchers of a [thing](..).
The event is a string value which you are free to choose. It is possible, but not required, to send extra arguments with the event.

{{% notice note %}}
When you emit an event, the event is handled by ThingsDB just as any other event and thus the order in which they are send
to the client is guaranteed.
{{% /notice %}}

This function generates an [event](../../../overview/events).


Using events enables a user to write code like this example of a ChatRoom in the Python language:

```python
import asyncio
from thingsdb.model import Emitter
from thingsdb.util import event
from thingsdb.client import Client

class ChatRoom(Emitter):

    @event('new-message')
    def on_new_message(self, msg):
        pass  # do something with the message

client = Client()

loop = asyncio.get_event_loop()
loop.run_until_complete(client.connect('localhost'))
loop.run_until_complete(client.authenticate('admin', 'pass'))

chat = ChatRoom(
    client,                     # ThingsDB Client() instance
    emitter='',                 # The 'thing' to watch. Defaults to the
                                # collection root by using an empty string.
    scope='//stuff')            # Collection Scope, defaults the the default
                                # scope of the client.

loop.run_forever()
```

### Function

*thing*.`emit([deep], event, ...)`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
deep | int (optional) | Specify how [deep](../../../collection-api/return/#deep) the arguments must be send with the event. (defaults to `1`)
event | str (required) | Event name to emit.
... | any (optional) | Arguments send together with the event.


### Return value

None

### Example

> This code shows an example using ***emit()***:

```thingsdb,json_response
.emit('new-message', 'Hello Everyone!');
```

> Return value in JSON format

```json
null
```
