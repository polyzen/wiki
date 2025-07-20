# Server performance

## Cache/Load balance

[HAProxy](https://www.haproxy.org/) : C : load balancer
: Free, fast and reliable solution offering high availability, load balancing,
  and proxying for TCP and HTTP-based applications

[memcached](https://www.memcached.org/) : C : memory cache
: Free & open source, high-performance, distributed memory object caching
  system, generic in nature, but intended for use in speeding up dynamic web
  applications by alleviating database load

[Varnish](https://varnish-cache.org/) : C : caching proxy
: Web application accelerator also known as a caching HTTP reverse proxy

## Test

### Benchmark

[bombardier](https://github.com/codesenberg/bombardier) : Go
: Fast cross-platform HTTP benchmarking tool

[WebPagetest](https://github.com/catchpoint/WebPageTest) : PHP/Python
: Free website speed test from multiple locations around the globe using real
  browsers (IE and Chrome) and at real consumer connection speeds

[wrk](https://github.com/wg/wrk) : C
: Modern HTTP benchmarking tool capable of generating significant load when run
  on a single multi-core CPU

### Load test

[drill](https://github.com/fcsonline/drill) : Rust
: HTTP load testing application written in Rust inspired by Ansible syntax

[Vegeta](https://github.com/tsenart/vegeta) : Go
: Versatile HTTP load testing tool built out of a need to drill HTTP services
  with a constant request rate

## See also

- {doc}`security`

## Further reading

- [Cross-Origin Resource Sharing (CORS)](https://enable-cors.org/) - Mechanism
  to enable client-side cross-origin requests
- [Zstandard (zstd)](https://facebook.github.io/zstd/) - Real-time compression
  algorithm, providing high compression ratios
