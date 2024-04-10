---
title: "backups_ok"
weight: 324
---

Returns `false` if at least one backup had failed _(result code != 0)_.
In all other cases this function returns `true` _(also when no backups are available or not yet started)_.

This function does *not* generate a [change](../../overview/changes).

### Function

`backups_ok()`

### Arguments

None

### Return value

Returns `false` if at least one backup has failed, otherwise this function returns `true`.
