---
title: "is..."
weight: 224
---

There are many functions in ThingsDB to check if a value is compatible with some specification.
All the these build-in check functions return with either `true` or `false` and none of the _is_ functions generate a [change](../../overview/changes).

### Is functions

Function                        | Description
------------------------------- | -----------
[is_array](./is_array)          | Determines whether the provided value is of type [list](../../data-types/list) or [tuple](../../data-types/tuple).
[is_ascii](./is_ascii)          | Determines whether the provided value is of type [str](../../data-types/str) and contains only valid ascii characters.
[is_bool](./is_bool)            | Determines whether the provided value is a [bool](../../data-types/bool) or not.
[is_bytes](./is_bytes)          | Determines whether the provided value is of type [bytes](../../data-types/bytes) or not.
[is_closure](./is_closure)      | Determines whether the provided value is a [closure](../../data-types/closure) or not.
[is_datetime](./is_datetime)    | Determines whether the provided value is of type [datetime](../../data-types/datetime) or not.
[is_email](./is_email)          | Determines whether the provided value is of type [str](../../data-types/str) and contains an email address.
[is_enum](./is_enum)            | Determines whether the provided value is an [enumeration type](../../data-types/enum) member or not.
[is_err](./is_err)              | Determines whether the provided value is a [error](../../data-types/error) or not.
[is_float](./is_float)          | Determines whether the provided value is a [floating point](../../data-types/float) value or not.
[is_future](./is_future)        | Determines whether the provided value is a [future](../../data-types/future) value or not.
[is_module](./is_module)        | Determines whether the provided value is a [module](../../modules) value or not.
[is_inf](./is_inf)              | Determines whether the provided value is a positive or negative *infinity*.
[is_int](./is_int)              | Determines whether the provided value is an [integer](../../data-types/int) or not.
[is_list](./is_list)            | Determines whether the provided value is a [list](../../data-types/list) or not.
[is_mpdata](./is_mpdata)        | Determines whether the provided value is of type [mpdata](../../data-types/) or not.
[is_nan](./is_nan)              | Determines whether the provided value is not a number.
[is_nil](./is_nil)              | Determines whether the provided value is [nil](../../data-types/nil).
[is_raw](./is_raw)              | Determines whether the provided value is of type [str](../../data-types/str) *or* [bytes](../../data-types/bytes).
[is_regex](./is_regex)          | Determines whether the provided value is of type [regex](../../data-types/regex) or not.
[is_room](./is_room)            | Determines whether the provided value is a [room](../../data-types/room) or not.
[is_set](./is_set)              | Determines whether the provided value is a [set](../../data-types/set) or not.
[is_str](./is_str)              | Determines whether the provided value is of type [str](../../data-types/str).
[is_task](./is_task)            | Determines whether the provided value is a [task](../../data-types/task) or not.
[is_tel](./is_tel)              | Determines whether the provided value is of type [str](../../data-types/str) and contains a telephone number.
[is_thing](./is_thing)          | Determines whether the provided value is a [thing](../../data-types/thing) or not.
[is_time_zone](./is_time_zone)  | Determines whether the provided value is of type [str](../../data-types/str) and contains a valid time zone.
[is_timeval](./is_timeval)      | Determines whether the provided value is of type [timeval](../../data-types/timeval).
[is_tuple](./is_tuple)          | Determines whether the provided value is a [tuple](../../data-types/tuple) or not.
[is_url](./is_url)              | Determines whether the provided value is of type [str](../../data-types/str) and contains a URL.
[is_utf8](./is_utf8)            | Determines whether the provided value is of type [str](../../data-types/str) and contains valid UTF-8 characters.