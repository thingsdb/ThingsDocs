---
title: "warning"
weight: 313
---

ThingsDB might send a warning events to a client. The `warn_code` can be used
to determine the warning type.

ThingsDB might push one of the following waning codes:

Code | Description
---- | -----------
`X` | Currently, ThingsDB does not have any known warning codes.

> Example *warning* event in JSON format:

```json
{
    "warn_code": 1,
    "warn_msg": "function XXX is deprecated..."
}
```
