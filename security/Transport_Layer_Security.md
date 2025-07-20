# Transport Layer Security

## HTTP headers

{rfc}`HTTP Strict Transport Security (HSTS) <6797>`
: Mechanism enabling web sites to declare themselves accessible only via secure
  connections and/or for users to be able to direct their user agent(s) to
  interact with given sites only over secure connections

: - “[HSTS tutorial by Remy Van Elst](https://raymii.org/s/tutorials/HTTP_Strict_Transport_Security_for_Apache_NGINX_and_Lighttpd.html)”

{rfc}`Online Certificate Status Protocol (OCSP) <2560>`
: Protocol useful in determining the current status of a digital certificate
  without requiring [Certificate Revocation Lists (CRLs)]

: - “[The case for “OCSP Must-Staple”](https://www.grc.com/revocation/ocsp-must-staple.htm)”

## Resources

[Is TLS Fast Yet?](https://istlsfastyet.com/)
: Yes, yes it is

[Let’s Encrypt](https://letsencrypt.org/)
: Free, automated, and open Certificate Authority

[moz://a SSL Configuration Generator](https://ssl-config.mozilla.org/)
: Builds configuration files to help you follow the Mozilla Server Side TLS
  configuration guidelines

## Test

[Observatory](https://developer.mozilla.org/en-US/observatory) : Python : CLI/Library/Web
: Project designed to help developers, system administrators, and security
  professionals configure their sites safely and securely

[Qualys SSL Labs SSL Server Test](https://www.ssllabs.com/ssltest/) : Web
: Performs a deep analysis of the configuration of any SSL web server on the
  public Internet

[SSLyze](https://github.com/nabla-c0d3/sslyze) : Python : CLI/Library
: Fast and powerful SSL/TLS server scanning library

[testssl.sh](https://github.com/testssl/testssl.sh) : Bash : CLI
: Testing TLS/SSL encryption anywhere on any port
