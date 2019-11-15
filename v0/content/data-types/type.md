---
title: "Type"
date: 2019-10-23T16:43:16+02:00
weight: 1500
---


It is possible to create a type in ThingsDB which can


definition | description
---------- | -----------
`'str'` | requires type [str](../str) and the value *should* contain valid UTF-8 characters.
`'utf8'` | requires type [str](../str) and the value is *must* be valid UTF-8.
`'raw'` | requires type [str](../str) *or* [bytes](../bytes).
`'bytes'` | requires type [bytes](../bytes).
`'int'` | requires type [int](../int).
`'uint'` | requires a *non-negative* type [int](../int).
`'[]'` | requires a [list](../list).
`'{}'` | requires a [set](../set).
`'any'` | any type is valid.

