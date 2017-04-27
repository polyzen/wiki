Server performance
==================

Cache/Load balance
------------------

`HAProxy`__ : C : load balancer
  Free, fast and reliable solution offering high availability, load balancing,
  and proxying for TCP and HTTP-based applications

  __ http://www.haproxy.org/

`memcached`__ : C : memory cache
  Free & open source, high-performance, distributed memory object caching
  system, generic in nature, but intended for use in speeding up dynamic web
  applications by alleviating database load

  __ http://www.memcached.org/

`Varnish`__ : C : caching proxy
  Web application accelerator also known as a caching HTTP reverse proxy

  __ https://www.varnish-cache.org/

Diagnose
--------

`wrk`__ / `wrk2`__ : C
  HTTP benchmarking tool / Constant throughput, correct latency recording
  variant

  __ https://github.com/wg/wrk
  __ https://github.com/giltene/wrk2

`YSlow`__ : JS
  Analyzes web pages and why they're slow based on Yahoo!'s rules for high
  performance web sites

  __ http://yslow.org/

`bombardier`__ : Go
  HTTP(S) benchmarking tool

  __ https://github.com/codesenberg/bombardier

See also
--------

- :doc:`security`

Further reading
---------------

- `Cross-Origin Resource Sharing (CORS)`__ - Mechanism to enable client-side
  cross-origin requests
- `HHVM`__ - Open-source virtual machine designed for executing programs written
  in Hack and PHP
- `Zstandard (zstd)`__ - Real-time compression algorithm, providing
  high compression ratios

__ https://enable-cors.org/
__ http://hhvm.com/
__ https://facebook.github.io/zstd/
