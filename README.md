Description
===========

This is a sample buildmaster configuration for Buildbot.
It is a splitted version of the original one, in order to treat the configuration in more modular fashion.

I did this to understand better the Buildbot configuration, but also to have a clean way to maintain my own configurations.

Requeriments
============

Obviously you'll need Buildbot installed to use this files as configuration for it ;-)

See [how to install Buildbot](http://buildbot.net/buildbot/docs/current/manual/installation.html)

Usage
=====

Here an example of how to try this configuration. Of course you can do this in any directory you are planning to use or try Buildbot instead of `/tmp/` and the name for the master's configurations (`my-master-dir`) could be anyone you like:

    $ cd /tmp/
    $ git clone git://github.com/juanje/buildbot-example-config.git my-master-dir
    $ buildbot create-master my-master-dir
    $ buildbot start my-master-dir


License and Authors
===================

This is basically the original Buildbot configuration example splitted, so it's a derived work of its authors:
* Brian Warner <warner-buildbot @ lothar . com>
* Dustin J. Mitchell <dustin@v.igoro.us>

And because of that, it should be distributed under the same license: **GPL v2**

Buildbot is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free
Software Foundation, version 2.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
Public License for more details.

For full details, please see the file named COPYING in the top directory
of the source tree. You should have received a copy of the GNU General
Public License along with this program. If not, see
<http://www.gnu.org/licenses/>.


This is also inspired on the [django-buildmaster](https://github.com/jacobian/django-buildmaster) from [Jacob Kaplan-Moss](https://github.com/jacobian).
