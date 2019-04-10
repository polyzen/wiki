Server performance
==================

Cache/Load balance
------------------

`HAProxy`__ : C : load balancer
  Free, fast and reliable solution offering high availability, load balancing,
  and proxying for TCP and HTTP-based applications

  __ https://www.haproxy.org/

`memcached`__ : C : memory cache
  Free & open source, high-performance, distributed memory object caching
  system, generic in nature, but intended for use in speeding up dynamic web
  applications by alleviating database load

  __ https://www.memcached.org/

`Varnish`__ : C : caching proxy
  Web application accelerator also known as a caching HTTP reverse proxy

  __ https://varnish-cache.org/

Test
----

Benchmark
^^^^^^^^^

`bombardier`__ : Go
  Fast cross-platform HTTP benchmarking tool

  __ https://github.com/codesenberg/bombardier

`WebPagetest`__ : PHP/Python
  Free website speed test from multiple locations around the globe using real
  browsers (IE and Chrome) and at real consumer connection speeds

  __ https://webpagetest.org/

`wrk`__ : C
  Modern HTTP benchmarking tool capable of generating significant load when run
  on a single multi-core CPU

  __ https://github.com/wg/wrk

Load test
^^^^^^^^^

`Vegeta`__ : Go
  Versatile HTTP load testing tool built out of a need to drill HTTP services
  with a constant request rate

  __ https://github.com/tsenart/vegeta

See also
--------

- :doc:`security`

Further reading
---------------

- `Cross-Origin Resource Sharing (CORS)`__ - Mechanism to enable client-side
  cross-origin requests
- `Zstandard (zstd)`__ - Real-time compression algorithm, providing
  high compression ratios

__ https://enable-cors.org/
__ https://facebook.github.io/zstd/
