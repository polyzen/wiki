Security
========

.. toctree::
   :hidden:

   security/Transport_Layer_Security

Pentest
-------

`Damn Vulnerable Web Application (DVWA)`__ : PHP/MySQL
  Practice some of the most common web vulnerability, with various difficultly
  levels, with a simple straightforward interface

  __ http://www.dvwa.co.uk/

`Kali Linux`__ : OS
  Debian-based Linux distribution aimed at advanced Penetration Testing and
  Security Auditing

  __ https://www.kali.org/

Safeguard
---------

Network
^^^^^^^

`nftables`__ : C : firewall
  Administration tool for packet filtering and classification

  __ https://netfilter.org/projects/nftables/

`OpenSSH`__ : C : secure services
  Free SSH protocol suite providing encryption for network services like remote
  login or remote file transfers

  - “`Secure Secure Shell`__”
  - `Rebex SSH Check`__

  __ https://www.openssh.com/
  __ https://stribika.github.io/2015/01/04/secure-secure-shell.html
  __ https://sshcheck.com/

`OpenVPN`__ : C : secure tunnel
  Full-featured open source SSL VPN solution that accommodates a wide range of
  configurations

  __ https://openvpn.net/

`sshguard`__ : C : brute-force protection
  Aggregates system logs and blocks repeat offenders using one of several
  firewall backends

  __ https://www.sshguard.net

`WireGuard`__ : C : secure tunnel
  Extremely simple yet fast and modern VPN that utilizes state-of-the-art
  cryptography

  __ https://www.wireguard.com/

Virtualization
^^^^^^^^^^^^^^

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
^^^

.. seealso:: :doc:`security/Transport_Layer_Security`

`Content Security Policy (CSP)`__ : HTTP header
  Mechanism by which web developers can control the resources which a particular
  page can fetch or execute, as well as a number of security-relevant policy
  decisions

  - `Quick Reference Guide`__

  __ https://www.w3.org/TR/CSP/
  __ https://content-security-policy.com/

Further reading
---------------

- `OWASP`__ - Free and open software security community

__ https://www.owasp.org/index.php/Main_Page
