---
title: "Java"
weight: 16
---

### Installation

For Maven users:

```
io.github.thingsdb thingsdb 1.0.0
```

### Quick usage

```java
import io.github.thingsdb.connector.Connector;
import io.github.thingsdb.connector.Result;
import io.github.thingsdb.connector.Vars;

...

Connector client = new Connector("localhost");  // or "hostname" and port
client
    .setDefaultScope("//stuff")     // change the default scope
    .connect()                      // connect to ThingsDB
    .authenticate("admin", "pass")  // token.. or username, password
    .get();                         // wait for the future to complete


// Example query
Vars vars = new Vars();
vars.setInt("a", 6);
vars.setInt("b", 7);
Result res = client.query("a * b;", vars).get();

assertEquals(res.unpackInt(), 42);
```

### More info

- https://github.com/thingsdb/java-thingsdb/#readme
- https://central.sonatype.com/artifact/io.github.thingsdb/thingsdb