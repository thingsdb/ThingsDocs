---
title: "Go"
weight: 6
---

### Installation

Simple install the package to your [$GOPATH](https://github.com/golang/go/wiki/GOPATH) with the [go tool](https://golang.org/cmd/go/) from shell:

```shell
$ go get github.com/thingsdb/go-thingsdb
```

Make sure [Git](https://git-scm.com/downloads) is installed on your machine and in your system's PATH.


### Quick usage

```go
package main

import (
	"crypto/tls"
	"fmt"

	thingsdb "github.com/thingsdb/go-thingsdb"
)

func example(conn *thingsdb.Conn, res chan interface{}) {
	var data interface{}
	var err error

	if err := conn.Connect(); err != nil {
		res <- err
		return
	}

	defer conn.Close()

	if err := conn.AuthToken("Fai6NmH7QYxA6WLYPdtgcy"); err != nil {
		res <- err
		return
	}

	if data, err = conn.Query(
		"//Doc",                // Scope
		".greetings.choice();", // ThingsDB code
		nil, // Optional array with variable (may be `nil`)
		120, // Timeout in seconds
	); err != nil {
		res <- err
		return
	}

	res <- data
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

	// Set-up a log channel, this is not required
	conn.LogCh = make(chan string)

	// Start our example
	go example(conn, res)

	// Log handler
	go func() {
		for {
			msg := <-conn.LogCh
			fmt.Printf("Log: %s\n", msg)
		}
	}()

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
