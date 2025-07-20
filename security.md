# Security

```{toctree}
:hidden: true

security/Transport_Layer_Security
```

## Network

[Fail2ban](https://github.com/fail2ban/fail2ban) : Python : brute-force protection
: Scans log files and bans IPs that show the malicious signs -- too many
  password failures, seeking for exploits, etc

[nftables](https://netfilter.org/projects/nftables/) : C : firewall
: Administration tool for packet filtering and classification

[OpenSSH](https://www.openssh.com/) : C : secure services
: Free SSH protocol suite providing encryption for network services like remote
  login or remote file transfers

: - “[Secure Secure Shell](https://blog.stribik.technology/2015/01/04/secure-secure-shell.html)”

[WireGuard](https://www.wireguard.com/) : C : secure tunnel
: Extremely simple yet fast and modern VPN that utilizes state-of-the-art
  cryptography

## Virtualization

[Firejail](https://firejail.wordpress.com/) : C : sandbox
: SUID sandbox program that reduces the risk of security breaches by restricting
  the running environment of untrusted applications using Linux namespaces,
  seccomp-bpf and Linux capabilities

[Docker](https://www.docker.com/) : Go : application container
: Run applications securely isolated in a container, packaged with all its
  dependencies and libraries

[LXC](https://linuxcontainers.org/) : C : system container
: Offers an environment as close as possible to the one you'd get from a VM but
  without the overhead that comes with running a separate kernel and simulating
  all the hardware

## Web

:::{seealso}
{doc}`security/Transport_Layer_Security`
:::

### HTTP headers

[Content Security Policy (CSP)](https://www.w3.org/TR/CSP/)
: Mechanism by which web developers can control the resources which a particular
  page can fetch or execute, as well as a number of security-relevant policy
  decisions

: - [Quick Reference Guide](https://content-security-policy.com/)

[X-Content-Type-Options](https://fetch.spec.whatwg.org/#x-content-type-options-header)
: Require checking of a response’s `Content-Type` header against the
  destination of a request

## Further reading

- [OWASP](https://owasp.org) - Free and open software security community
