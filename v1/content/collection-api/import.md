---
title: "import"
weight: 221
---

This function can be used to import a collection which was exported using the [export(..)](../import) function with the option `dump` enabled.

{{% notice warning %}}
This method can only be used in an empty collection.
{{% /notice %}}

This function generates a [change](../../overview/changes).

### Function

`import(data, [options])`

### Arguments

Argument  | Type             | Description
--------- | ---------------- | -----------
`data`    | bytes (required) | The data to import.
`options` | thing (optional) | A thing with optional [options](#options).

#### Options

Option | Type | Description
------ | ---- | -----------
`import_tasks` | bool | When `true`, tasks will be imported as well and the owner will be set to the user performing the import. If `false` *(default)*, tasks are not imported and each existing task will be set to an empty task.

### Return value

Returns `nil` when successful.

### Example

We provide two examples, one using the [thingsdb-prompt](https://github.com/thingsdb/ThingsPrompt) and another using Python code.

{{% notice note %}}
In the examples below we use the default credentials and assume ThingsDB is running on localhost and a collection "stuff" exists. This might be different on your set-up so be sure to not simple copy/paste the examples.
{{% /notice %}}

#### ThingsDB prompt

```bash
# Export the "stuff" collection to a filename
things-prompt -u admin -p pass -s //stuff export /tmp/dump.mp

# Import the file into a new collection "clone"
# ThingsDB prompt will automatically create the collection if it does not exist
things-prompt -u admin -p pass -s //clone import /tmp/dump.mp
```

#### Python code

```python
import asyncio
from thingsdb.client import Client

async def export_and_import():
    client = Client()
    await client.connect('localhost')

    try:
        await client.authenticate('admin', 'pass')

        # export the "stuff" collection
        dump = await client.query("""//ti
            export({dump: true});
        """, scope='//stuff')

        # create a new collection called "clone"
        await client.query("""//ti
            new_collection('clone');
        """, scope='/s')

        # import the dump into the new "clone" collection
        await client.query("""//ti
            import(dump, {import_tasks: true});
        """, dump=dump, scope='//clone')

    finally:
        client.close()
        await client.wait_closed()

asyncio.run(export_and_import())
```