---
title: "warning"
weight: 250
---

ThingsDB might send a warning events to a client. The `warn_code` can be used
to determine the warning type.

ThingsDB might push one of the following waning codes:

Code | Description
---- | -----------
`1` | This warning is pushed after attempting to *watch* a thing which does not exist in the collection.

> Example *warning* event in JSON format:

```json
{
    "warn_code": 1,
    "warn_msg": "failed to watch thing ..."
}
```
