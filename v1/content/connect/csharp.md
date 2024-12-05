---
title: "C#"
weight: 14
---

### Installation

{{% notice note %}}
The **ThingsDB.Connector** library requires **.NET8**.
{{% /notice %}}


This library is distributed via NuGet.

Using a package manager:
```
Install-Package ThingsDB.Connector
```

Or, by using NET CLI:
```
dotnet add package ThingsDB.Connector
```

### Quick usage

```csharp
using System;
using ThingsDB;

namespace HelloWorld
{
    class Program
    {
        static async Task Example()
        {
            // replace `localhost` with your ThingsDB server address and optionally
            // provide a port and enable TLS/SSL. (see documentation)
            Connector conn = new("localhost");

            // replace 'admin' and 'pass' with your username and password or a valid token
            await conn.Connect("admin", "pass");

            // perform a query; the documentation shows more examples
            var response = await conn.Query(@"//ti
                'Hello World!';
            ");

            // unpack and return the result
            var result = Unpack.Deserialize<string>(response);

            // write the result to the console output
            Console.WriteLine(result);

            // close the connection when finished
            conn.Close();
        }
        static void Main(string[] args)
        {
            // async code so we use a Task
            Task.Run(() => Example()).Wait();
        }
    }
}
```

### More info

A more complete description of the C# connector can be found in one of the links below.

- https://github.com/thingsdb/ThingsDB-CSharp#readme
- https://www.nuget.org/packages/ThingsDB.Connector
