---
title: "Go"
weight: 10
---

### Installation

Simple install the package to your [$GOPATH](https://github.com/golang/go/wiki/GOPATH) with the [go tool](https://golang.org/cmd/go/) from shell:

```shell
$ go get github.com/thingsdb/go-thingsdb
```

Make sure [Git](https://git-scm.com/downloads) is installed on your machine and in your system's PATH.

### Quick usage

> Note: This example requires at lease **version 1.0.0** of the go-thingsdb connector.

```go
package main

import (
    "crypto/tls"
    "fmt"

    thingsdb "github.com/thingsdb/go-thingsdb"
)

func example(conn *thingsdb.Conn, res chan interface{}) {
    if err := conn.Connect(); err != nil {
        res <- err
        return
    }

	// Close the connection at the end of this function
    defer conn.Close()

	if err := conn.AuthToken("Fai6NmH7QYxA6WLYPdtgcy"); err != nil {
		res <- err
		return
	}

	data, err := conn.Query(
		"//Doc",                // Scope
		".greetings.choice();", // ThingsDB code
		nil,                    // Arguments, may be a map[string]interface{}
	);

	if err == nil {
		res <- data
	} else {
		res <- err
	}
}

func main() {
	// Only required for a secure connection
	conf := &tls.Config{
		InsecureSkipVerify: false,
	}

	// In this example we will use a channel to read the example response
	res := make(chan interface{})

	// Create a new ThingsDB connection
	conn := thingsdb.NewConn("playground.thingsdb.net", 9400, conf)

	// Start our example
	go example(conn, res)

	// Wait for the response
	data := <-res

	// Print the response (or error)
	fmt.Printf("%v\n", data)
}
```

> Possible response

```bash
Log: connected to playground.thingsdb.net:9400 using a secure connection
Welcome at ThingsDB!
```

### More info

A more complete description of the Go client can be found in the link below.

- https://github.com/thingsdb/go-thingsdb#readme
