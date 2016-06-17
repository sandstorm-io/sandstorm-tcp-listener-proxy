# You may override the following vars on the command line to suit
# your config.
CXX=clang++
CXXFLAGS=-O2 -Wall

# You generally should not modify these.
CXXFLAGS2=-std=c++1y -Itmp $(CXXFLAGS)

.PHONY: all clean

all: bin/sandstorm-tcp-listener-proxy

clean:
	rm -rf bin tmp

bin/sandstorm-tcp-listener-proxy: tmp/genfiles sandstorm-tcp-listener-proxy-main.c++ sandstorm-tcp-listener-proxy.h
	@mkdir -p bin
	@$(CXX) sandstorm-tcp-listener-proxy-main.c++ tmp/sandstorm/*.capnp.c++ -o bin/sandstorm-tcp-listener-proxy -static $(CXXFLAGS2) `pkg-config capnp-rpc --cflags --libs`

tmp/genfiles: /opt/sandstorm/latest/usr/include/sandstorm/*.capnp
	@echo "generating capnp files..."
	@mkdir -p tmp
	@capnp compile --src-prefix=/opt/sandstorm/latest/usr/include -oc++:tmp /opt/sandstorm/latest/usr/include/sandstorm/*.capnp
	@touch tmp/genfiles
