---
title: "warning"
weight: 357
---

ThingsDB might send a warning events to a client. The `warn_code` can be used
to determine the warning type.

ThingsDB might push one of the following waning codes:

Code | Description
---- | -----------
`2`  | Message from the [log()](../../collection-api/log) function.

> Example *warning* event in JSON format:

```json
{
    "warn_code": 2,
    "warn_msg": "Test.., one, two, three"
}
```
