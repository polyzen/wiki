Security
========

.. toctree::
   :hidden:

   security/Transport_Layer_Security

Network
-------

`Fail2ban`__ : Python : brute-force protection
  Scans log files and bans IPs that show the malicious signs -- too many
  password failures, seeking for exploits, etc

  __ https://github.com/fail2ban/fail2ban

`nftables`__ : C : firewall
  Administration tool for packet filtering and classification

  __ https://netfilter.org/projects/nftables/

`OpenSSH`__ : C : secure services
  Free SSH protocol suite providing encryption for network services like remote
  login or remote file transfers

  - “`Secure Secure Shell`__”

  __ https://www.openssh.com/
  __ https://blog.stribik.technology/2015/01/04/secure-secure-shell.html

`WireGuard`__ : C : secure tunnel
  Extremely simple yet fast and modern VPN that utilizes state-of-the-art
  cryptography

  __ https://www.wireguard.com/

Virtualization
--------------

`Firejail`__ : C : sandbox
  SUID sandbox program that reduces the risk of security breaches by restricting
  the running environment of untrusted applications using Linux namespaces,
  seccomp-bpf and Linux capabilities

  __ https://firejail.wordpress.com/

`Docker`__ : Go : application container
  Run applications securely isolated in a container, packaged with all its
  dependencies and libraries

  __ https://www.docker.com/

`LXC`__ : C : system container
  Offers an environment as close as possible to the one you'd get from a VM but
  without the overhead that comes with running a separate kernel and simulating
  all the hardware

  __ https://linuxcontainers.org/

Web
---

.. seealso:: :doc:`security/Transport_Layer_Security`

HTTP headers
^^^^^^^^^^^^

`Content Security Policy (CSP)`__
  Mechanism by which web developers can control the resources which a particular
  page can fetch or execute, as well as a number of security-relevant policy
  decisions

  - `Quick Reference Guide`__

  __ https://www.w3.org/TR/CSP/
  __ https://content-security-policy.com/

`X-Content-Type-Options`__
  Require checking of a response’s `Content-Type` header against the
  destination of a request

  __ https://fetch.spec.whatwg.org/#x-content-type-options-header

Further reading
---------------

- `OWASP`__ - Free and open software security community

__ https://owasp.org
