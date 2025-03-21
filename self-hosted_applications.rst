Self-hosted applications
========================

Bookmark managers
-----------------

`Shaarli`__ : PHP
  Personal, minimalist, super-fast, database free, bookmarking service

  __ https://github.com/shaarli/Shaarli

Calendars & Contacts
--------------------

`DAViCal`__ : PHP
  Server for calendar sharing

  __ https://www.davical.org/

`Radicale`__ : Python
  Simple calendar and contact server

  __ https://radicale.org/

`sabre/dav`__ : PHP
  Most popular WebDAV framework for PHP. Use it to create WebDAV, CalDAV and
  CardDAV servers

  __ https://sabre.io/

`Xandikos`__ : Python
  Lightweight yet complete CardDAV/CalDAV server that backs onto a Git
  repository

  __ https://github.com/jelmer/xandikos

.. _development-platforms:

Development platforms
---------------------

`GitLab FOSS`__ : Node.js/Ruby
  Open source end-to-end software development platform with built-in version
  control, issue tracking, code review, CI/CD, and more

  __ https://gitlab.com/gitlab-org/gitlab-foss

`Gitea`__ : Go
  Git with a cup of tea, painless self-hosted Git service

  __ https://gitea.io

`sourcehut`__ : Python
  Open source software suite for managing your software development projects

  __ https://sourcehut.org

Email
-----

Clients
^^^^^^^

`Mailpile`__ : Python
  Free & open modern, fast email client with user-friendly encryption and
  privacy features

  __ https://www.mailpile.is/

`Roundcube`__ : PHP
  Browser-based multilingual IMAP client with an application-like user interface

  __ https://roundcube.net/

Servers
^^^^^^^

`Dovecot`__ : C : retrieve
  Open source IMAP and POP3 email server for Linux/UNIX-like systems, written
  with security primarily in mind

  __ https://www.dovecot.org/

`OpenSMTPD`__ : C : transfer
  FREE implementation of the server-side SMTP protocol as defined by :RFC:`5321`,
  with some additional standard extension

  __ https://www.opensmtpd.org/

Feed readers
------------

`Feedbin`__ : Ruby
  RSS reader with a beautiful reading experience

  __ https://feedbin.com/

`FreshRSS`__ : PHP
  Free, self-hostable aggregator

  __ https://freshrss.org/

`Miniflux`__ : Go
  Minimalist and opinionated feed reader

  __ https://miniflux.app

`selfoss`__ : PHP
  Multipurpose RSS reader, live stream, mashup, aggregation web application

  __ https://selfoss.aditu.de/

`Tiny Tiny RSS`__ : PHP
  Open source web-based news feed (RSS/Atom) reader and aggregator

  __ https://tt-rss.org

**Reference:** https://www.devolve.net/self-hosted-open-source-rss-readers/

Read later
----------

`wallabag`__ : PHP
  Self hostable application for saving web pages

  __ https://wallabag.org

Wikis
-----

`DokuWiki`__ : PHP
  Simple to use and highly versatile Open Source wiki software that doesn't
  require a database

  __ https://www.dokuwiki.org/dokuwiki

`gitit`__ : Haskell
  Wiki using HAppS, pandoc, and Git

  __ https://github.com/jgm/gitit

`Gollum`__ : Ruby
  Simple, Git-powered wiki with a sweet API and local frontend

  __ https://github.com/gollum/gollum

`MediaWiki`__ : PHP
  Free software open source wiki package written in PHP, originally for use on
  Wikipedia

  __ https://www.mediawiki.org/wiki/MediaWiki

`Wiki.js`__ : Node.js
  Modern, lightweight and powerful wiki app built on NodeJS, Git and Markdown

  __ https://wiki.js.org/

.. note::
   Another option would be to pair a static site generator with a
   :ref:`development platform <development-platforms>`. This wiki uses
   `Sphinx`__ and `GitLab`__, see its `.gitlab-ci.yml`__ file.

   __ https://www.sphinx-doc.org
   __ https://docs.gitlab.com/user/project/pages/getting_started/pages_from_scratch/
   __ https://gitlab.com/polyzen/wiki/blob/master/.gitlab-ci.yml

See also
--------

- :doc:`console_applications`
- :doc:`security`
- :doc:`server_performance`
