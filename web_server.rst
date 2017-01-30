Web server
==========

Performance
-----------

Cache/Proxy
^^^^^^^^^^^

- http://www.haproxy.org/
- http://www.memcached.org/
- https://www.varnish-cache.org/
- http://www.squid-cache.org/

Diagnose
^^^^^^^^

- https://github.com/wg/wrk
- https://github.com/giltene/wrk2
- https://github.com/marcelduran/yslow
- https://github.com/codesenberg/bombardier

Other considerations
^^^^^^^^^^^^^^^^^^^^

- https://enable-cors.org/
- https://hacks.mozilla.org/2015/11/better-than-gzip-compression-with-brotli/
- http://hhvm.com/

Transport Layer Security
------------------------

- https://wiki.mozilla.org/Security/Server_Side_TLS
- https://cipherli.st/

Certificate authorities
^^^^^^^^^^^^^^^^^^^^^^^

- http://www.cacert.org/
- https://www.freessl.com/
- `Let’s Encrypt  <https://letsencrypt.org/>`_ (recommended)
- https://www.namecheap.com/security/ssl-certificates.aspx

Headers
^^^^^^^

- https://raymii.org/s/articles/HTTP_Public_Key_Pinning_Extension_HPKP.html

  - https://timtaubert.de/blog/2014/10/http-public-key-pinning-explained/

- `HTTP Strict Transport Security <https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security>`_

  - https://raymii.org/s/tutorials/HTTP_Strict_Transport_Security_for_Apache_NGINX_and_Lighttpd.html

Diagnose
^^^^^^^^

- https://github.com/nabla-c0d3/sslyze
- https://github.com/drwetter/testssl.sh
- https://www.ssllabs.com/ssltest/
- https://ssldecoder.org/
- https://istlsfastyet.com/

Vulnerabilities
"""""""""""""""

- https://censys.io/blog/freak

  - https://tools.keycdn.com/freak

- http://disablessl3.com/
- https://weakdh.org/
- https://shaaaaaaaaaaaaa.com/ (has information on certs and intermediate certs)

Content Security Policy
-----------------------

- http://www.w3.org/TR/CSP/ 
- https://content-security-policy.com/

See also
--------

- :doc:`security`

Further reading
---------------

- `List_of_HTTP_header_fields <https://en.wikipedia.org/wiki/List_of_HTTP_header_fields>`_
- https://github.com/marcobiedermann/search-engine-optimization
