Transport Layer Security
========================

HTTP headers
------------

:rfc:`HTTP Strict Transport Security (HSTS) <6797>`
  Mechanism enabling web sites to declare themselves accessible only via secure
  connections and/or for users to be able to direct their user agent(s) to
  interact with given sites only over secure connections

  - “`HSTS tutorial by Remy Van Elst`__”

  __ https://raymii.org/s/tutorials/HTTP_Strict_Transport_Security_for_Apache_NGINX_and_Lighttpd.html

:rfc:`Online Certificate Status Protocol (OCSP) <2560>`
  Protocol useful in determining the current status of a digital certificate
  without requiring [Certificate Revocation Lists (CRLs)]

  - “`The case for “OCSP Must-Staple”`__”

  __ https://www.grc.com/revocation/ocsp-must-staple.htm

Resources
---------

`Is TLS Fast Yet?`__
  Yes, yes it is

  __ https://istlsfastyet.com/

`Let’s Encrypt`__
  Free, automated, and open Certificate Authority

  __ https://letsencrypt.org/

“`Security/Server Side TLS`__”
  Contains information on TLS protocols, known issues and vulnerabilities,
  configuration examples and testing tools

  __ https://wiki.mozilla.org/Security/Server_Side_TLS

Test
----

`Observatory`__ : Python : CLI/Library/Web
  Project designed to help developers, system administrators, and security
  professionals configure their sites safely and securely

  __ https://developer.mozilla.org/en-US/observatory

`Qualys SSL Labs SSL Server Test`__ : Web
  Performs a deep analysis of the configuration of any SSL web server on the
  public Internet

  __ https://www.ssllabs.com/ssltest/

`SSLyze`__ : Python : CLI/Library
  Fast and powerful SSL/TLS server scanning library

  __ https://github.com/nabla-c0d3/sslyze

`testssl.sh`__ : Bash : CLI
  Testing TLS/SSL encryption anywhere on any port

  __ https://github.com/testssl/testssl.sh
