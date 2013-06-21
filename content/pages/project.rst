Projects
========

:title: Projects
:date: 2013-06-21 11:39

I like working with Open Source software, and contributing when I can. I have a
`Github account <https://github.com/bsandrow>`_ with some personal projects.

Some of my projects:

urilib_
    A library for dealing with URIs. Based on the RFCs, and with a bunch of
    unit tests. This project is waiting for me to get some outside opinions on
    the API design before I push it out to PyPI (there's an old version up
    there now) and begin trying to 'advertise' is to the rest of the dev
    community.

.. _urilib: https://github.com/bsandrow/urilib

MongoHN_
    My exploration of both Flask_ and MongoDB_ by creating a HackerNews_ clone.
    It's currently incomplete, but I work on it in my spare time.

.. _MongoHN: https://github.com/bsandrow/MongoHN
.. _Flask: http://flask.pocoo.org
.. _MongoDB: http://mongodb.org
.. _HackerNews: https://news.ycombinator.com

pytee_
    This is small library that emulates the behaviour of the Unix utility tee_.
    You get a file-like object that allows you to write to it once, and it will
    then write that out to multiple destinations. This turned out to be a
    little more difficult than I initially thought since a File-like object
    needs to *actually* have a ``fileno`` to interact with the subprocess_
    module.

.. _pytee: https://github.com/bsandrow/pytee
.. _tee: http://unixhelp.ed.ac.uk/CGI/man-cgi?tee
.. _subprocess: http://docs.python.org/2/library/subprocess.html

tmux.sh_
    A shell script wrapper around tmux that introduces some GNU screen-like
    behaviour. The functionality is there in newer versions tmux, but it's not
    something that is enabled/managed by default. This shell script aims to
    make it effort-less. See the README for a better explanation.

.. _tmux.sh: https://github.com/bsandrow/tmux.sh
