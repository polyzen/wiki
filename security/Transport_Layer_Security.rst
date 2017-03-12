Transport Layer Security
========================

`Security/Server Side TLS <https://wiki.mozilla.org/Security/Server_Side_TLS>`_
  Contains information on TLS protocols, known issues and vulnerabilities,
  configuration examples and testing tools

`Cipherli.st <https://cipherli.st/>`_
  Strong Ciphers for Apache, nginx and Lighttpd

`Is TLS Fast Yet? <https://istlsfastyet.com/>`_
  Yes, yes it is.

`Let’s Encrypt  <https://letsencrypt.org/>`_
  Free, automated, and open Certificate Authority

Headers
-------

Public Key Pinning Extension for HTTP (HPKP) :RFC:`7469`
  Allows web host operators to instruct user agents to remember ("pin") the
  hosts' cryptographic identities over a period of time

- `HTTP Public-Key-Pinning Explained <https://timtaubert.de/blog/2014/10/http-public-key-pinning-explained/>`_
- `HPKP tutorial by Remy Van Elst <https://raymii.org/s/articles/HTTP_Public_Key_Pinning_Extension_HPKP.html>`_

HTTP Strict Transport Security (HSTS) :RFC:`6797`
  Mechanism enabling web sites to declare themselves accessible only via secure
  connections and/or for users to be able to direct their user agent(s) to
  interact with given sites only over secure connections

- `HSTS tutorial by Remy Van Elst <https://raymii.org/s/tutorials/HTTP_Strict_Transport_Security_for_Apache_NGINX_and_Lighttpd.html>`_

Diagnose
--------

`Qualys SSL Labs SSL Server Test <https://www.ssllabs.com/ssltest/>`_ : Online
  Performs a deep analysis of the configuration of any SSL web server on the
  public Internet

`SSL Decoder <https://ssldecoder.org/>`_ : PHP
  PHP script which decodes an SSL connection and/or certificate and displays
  information

`SSLyze <https://github.com/nabla-c0d3/sslyze>`_ : Python
  Fast and powerful SSL/TLS server scanning library

`testssl.sh <https://github.com/drwetter/testssl.sh>`_ : Bash
  Testing TLS/SSL encryption anywhere on any port

Vulnerabilities
^^^^^^^^^^^^^^^

- `Disable SSL3 <http://disablessl3.com/>`_
- `FREAK <https://censys.io/blog/freak>`_

  - https://tools.keycdn.com/freak

- `SHA-1 certificates <https://shaaaaaaaaaaaaa.com/>`_ (has information on
  certs and intermediate certs)
- `Weak Diffie-Hellman and the Logjam Attack <https://weakdh.org/>`_
