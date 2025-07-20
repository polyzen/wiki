# Self-hosted applications

## Bookmark managers

[Shaarli](https://github.com/shaarli/Shaarli) : PHP
: Personal, minimalist, super-fast, database free, bookmarking service

## Calendars & Contacts

[DAViCal](https://www.davical.org/) : PHP
: Server for calendar sharing

[Radicale](https://radicale.org/) : Python
: Simple calendar and contact server

[sabre/dav](https://sabre.io/) : PHP
: Most popular WebDAV framework for PHP. Use it to create WebDAV, CalDAV and
  CardDAV servers

[Xandikos](https://github.com/jelmer/xandikos) : Python
: Lightweight yet complete CardDAV/CalDAV server that backs onto a Git
  repository

(development-platforms)=

## Development platforms

[GitLab FOSS](https://gitlab.com/gitlab-org/gitlab-foss) : Node.js/Ruby
: Open source end-to-end software development platform with built-in version
  control, issue tracking, code review, CI/CD, and more

[Gitea](https://about.gitea.com) : Go
: Git with a cup of tea, painless self-hosted Git service

[sourcehut](https://sourcehut.org) : Python
: Open source software suite for managing your software development projects

## Email

### Clients

[Mailpile](https://www.mailpile.is/) : Python
: Free & open modern, fast email client with user-friendly encryption and
  privacy features

[Roundcube](https://roundcube.net/) : PHP
: Browser-based multilingual IMAP client with an application-like user interface

### Servers

[Dovecot](https://dovecot.org) : C : retrieve
: Open source IMAP and POP3 email server for Linux/UNIX-like systems, written
  with security primarily in mind

[OpenSMTPD](https://www.opensmtpd.org/) : C : transfer
: FREE implementation of the server-side SMTP protocol as defined by {RFC}`5321`,
  with some additional standard extension

## Feed readers

[Feedbin](https://feedbin.com/) : Ruby
: RSS reader with a beautiful reading experience

[FreshRSS](https://freshrss.org/) : PHP
: Free, self-hostable aggregator

[Miniflux](https://miniflux.app) : Go
: Minimalist and opinionated feed reader

[selfoss](https://selfoss.aditu.de/) : PHP
: Multipurpose RSS reader, live stream, mashup, aggregation web application

[Tiny Tiny RSS](https://tt-rss.org) : PHP
: Open source web-based news feed (RSS/Atom) reader and aggregator

**Reference:** <https://www.devolve.net/self-hosted-open-source-rss-readers/>

## Read later

[wallabag](https://wallabag.org) : PHP
: Self hostable application for saving web pages

## Wikis

[DokuWiki](https://www.dokuwiki.org/dokuwiki) : PHP
: Simple to use and highly versatile Open Source wiki software that doesn't
  require a database

[gitit](https://github.com/jgm/gitit) : Haskell
: Wiki using HAppS, pandoc, and Git

[Gollum](https://github.com/gollum/gollum) : Ruby
: Simple, Git-powered wiki with a sweet API and local frontend

[MediaWiki](https://www.mediawiki.org/wiki/MediaWiki) : PHP
: Free software open source wiki package written in PHP, originally for use on
  Wikipedia

[Wiki.js](https://wiki.js.org/) : Node.js
: Modern, lightweight and powerful wiki app built on NodeJS, Git and Markdown

:::{note}
Another option would be to pair a static site generator with a
{ref}`development platform <development-platforms>`. This wiki uses [Sphinx](https://www.sphinx-doc.org)
and [GitLab](https://docs.gitlab.com/user/project/pages/getting_started/pages_from_scratch/),
see its [.gitlab-ci.yml file](https://gitlab.com/polyzen/wiki/blob/master/.gitlab-ci.yml).
:::

## See also

- {doc}`console_applications`
- {doc}`security`
- {doc}`server_performance`
