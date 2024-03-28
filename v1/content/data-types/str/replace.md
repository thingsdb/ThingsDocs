---
title: "replace"
weight: 135
---

Return a new [string](..) in which in which the occurrences of *old* have been replaced with *new*. Instead of an *old* string it is also possible to use a regular expression and the *new* string may also be a closure which then in turn should return a new string to replace the *old* part with.

Optionally, the *number* of replacements can be restricted and may start from either left or right *(Unless a regular expression is used, in which case the number of replacements can only be restricted from the left)*.


This function does *not* generate a [change](../../../overview/changes).

### Function

*str*.`replace(old, new, [number])`

### Arguments

Argument | Type | Description
-------- | ---- | -----------
old | str/regex (required) | The old substring to replace, or a regular expression to search for matches.
new | str/closure (required) | String which will replace the *old* substring. If a closure is used, the return value of the closure will be used to replace the *old* substring with (see [closure arguments](#closure-arguments)).
number | int (optional) | Maximum number of replacements. If not given, all occurrences of the *old* substring will be replaced. If *negative*, replacement starts at the end of the string *(a negative replacement is only possible when `old` is of type `str`)*.

### Closure Arguments

This are the arguments which are given when a closure is used for *new* instead of a plain string:

Argument | Description
----- | -----------
groups `0..X` | The first arguments are all the capture groups. *(Only when `old` is a regular expression)*
full match | After the capture groups, the next argument will be the full match. *(Only when `old` is a regular expression)*
start position | Start position of the match in the original string.
end position | End position of the match in the original string.
original string | The original string. The full match thus is `original[start:end]`.


### Return value

Returns a new string with all occurrences of *old* have been replaced with *new*, optionally limited by a maximum *number* of replacements.

### Example

> Example using ***replace()***:

```thingsdb,json_response
[
    {
        // Replace all occurrences of `blue` with `black`
        'My favorite color is blue and I have a blue bicycle.'.replace('blue', 'black');
    },
    {
        // Replace the first occurrence of `white` with `black`
        'My favorite color is white and I have a white car.'.replace('white', 'black', 1);
    },
    {
        // Replace the last occurrence of `red` with `black`
        'My favorite color is red and I have a red mountainbike.'.replace('red', 'black', -1);
    }
]
```

> Return value in JSON format

```json
[
    "My favorite color is black and I have a black bicycle.",
    "My favorite color is black and I have a white car.",
    "My favorite color is red and I have a black mountainbike."
]
```

> Example using ***replace()*** with a **regular expression**:

```thingsdb,json_response
s = 'Iris is 8 years old, has 3 bikes and about 25 books';
s.replace(/\d+/, |m| str(int(m)+1));
```

> Return value in JSON format

```json
"Iris is 9 years old, has 4 bikes and about 26 books"
```

> Example using ***replace()*** with a **regular expression** and **capture groups**:

```thingsdb,json_response
s = 'This is an _example_!!';
s.replace(/_(\w*)_/, |a| `<strong>{a}</strong>`);
```

> Return value in JSON format

```json
"This is an <strong>example</strong>!!"
```