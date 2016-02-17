# Sandstorm TCP Listener Proxy

This command line tool allows [Sandstorm](http://sandstorm.io/) apps to expose a listening TCP socket outside of Sandstorm's sandbox. This is meant for non-HTTP protocols, such as an IRC bouncer or a game server. UDP is not supported by this tool (although it may be in the near future).

## Building

Run `make`. You must have Sandstorm and [Cap'n Proto](https://capnproto.org/) installed on your system, as well as Clang 3.6 or newer.

## Using

You are meant to use this as a command line tool that your main web server calls out to. Run `make` as part of your build process and copy/use the binary from `bin/sandstorm-tcp-listener-proxy`. Here is its usage statement reproduced:

```
Usage: ./bin/sandstorm-tcp-listener-proxy [<option>...] <token> <localPort> <externalPort>

Runs a TCP listener proxy for bridging IpInterface to convential TCP listening
applications.

Options:
    --verbose
        Log informational messages to stderr; useful for debugging.
    --version
        Print version information and exit.
    --help
        Display this help text and exit.
```

`token`: This is the raw token that you get from requesting an ipInterface.

`localPort`: The port that the local service inside the sandbox is listening on.

`externalPort`: The external port outside of the sandbox you wish to be world reachable.
