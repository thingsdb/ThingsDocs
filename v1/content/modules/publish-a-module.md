---
title: "Publish a module"
weight: 347
---

Modules can be published using a [GitHub](https://github.com) repository. A module repository mush at least contain a `module.json` file and the module file to start.

## module.json

> Example of a `module.json`:

```json
{
    "doc": "Demo module",
    "version": 11,
    "main": "demo.py",
    "defaults": {
        "load": true,
        "deep": 0
    },
    "exposes": {
        "ping": {
            "defaults": {
                "message": "ping"
            },
            "argmap": []
        },
        "msg": {
            "argmap": ["message"]
        }
    },
    "requirements": [
        "py-timod"
    ]
}
```

### Key: `doc` *(optional)*

Type `string` or `null`.

Should contain a description for the module or a link to the module documentation. If omitted or `null`, no documentation will be available. The documentation can be viewed with `module_info(<name>).load().doc;`

### Key: `version` *(required)*

Type `string` or `number`.

A string must by in the format of digits separated by dots.
Examples of valid versions: `"0.1.0"`, `"2.0"`, `"42"`, or just numbers like `1`, `3.2`.

> Note: when a number is used, the number will be converted to a string in ThingsDB.

### Key: `main` *(required)*

Type `string` or `map`.

Path to the *main* file for the module. This should be either a binary file or a Python file (ending in`.py`). When using a Python file, this module will automatically be marked as a Python module and started using the Python interpreter.

Instead of a `string` with a singe file, it is also possible to use an platform/architecture mapping for pointing to the correct binary.
The key should consist of the platform and architecture combined with a slash (`/`). You can view which platform and architecture your ThingsDB node(s) are running on by using the following command in the `@node` scope:

```javascript
x = node_info().load(); `{x.platform}/{x.architecture}`;
```

Example of a `main` key with some common platform/architecture mappings:

```json
    "main": {
        "linux/386": "bin/demo_linux_386.bin",
        "linux/amd64": "bin/demo_linux_amd64.bin",
        "linux/arm": "bin/demo_linux_arm.bin",
        "linux/arm64": "bin/demo_linux_arm64.bin",
        "freebsd/386": "bin/demo_freebsd_386.bin",
        "freebsd/amd64": "bin/demo_freebsd_amd64.bin",
        "freebsd/arm": "bin/demo_freebsd_arm.bin",
        "freebsd/arm64": "bin/demo_freebsd_arm64.bin",
        "darwin/amd64": "bin/demo_darwin_amd64.bin"
    }
```

> Note that we placed the binaries in a **bin** folder. This is important as large files should be in either in a **bin/**, **blob/** or **blobs/** folder in the root of the repository.

### Key: `defaults` *(optional)*

Type `map`.

It is possible to provide some global defaults for this module. All the *defaults* which are configured at the root of the module will be used by all *exposed* functions and also when the module is used directly. It is possible to overwrite defaults with an exposed function and defaults may also be overruled when using the module.

Example defaults:

```json
    "defaults": {
        "load": true,
        "deep": 0
    }
```

### Key: `includes` *(optional)*

Type `array` with `string` and/or `map` items.

Each file in the `includes` array will be copied to the module folder. If files depend on a platform/architecture, a map might be used to copy only the applicable file(s). Like with *main*, large files should be placed in either a `bin/`, `blob/` or `blobs/` folder.

### Key: `exposes` *(optional)*

Type `map` with a *doc*, *defaults* and/or *argmap* key. All keys are optional.

Expose functions to ThingsDB which might be easy to use. An exposed function may have some default values and may also map positional arguments to key/value pairs. The latter can be done by using the optional `argmap` key.

The following keys can be used in an exposed function map:

- `doc` *(optional)*: Documentation or link to documentation of the exposed function.
- `defaults` *(optional)*: Defaults for this exposed function. Global defaults will be inherited but may be overwritten here.
- `argmap` *(optional)*: Map positional arguments to key/value pairs.

For example: suppose we have a module `demo` which requires a `message` argument. To use this module we would have to call the module like this:

```javascript
demo({message: "my beautiful message"});
```

Instead, we could expose a `msg` function and map the first argument to the `message` key.

```json
    "exposes": {
        "msg": {
            "argmap": ["message"]
        }
    }
```

Now, we can write the following in ThingsDB:

```javascript
demo.msg("my beautiful message");
```

In combination with `defaults` it is possible to expose some nice and handy functions to ThingsDB. It is also possible to combine positional arguments with a (optional) *thing* as properties. This can be done with the special `"*"`.  For example:

```json
{
    "argmap": ["message", "*"]
}
```

The above will first capture the `"message"` as first argument, and accepts a second argument which must be `nil` or a `thing`.

### Key: `requirements` *(optional)*

Type `array` of `strings`.

The requirements key can only be used in combination with Python modules. If omitted, a Python module will automatically look for a `requirements.txt` file in the root of your repository. If you do not want ThingsDB to perform that action, you may provide the requirements key with an empty array. ` "requirements": []`. Each requirement should be formatted like `pip` is you expecting to, for example `py-timod >= 0.0.6` is a valid requirement.





