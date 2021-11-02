---
title: "Hello World Module"
weight: 321
---

In this section we will create and use a module to help you understand how a module can be used.
Our module will be written in Python and will accept a *name* and returns with a greeting in either English or Dutch, depending on the module configuration.

Before we can use a Python module, make sure ThingsDB has a Python interpreter (*at least Python 3.7)* with the Python package [py-timod](https://pypi.org/project/py-timod/) installed.

Use the following code in the `@node` scope to view which Python interpreter ThingsDB is using:

```thingsdb,should_pass,@n
node_info().load().python_interpreter;  // something like "/usr/bin/python"
```

If you are able to open a terminal on the host where ThingsDB is running, you can check if `py-timod` is installed by staring the Python interpreter and import `timod`.

```bash
$ /usr/bin/python
Python 3.8.5 (default, May 27 2021, 13:30:53)
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import timod
>>> timod.__version__
'0.0.6'
>>>
```

If this is all set-up, we can create, deploy and test the module!

The rest of the ThingsDB code in this tutorial code must run in the `@thingsdb` scope!

```thingsdb,should_pass,@t
new_module("greeting", "greeting.py");  // The module file must end with .py to tell
                                        // ThingsDB we are going to use a Python module.
```

Hooray, the module is created!! ..but wait.. we don't have the actual module yet. If we look at the module status, we should see that the module will not be started because obviously, the greeting.py file is missing.

```thingsdb,should_pass,@t
module_info('greeting').load().status;  // "no such file or directory"
```

Ok, let's first create the required Python code. A basic module looks like the following:

```python
from timod import start_module, TiHandler


class Handler(TiHandler):

    async def on_config(self, cfg):
        pass

    async def on_request(self, req):
        pass


if __name__ == '__main__':
    start_module('greeting', Handler())
```

This code contains a handler with two methods. The `on_config(..)` method will be called when ThingsDB starts a module and when the config is changed using the [set_module_conf](../../thingsdb-api/set_module_conf) function. The `on_request(..)` method will be called from a [future](../../data-types/future/#modules). A [future](../../data-types/future/#modules) is required to use the module.

The Python method `start_module` is used to start the module and accepts a *name* which we changed to `greeting` and an instance of a `TiHandler` class, just `Handler()` in our case.

{{% notice note %}}
As mentioned earlier, a module usually keeps running as long as ThingsDB is alive and may accept multiple request in parallel. Therefore, it is important to write code in both the `on_config` and `on_request` in a **non-blocking** way.
{{% /notice %}}


We want our module to support both English and Dutch and therefore we are going to create a configuration function which accepts a language. We also use the `__init__()` function to initialize a default language.

```python
from timod import LookupError, ValueError
...
    def __init__(self):
        self.lang = 'en'  # set a default language

    async def on_config(self, cfg):
        try:
            lang = cfg['lang']
        except KeyError:
            raise LookupError('`lang` is missing')

        if lang not in ['nl', 'en']:
            raise ValueError('only `nl` and `en` are supported')

        self.lang = lang
```

Next, we write the `on_request` method:

```python
    async def on_request(self, req):
        try:
            name = cfg['name']
        except KeyError:
            raise LookupError('`name` is missing')

        return {
            'en': 'Hello {}, enjoy this day!!'.format(name),
            'nl': 'Hallo {}, geniet van deze dag!!'.format(name)
        }[self.lang]
```

Our module is finished!

Now we are going to deploy the code and we are going to use the [deploy_module()](../../thingsdb-api/deploy_module) function for this job.

The [deploy_module()](../../thingsdb-api/deploy_module) function accepts a module name and data. It writes the data *(or code)* to the attached file of the module and then (re-)loads the module on all the nodes.
In our case, we keep it simple and just paste the code in a query as a plain string. When developing a real module you probably want to upload the file using a query argument.

```thingsdb,should_pass,@t
// Deploy the module code
deploy_module('greeting',
"from timod import start_module, TiHandler, LookupError, ValueError


class Handler(TiHandler):

    def __init__(self):
        self.lang = 'en'  # set a default language

    async def on_config(self, cfg):
        try:
            lang = cfg['lang']
        except KeyError:
            raise LookupError('`lang` is missing')

        if lang not in ['nl', 'en']:
            raise ValueError('only `nl` and `en` are supported')

        self.lang = lang

    async def on_request(self, req):
        try:
            name = req['name']
        except KeyError:
            raise LookupError('`name` is missing')

        return {
            'en': 'Hello {}, enjoy this day!!'.format(name),
            'nl': 'Hallo {}, geniet van deze dag!!'.format(name)
        }[self.lang]


if __name__ == '__main__':
    start_module('greeting', Handler())
");
```

If everything is successful, the module status should now be changed to "running":

```thingsdb,should_pass,@t
module_info('greeting').load().status;  // "running"
```

Ok, now let's try to use the module:

```thingsdb,syntax_only,@t
future({
    module: 'greeting',
    name: 'Arthur Dent'
}).then(|greet| greet);  // "Hello Arthur Dent, enjoy this day!!"
```

Or, when we configure the module language to `nl` (dutch):

```thingsdb,syntax_only,@t
// Configure the module to use Dutch (nl)
set_module_conf('greeting', {lang: 'nl'});

// The greet should now be in Dutch
future({
    module: 'greeting',
    name: 'Arthur Dent'
}).then(|greet| greet);  // "Hallo Arthur Dent, geniet van deze dag!!"
```
