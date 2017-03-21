Transport Layer Security
========================

`Let’s Encrypt`__
  Free, automated, and open Certificate Authority

  __ https://letsencrypt.org/

Resources
---------

“`Security/Server Side TLS`__”
  Contains information on TLS protocols, known issues and vulnerabilities,
  configuration examples and testing tools

  __ https://wiki.mozilla.org/Security/Server_Side_TLS

`Cipherli.st`__
  Strong Ciphers for Apache, nginx and Lighttpd

  __ https://cipherli.st/

`Weak Diffie-Hellman and the Logjam Attack`__
  Uncovered several weaknesses in how Diffie-Hellman key exchange has been
  deployed

  __ https://weakdh.org/

`Is TLS Fast Yet?`__
  Yes, yes it is.

  __ https://istlsfastyet.com/

Headers
^^^^^^^

`Public Key Pinning Extension for HTTP (HPKP)`__
  Allows web host operators to instruct user agents to remember ("pin") the
  hosts' cryptographic identities over a period of time

  - “`HTTP Public-Key-Pinning Explained`__”
  - `HPKP tutorial by Remy Van Elst`__

  __ https://tools.ietf.org/html/rfc7469.html
  __ https://timtaubert.de/blog/2014/10/http-public-key-pinning-explained/
  __ https://raymii.org/s/articles/HTTP_Public_Key_Pinning_Extension_HPKP.html

`HTTP Strict Transport Security (HSTS)`__
  Mechanism enabling web sites to declare themselves accessible only via secure
  connections and/or for users to be able to direct their user agent(s) to
  interact with given sites only over secure connections

  - `HSTS tutorial by Remy Van Elst`__

  __ https://tools.ietf.org/html/rfc6797.html
  __ https://raymii.org/s/tutorials/HTTP_Strict_Transport_Security_for_Apache_NGINX_and_Lighttpd.html

Diagnose
--------

`Observatory`__ : Python : CLI/Web
  Project designed to help developers, system administrators, and security
  professionals configure their sites safely and securely

  __ https://observatory.mozilla.org/

`Qualys SSL Labs SSL Server Test`__ : Web
  Performs a deep analysis of the configuration of any SSL web server on the
  public Internet

  __ https://www.ssllabs.com/ssltest/

`SSL Decoder`__ : PHP : CLI/Web
  PHP script which decodes an SSL connection and/or certificate and displays
  information

  __ https://ssldecoder.org/

`SSLyze`__ : Python : CLI
  Fast and powerful SSL/TLS server scanning library

  __ https://github.com/nabla-c0d3/sslyze

`testssl.sh`__ : Bash : CLI
  Testing TLS/SSL encryption anywhere on any port

  __ https://github.com/drwetter/testssl.sh
